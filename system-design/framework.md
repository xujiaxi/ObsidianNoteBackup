# System Design 答题框架（Answering Framework，45 分钟流程版）

> 来源 / Source：Day 1 讲解整理（2026-09-18）
> 配套 / Companions：`plans/two-week-plan-2026-09-18.md`、`system-design/fundamentals.md`、`system-design/metrics-monitoring.md`
> 用法 / Usage：每道设计题的 `system-design/{theme}.md` 都按本文第 6 节的模板产出（every design doc follows the template in §6）

## 1. 时间分配（Time Allocation —— 把面试当流程走）

| 阶段 Phase | 时间 | 你要做的事 | 千万不要做 |
|---|---|---|---|
| 需求澄清 Clarification | 0–5 min | 问五问，然后**复述确认**（restate and confirm） | 上来就画框图 |
| 容量估算 Estimation | 5–10 min | 算 QPS / 存储 / 带宽 / 机器数 | 说"规模不大不用算" |
| API + 数据模型 API + data model | 10–15 min | 3–5 个端点 + 表结构 + 存储选型理由 | 写完整 SQL / Protobuf |
| 高层架构 High-level design | 15–30 min | 组件 + 数据流（画图 + 口述一条请求路径） | 一上来就谈多机房 |
| 深挖 Deep dive | 30–40 min | 面试官指定；答"怎么做 + 为什么" | 只给结论不给取舍 |
| 收尾 Wrap-up | 40–45 min | 失败模式、降级、演进路线、反问 | 说"设计完了"然后沉默 |

**核心原则**：前 15 分钟只动嘴不动笔。面试官打分里「是否先定义问题」权重很高。

▸ **Say it in English**
> "Before drawing anything, let me spend the first five minutes on requirements, because those answers change the architecture. Then I'll do a quick back-of-the-envelope estimate, pin down the API and data model, and only then draw the high-level design."

## 2. 需求澄清五问（The Five Clarifying Questions，背熟）

1. **核心用户动作是什么**，谁是主要读方、谁是主要写方？（core user action; main readers vs main writers）
2. **规模**：DAU 多少、峰值 QPS、数据量级、数据保留多久？（scale: DAU, peak QPS, data volume, retention）
3. **读写比例**多少？（决定推/拉、缓存策略、有序结构要不要预维护）*Read/write ratio — decides push vs pull, caching, whether an ordered structure must be pre-maintained.*
4. **一致性要求**：强一致还是最终一致？延迟 SLA 多少？（决定单主/多主/CRDT）*Consistency: strong or eventual? Latency SLA?*
5. **边界**：多区域？移动端？合规（PII/支付）？成本约束？*Boundaries: multi-region, mobile, compliance, cost.*

收尾话术（closing script）：「我理解这个系统需要支持 X 做 Y，规模是 Z，允许最终一致但延迟要在 W 以内——如果理解有偏差请纠正我。」
*"My understanding is that this system must let X do Y, at a scale of Z, allowing eventual consistency but with latency under W — please correct me if that's off."*

## 3. 容量估算速算手册（Capacity Estimation Cheat Sheet）

### 3.1 常数表（Constants，记这几个就够）

| 量 Quantity | 值 Value | 用途 Use |
|---|---|---|
| 一天 one day | ≈ 86,400s，**按 10^5 算** | 日均 → QPS |
| 一个月 one month | 2.6 × 10^6 s | |
| 一年 one year | 3.15 × 10^7 s ≈ 3 × 10^7 | 年存储 annual storage |
| 单机 Web 服务 single web server | 1K–10K QPS | 应用层机器数 |
| 单实例 MySQL | 写 1K–10K TPS；索引读 10K QPS | 存储选型 |
| Redis 单实例 | 10^5 QPS | 缓存 / 榜单 |
| 单机内存 single machine RAM | 128–256 GB | 能不能全放内存 |
| SSD 随机 IOPS | 10K–100K | 是否需要 LSM 结构 |
| 可用性 availability | 99.9% = 8.76h/年；99.99% = 52.6min/年 | SLA 话术 |

### 3.2 公式链（Formula Chain，按顺序算，别跳步）

```
日均请求   daily requests  = DAU × 人均日操作数 (actions per user per day)
平均 QPS   average QPS     = 日均请求 / 10^5
峰值 QPS   peak QPS        = 平均 × 3   （社交/电商 3~5，内部工具 2）
日增存储   daily storage   = 日请求 × 单条大小 (size per record)
年存储     annual storage  = 日增 × 365 × 副本数(3) × 索引放大(1.5)
出带宽     egress BW       = 峰值 QPS × 平均响应大小
机器数     machine count   = 峰值 QPS / 单机容量 ÷ 0.7（留余量 headroom）
缓存内存   cache memory    = 热数据条数 × 单条大小（热数据通常取 20%）
```

### 3.3 演练 A：News Feed（200M DAU）

- 读：200M × 10 次/天 = 2B/天 → **20K QPS 平均，60K 峰值**
- 写：200M × 0.1 帖/天 = 20M/天 → 200 QPS → 峰值 600 QPS
- 读写比 **100:1** → 结论：重缓存 + 预生成 timeline（fanout on write），**读路径不能碰 DB**
- 存储：20M × 1KB = 20GB/天 → 7.3TB/年，×3 副本 ≈ 22TB
- 结论：应用机约 60 台（按 1K QPS/台算 60K 峰值）；Redis 存热 timeline：200M × 800 条 × 8B(post_id) ≈ 1.3TB → 分片约 20 台

### 3.4 演练 B：视频上传（100M DAU，面经 #5）

- 上传数：100M × 0.01 视频/天 = 1M 视频/天 → 12 QPS 平均，峰值约 40 QPS
- 大小：1M × 200MB = **200TB/天** ← 一眼看出瓶颈在存储不在 QPS
- 年存储：200TB × 365 × 1.2（多码率转码）= 87PB → 对象存储 + 冷层
- 上传带宽：40 QPS × 200MB / 300s = **27GB/s** → 必须分片直传对象存储 + CDN 边缘接入，**绝不过应用服务器**
- 转码算力：1M 视频 × 5min = 5M 分钟素材/天；3 档码率 × 0.5x 实时速度 → 5M × 3 / 0.5 = 30M 机器分钟/天 = 20,833 机器小时 → 24h 跑满约 **870 台转码机**（70% 利用率约 1250 台）

**这套算法就是面试官想听的**：不是背数字，而是从数字推出架构决策（"27GB/s 决定了不能过应用层"）。

▸ **Say it in English**
> "Let me do the arithmetic out loud, because the number itself drives the design: a million videos a day at 200 MB each is 200 TB per day, and the upload rate works out to about 27 GB/s. That's six times more than any reasonable application-tier fleet can absorb, so uploads have to go multipart and direct into object storage, with the CDN handing off at the edge. The application layer never sees the bytes."

## 4. 高层设计怎么讲（How to Present the High-Level Design，15 分钟）

1. 先画 4 层：客户端 → 接入层（LB/CDN）→ 服务层（无状态）→ 存储层（缓存/DB/对象存储/队列）
2. 然后**用一条请求路径串起来**：「用户发帖 → API 网关 → 帖子服务写主库 → 发消息到队列 → 扇出服务写 timeline → 读时直接读 Redis timeline」
3. 每个组件说一句选型理由，**不要列产品名清单**
4. 主动提一个「我先不做」的部分（如"v1 不做多区域，后面演进再加"）→ 显示边界感

▸ **Say it in English**
> "Four layers to start: clients, the edge with load balancing and CDN, a stateless service tier, and storage. Let me walk one request end to end rather than describe boxes in isolation: the client posts, the API gateway routes it, the post service writes to the primary database, publishes to a queue, the fanout service writes the timelines, and reads then go straight to the Redis timeline without touching the database."
>
> "One thing I'm deliberately not doing in v1 is multi-region — I'd rather make the single-region path solid first and add regions in the evolution."

## 5. 深挖与失败模式（Deep Dives and Failure Modes —— 面试官最爱的三连）

- **数据一致性 consistency**：写扩散怎么保证不丢帖？（outbox/队列 + 幂等 + 重试）
- **热点 hotspots**：明星用户 / 爆款帖子？（拉模式兜底 + 本地缓存 + 请求合并 request coalescing）
- **降级 degradation**：Redis 挂了读什么？（降级直连 DB + 限流 + 返回陈旧数据 serve stale）
- **扩缩容 scaling**：分片键怎么选？扩分片怎么迁数据？（一致性哈希 / 预分片 pre-sharding）
- **可观测性 observability**：出问题怎么定位？（埋点 + 尾延迟 tail latency + 队列堆积告警）

▸ **Say it in English**
> "For each component I'd also define how it degrades. If Redis is gone, reads fall back to the database behind a rate limiter and we serve slightly stale data rather than fail. If a celebrity posts and the fanout queue backs up, we switch that account to a pull-based path instead of writing a hundred million timeline entries."

## 6. 每份设计文档的统一模板（Unified Template）

```
## 需求澄清 Requirements clarification（功能性 / 非功能性 / 规模假设）
## 容量估算 Capacity estimation（QPS、存储、带宽、机器数）
## API 设计 API design
## 数据模型与存储选型 Data model & storage selection（含"为什么不是另一个 why not the alternative"）
## 高层架构 High-level architecture（组件 + 数据流 components + data flow）
## 深挖点 Deep dives（3 个，每个 5 分钟）
## 失败模式与降级 Failure modes & degradation
## 演进路线 Evolution path（v1 → v2）
```

## 7. Day 1 自测题（Self-Test —— 做完 coding 后回答）

中英双问，用英文答（answer in English）：

1. **澄清练习**：面经 #16（电商库存管理）——写出你要问的 5 个澄清问题，每个问题后面写出"无论他怎么答，我的设计会怎么变"。
   *Clarification drill: interview #16 (e-commerce inventory) — write the five clarifying questions, and after each, how your design changes depending on the answer.*
2. **估算练习**：论证为什么视频上传的瓶颈是带宽而不是 QPS（用演练 B 的数字）。
   *Estimation drill: argue why the bottleneck for video upload is bandwidth, not QPS, using the numbers from worked example B.*
3. **决策练习**：面经 #12（Leaderboard 10M DAU）——若 QPS 只有 100，还需要 Redis ZSet 吗？为什么面试官仍然期待"跳表"这个答案？
   *Decision drill: interview #12 (leaderboard, 10M DAU) — if QPS were only 100, would you still need a Redis ZSet? Why does the interviewer still expect "skip list" as the answer?*
4. **口径练习**：把 News Feed 的设计压成 5 句话（面试官说"假设我们没时间了，一句话讲你的核心思路"）。
   *Compression drill: compress the News Feed design into five sentences — "we're out of time, give me the core idea in one breath."*
