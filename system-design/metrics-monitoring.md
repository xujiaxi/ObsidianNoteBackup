# M1 · 指标监控系统（Metrics / Monitoring System）

> 面经来源 / Sources：#3 Multi-Region Metrics Monitoring System、#15 Metric collection & query system
> 母题 / Archetype：从零设计一个 Datadog / Prometheus 级别的指标采集、存储、查询、告警平台
> 配套 / Companion：`system-design/framework.md`（答题流程与估算公式链 / answering flow + estimation chain）
> 分两半 / Split：**Part 1（Day 2）** = 采集模型 + 时序数据模型 + 写入路径 + 查询语言；**Part 2（Day 3）** = 降采样保留 + 多区域聚合 + 告警评估 + 基数治理

---

# Part 1 · 地基（Foundations, Day 2）

## 0. 这道题在考什么（What this question is really testing）

面经两条是同一母题的两个切面（two facets of one archetype）：

| 面经 Entry | 范围 Scope | 侧重 Emphasis |
|---|---|---|
| #15 指标收集与查询系统 | 单区域 Single region | **写入路径 + 查询语言**（write path + query language） |
| #3 多区域指标监控 | 多区域 Multi region | **数据本地性 + 跨区聚合 + 一致性**（locality + cross-region aggregation） |

面试官实际在测四件事（按权重排序 / ranked by weight）：

| #   | 测什么                         | Why it matters                                                                    |
| --- | --------------------------- | --------------------------------------------------------------------------------- |
| 1   | 你会不会先定义问题（前 15 分钟只动嘴）       | Do you define the problem before drawing boxes?                                   |
| 2   | 你知不知道"机器写的系统"和"人写的系统"架构不同   | Machine-generated vs human-generated traffic                                      |
| 3   | 每个组件能不能说清选型理由（不是列产品名）       | Justify components, don't recite product names                                    |
| 4   | 你知不知道本领域的真实痛点：基数、乱序、读放大、降采样 | **Real pain points: cardinality, out-of-order, read amplification, downsampling** |

第 4 条是"背过系统设计"和"真做过"的分水岭（the divider between memorized and operated）。

▸ **Say it in English**
> "Before I draw anything, let me frame what makes this system unusual: the writers are machines emitting a constant stream of data points, and the readers are dashboards, an alerting engine, and humans doing ad-hoc debugging. That shape drives everything downstream."

## 1. 需求澄清（Requirements Clarification）

每个问题都要说清"答案如何改变设计"（always state how the answer changes the design）。

### 1.1 谁写谁读（Who writes, who reads）

**写方是机器（writers are machines）**：Agent / SDK / exporter。无人值守、速率恒定、不关心单点是否成功（允许最终一致）、写源数量几万个、没有耐心——延迟高就丢点而不是重试到天亮。

**读方有三类，必须自己拆出来（three kinds of readers — split them out yourself）**：

| 读方 Reader | 访问模式 Pattern | 延迟敏感度 Latency sensitivity | 设计后果 Consequence |
|---|---|---|---|
| Grafana 看板 Dashboards | 周期性、查询固定、可缓存 | 宽容（1–2s 可接受） | 走热缓存 / 近期数据（hot cache / recent data） |
| 告警引擎 Alerting engine | 每分钟评估、窗口短 | **极敏感**——数据晚到 = 漏报 | 必须与写入路径解耦，且优先级最高（decoupled + prioritized） |
| 工程师临时排查 Ad-hoc debugging | 一次性、范围大、要灵活 | 宽容（几十秒也行） | 走 rollup、限流、可转异步（rollups, rate-limited, async） |

**为什么这个拆解重要**：它决定你要**一条路径**还是**多条**。正解是热路径（近 2 小时常驻内存/SSD）给看板和告警用，冷路径（>1 天）读降采样后的 rollup。如果只答"读多写少要加缓存"，就把这道题答成了 CRUD 题。

### 1.2 规模（Scale）

必须问出三个原始数（three raw numbers）：**主机/容器数、每主机活跃指标数、采集间隔**。再问四个衍生问题：标签维度有多少、保留多久、单点多大（文本还是二进制）、是否必须多区域。

追问预案：*"200 个指标是怎么来的？"* 答：应用自埋点 + node_exporter（CPU/内存/磁盘/网络约 60 个）+ 容器指标 + 运行时/JVM 指标，一个中等规模微服务实例通常 100–500。**给区间比给单点数字更可信。**

### 1.3 读写比——所有人都踩的坑（the trap everyone falls into）

要区分两个完全不同的比值（two completely different ratios）：

| 比值 Ratio                      | 数值 Value                                           | 原因 Why                  |
| ----------------------------- | -------------------------------------------------- | ----------------------- |
| 请求次数比（request count）          | 10:1 ~ 100:1（写多 write-heavy）                       | 机器持续在写，人偶尔看一眼           |
| **数据放大比（data amplification）** | 10^3 ~ 10^4（**读贵得多 reads are far more expensive**） | 写一个点 16 字节；一次查询可能扫几十亿个点 |

正确结论：**写路径优化吞吐与成本，读路径优化扫描点数**（write path optimizes throughput and cost; read path optimizes points scanned）。两个解法毫无交集：写 = LSM / Kafka / 列式压缩；读 = 索引预筛 / rollup / 缓存。

> 主动说出这个反直觉结论：「请求数上是写多读少，数据量上是读重写轻，所以两条路径要独立优化。」

### 1.4 一致性——分三层答，不要只答一层（answer in three layers）

**第一层 · 数据完整性，能丢点吗（data completeness）**：可以，但要**按指标类型区分**：

| 类型 | 丢点后果 |
|---|---|
| gauge（内存用量） | 无所谓，点与点之间独立 |
| counter（请求总数） | **破坏 rate() 计算**——缺口必须被标记，让 rate() 跳过而不是把 gap 摊平（否则算出的速率偏低） |

说出这条等于告诉面试官你运维过监控栈。

**第二层 · 时序一致性，迟到的点怎么办（late points）**：允许回填窗口（约 5 分钟）接收乱序点；超出则丢弃并**计数打点**（详见 §5.6）。

**第三层 · 语义一致性（最关键）：告警不能因为数据延迟而漏报。** 所以：告警评估与写入路径解耦（独立消费者、独立限流），用"评估窗口 + for 持续时间"抗抖动，并且必须有**陈旧标记（staleness handling）**——series 超过 N 个采集周期没有新点，查询返回"无数据"而不是沿用最后一个值。否则一个已经死掉的服务会永远显示最后一个健康值，**告警永不触发**（僵尸数据 zombie data）。

> 收尾话术：「监控系统对一致性的答案是**最终一致 + 丢失可见**，不是强一致。丢了多少、丢在哪，必须有指标暴露出来。」

### 1.5 边界——"多区域"是题眼，拆成三个问题反问他（split "multi-region" into three readings）

| 理解 Reading                                  | 改的是设计的哪一块 What changes                                |
| ------------------------------------------- | ----------------------------------------------------- |
| **A. 采集端分布多区域**（collectors distributed）     | 传输与数据本地性：各区域本地写本地存，跨区只传降采样结果（transport & locality）    |
| **B. 查询端多区域**（queriers distributed，用户全球就近查） | 查询路由与副本：每区域要有全量副本，或跨区扇出 + 结果合并（routing & replication） |
| **C. 需要全球视图**（global view）                  | 聚合层：全局查询层做分区聚合，还要处理时钟偏斜与时间边界对齐（aggregation layer）     |

标准答案：**A 是 v1 必做（也最省），B/C 是 v2/v3。** 主动说"A 和 B 的工程量差一个数量级，我先把 A 做扎实"——这正是评分项里的"边界感"。

另外两个边界要主动问：**成本**（存储 + 跨区带宽是成本大头，成本本身就是一条非功能需求）和**合规**（指标本体一般不含 PII，但 label 可能含 tenant_id / email → 网关强制 label 白名单）。

▸ **Say it in English**
> Restatement: "Let me make sure I have the problem right. Writers are machines — about 50,000 agents emitting roughly 200 metrics each every 10 seconds, so around a million data points per second. Readers are dashboards, an alerting engine, and engineers debugging. We can accept eventual consistency and some data loss, but alerts have to be correct, because a missed alert is worse than a missing data point. Multi-region collection is required. Correct me if that's off."
>
> Read/write framing: "It's write-heavy in request count — 10 to 100 times more writes than reads — but read-heavy in data volume by three to four orders of magnitude. One write is 16 bytes; one month-long dashboard query can scan billions of points. So I'll optimize the write path for throughput and cost, and the read path for points scanned. Those two solutions are completely disjoint."
>
> Consistency: "I separate three layers. First, data completeness — dropping a gauge point is harmless, but dropping a counter point breaks rate(), so the gap has to be marked. Second, late points — I'll allow a short backfill window, beyond that I drop and count. Third and most important, alerts must not be missed because data arrived late, which means alert evaluation is decoupled from the write path and I need staleness handling. Otherwise a dead service reports its last healthy value forever and the alert never fires."

## 2. 容量估算（Capacity Estimation）

普通题从 QPS 起步；这题必须从 **DPS（数据点/秒，data points per second）** 起步——机器不产生"请求"，只产生数据点。

### 2.1 公式链（the formula chain）

```
DPS              = hosts × active metrics per host ÷ collection interval (s)
series count     = Σ over metrics of (product of label value counts)
write bandwidth  = DPS × bytes per point on the wire  (binary 12–16B; text 80–150B)
raw storage/yr   = DPS × bytes per point × 3.15×10^7
compressed/yr    = raw ÷ compression ratio  (columnar time-series 10–12× ≈ 1.4B/point)
index memory     = active series × 2–3 KB
```

### 2.2 把这组数字算出来（worked numbers，面试就报这组）

| 量 Quantity | 计算 Calculation | 结果 Result |
|---|---|---|
| DPS | 50,000 × 200 ÷ 10s | **1,000,000 点/秒** |
| 写入带宽（二进制线格式 binary） | 1M × 16 B | **16 MB/s** |
| 写入带宽（文本格式 text，对比用） | 1M × 100 B | 100 MB/s ← **6× 差距纯粹来自编码选择** |
| series 理论上限 theoretical bound | 50,000 × 200 | 1000 万（还没算额外 label 维度） |
| 压缩后存储（15 天原始） | 1M × 1.4 B × 86,400 × 15 | **1.8 TB**（热数据其实很小） |
| 1 分钟 rollup，保留 1 年 | 166K × 12 B × 3.15e7 | **63 TB**（rollup 点更大：存 sum/count/min/max） |
| 1 小时 rollup，保留 3 年 | 2.8K × 12 B × 9.5e7 | **3.2 TB** |
| 合计 | 分层保留 layered retention | **≈68 TB → 3 副本约 200 TB** |
| 索引内存 index memory | 1000 万 series × 2.5 KB | **约 25 GB** ← 真正的单机天花板 |

注意这个表述方式：不是"每年 44TB 原始点"，而是一份**分层保留方案**，显示你在控制成本。

### 2.3 每个数字对应一个架构决策（every number forces a decision）

| 数字 Number    | 逼出的决策 Decision                                       |
| ------------ | ---------------------------------------------------- |
| 16 MB/s 入带宽  | 普通 Kafka（3 broker，3–5 分区）足够——**带宽不是瓶颈**              |
| 约 25 GB 索引内存 | 必须按 hash(series) 分片；写入节点 5–10 台（每台 100–200 万 series） |
| 1.8 TB 热数据   | 本地 NVMe/SSD 即可，不需要特殊存储                               |
| ≈68 TB 冷数据   | **必须**上对象存储；本地盘成本不可接受                                |
| 写查互相挤占       | 写入节点与查询节点分离                                          |
|              |                                                      |

> **必背一句（memorize）**：「这类系统的瓶颈不是 QPS，而是**基数 × 时间（cardinality × time）**带来的存储与查询放大。1M DPS 的入带宽只有 16 MB/s 不值一提，但 1000 万 series 的索引内存和一次跨月聚合就能把单机打爆。」

▸ **Say it in English**
> "The unit here isn't QPS, it's data points per second — 50,000 hosts times 200 metrics over a 10-second interval is a million points per second. In binary batch format that's 16 MB/s on the wire; in text format it would be 100 MB/s, a six-times difference purely from encoding choice."
>
> "Cardinality is the real driver. Each active series costs two to three kilobytes of memory — the inverted index postings, the series metadata, and the head chunk. Ten million series is roughly 25 GB of RAM, which is the single-node ceiling. So we have to shard by series hash."
>
> "The conclusion I'd draw: the bottleneck is not QPS. It's the cardinality-times-time product — storage and query amplification. Ingest bandwidth is a trivial 16 MB/s; the index memory and a single month-long aggregation are what take the node down."

## 3. 采集层：推送还是拉取（Collection Layer: push vs pull）

先定义 Agent，否则后面全是空中楼阁（define the agent first, or everything downstream is hand-wavy）：

**Agent** = 部署在每台机器上的常驻进程，四个职责：① 发现采集目标（服务发现 / 本地进程 / 静态配置）② 抓取并解析 ③ 本地聚合与缓存（断网不丢）④ 批量上报中心。

### 3.1 pull：怎么工作，代价落在哪（how it works, where the costs land）

中心有个**抓取调度器（scrape scheduler）**：每 15s 从 SD 拉目标列表，对每个目标发 `GET /metrics`（超时 10s），解析后打上外部标签（job / instance / region），并生成 `up` 指标（1 = 成功，0 = 失败）。

| 代价 Cost                         | 细节                                       | 补法 Mitigation                                                      |
| ------------------------------- | ---------------------------------------- | ------------------------------------------------------------------ |
| ① 目标必须可寻址 addressable           | 容器网络、防火墙、NAT 后的目标抓不到——最被诟病的一点            | 把 Agent 放在同网段（K8s 里就是 DaemonSet / sidecar），抓取走本地回环                 |
| ② 短命任务抓不到 short-lived jobs      | 跑 30s 就退出的批处理，一个周期都赶不上                   | Pushgateway（任务结束前推一次，监控端去拉）。它自己三个坑：单点写入、数据永不过期（要设 TTL）、分不清新任务和残留数据 |
| ③ 抓取调度器成瓶颈 scheduler bottleneck | 10 万目标 / 15s = 6667 次 HTTP/s + 解析，单实例不可能 | 分片抓取（每个 Agent 负责一批目标）——"分片"思想第一次出现                                 |
| ④ SD 集成的长期运维成本                  | 要为 K8s / Consul / EC2 / 自研 CMDB 各写适配器    | 接受它，换来全网统一采集配置                                                     |
| ⑤ 不适合事件型指标 event-shaped         | "订单创建"本质是推送语义，用计数器模拟会丢信息                 | 这类指标改走 push，或用 counter + increase()                                |

### 3.2 push：怎么工作，代价落在哪

Agent 在内存里维护指标（计数器累加、直方图分桶），每 10–60s flush 一批。两种传统：**StatsD 式**（UDP 无连接、丢了就丢、极简、Agent 端聚合）和**现代式**（内存聚合 + 批量 HTTP/gRPC + 本地磁盘 WAL 缓存 1–4 小时）。

| 代价 Cost | 细节 | 补法 Mitigation |
|---|---|---|
| ① 没有存活信号（最致命） | 目标死了就没人上报，**分不清"服务挂了"和"这服务本来就没这些指标"** | deadman 心跳告警（3 分钟没收到 agent_heartbeat 就告警）。必要但不充分：它能发现 Agent 死，发现不了"Agent 活着但 exporter 死了" |
| ② 没有背压 no backpressure | 突发流量直冲存储（如主机重启风暴） | Agent 端限流 + 网关按租户令牌桶 + Kafka 缓冲；**队列 lag 是核心告警指标** |
| ③ 配置分散 | 每个 Agent 都要知道自己该报什么、间隔多少 | 中心下发配置，Agent 定期拉配置 |
| ④ 重复与乱序（pull 没有这个问题） | 网络重传产生重复点 | (series, timestamp) 幂等去重 |
| ⑤ 客户端时钟不可信 | pull 由采集端打时间戳（时钟统一）；push 由客户端打，偏斜会污染数据，甚至写入"未来"的点 | 网关校验时间戳偏移，超阈值（约 5 分钟）丢弃并计数 |

> 代价 ⑤ 是深度信号——大多数人根本不会提时钟。

### 3.3 标准答案：分层混合，不是二选一（hybrid by layer, not either/or）

**边缘 pull、骨干 push（Pull at the edge, push on the backbone）。** 这是 Datadog / New Relic / 主流云监控的真实架构：

```
第 1 层（本机 on host）   Agent 用 PULL 抓本机 /metrics 和 exporter
                          → 免费的 up 信号、配置统一、不受 NAT 影响、零网络成本
第 2 层（本机→中心）      Agent 用 PUSH 批量上报到中心
                          → 天然适合跨网 / 边缘 / 多区域；WAL 抗断网
第 3 层（中心 center）    接入网关 → Kafka → TSDB → 对象存储
```

pull 的代价 ①②③（可寻址 / 短命任务 / 调度瓶颈）被"本机 Agent"消解；push 的代价 ①（无存活信号）被 Agent 心跳补上，代价 ②（无背压）被 Agent 端限流 + Kafka 补上。

**产品映射（product mapping，一句话显示你了解工业界）**：

| 系统 System | 模式 Model |
|---|---|
| Prometheus | 纯 pull + Pushgateway 补短命任务 + remote_write 上中心 |
| Datadog | Agent 本机 pull + push 到 SaaS（正是上面这套混合） |
| StatsD / Graphite | 纯 push、UDP、Agent 端聚合 |
| OTel Collector | receiver/exporter 模型，pull / push 原生都支持 |

### 3.4 深水区：聚合该放在哪一层（deep water: where does aggregation belong）

面试官问"10s 间隔太贵，能不能改 60s"时，不要只答"分辨率会降低"。拆成三个可选位置（three candidate placements）：

| 选项 Option | 做法 | 收益 Gain | 代价 Cost | 适用 Fits |
|---|---|---|---|---|
| **A · Agent 端聚合** | 10s → 60s 后上报 | DPS 1M → 166K，成本 ÷6 | **丢失 10s 分辨率且不可回溯**（原始数据从未离开主机） | 跨区域上报、边缘 IoT 等传输成本占主导的场景 |
| **B · 传输层只压缩不降采样** | 保留 10s 点，二进制批量 + snappy | 带宽压到 16 MB/s | 无 | 本方案（传输层） |
| **C · 存储侧双重保留** | 永远写原始点；compaction 时生成 rollup；查询按 step 选粒度 | **可回溯**，策略可独立调整 | 需要 rollup 管道 | 本方案（存储侧） |

**必须说出口的洞见**：聚合时**不要存 avg，要存 max/min/sum/count**。60s 的 max 是"这 60s 内的最大瞬时值"，保留尖峰；avg 会把尖峰抹平。对 P99 延迟、GC 停顿这类指标，**尖峰才是信号，均值是噪音**。

▸ **Say it in English**
> "I wouldn't pick one — I'd layer them. Pull at the edge, push on the backbone. An agent on every host pulls the local metrics endpoint, which gives us a free liveness signal, uniform configuration, and immunity to NAT and firewalls. The agent then pushes batches to the central tier, which is what you want across networks and regions. That's essentially what Datadog does."
>
> "Pull's real costs: targets must be addressable — solved by putting the agent on the same host. Short-lived jobs never get scraped — solved with a push gateway plus a TTL. And the scrape scheduler becomes the bottleneck at 100,000 targets — solved by sharded scraping."
>
> "If you ask me to make 10-second collection cheaper, there are three places I could aggregate. At the agent — irreversible, and only right when transport cost dominates. In transport — no, compression is enough. Or in storage — always keep the raw point, generate rollups during compaction, and let the query pick granularity by step. I'd choose storage, because it's reversible and the retention policy stays tunable."
>
> "And when I aggregate, I store max, min, sum and count — never avg. A 60-second max is the largest instantaneous value in that window and it preserves the spike. The average flattens it. For P99 latency or GC pauses, the spike is the signal."

## 4. 时序数据模型（Time-Series Data Model）

### 4.1 series 的精确定义（definition of a series）

```
http_requests_total{service="api", region="us-east", instance="10.0.0.5", status="200"}
└─── metric name ──┘└──────────────────── labels（维度 dimensions）──────────────┘
```

一个 **series** = metric name + 一组 label 的**确定组合**。两个点属于同一 series 的充要条件：metric name 相同，且**每一个** label 键值对都相同。label 顺序不影响身份——它是集合不是列表（写查询时要记住）。

**三条性质决定了整个存储设计（three properties drive the storage design）**：

| 性质 Property                           | 后果 Consequence                             |
| ------------------------------------- | ------------------------------------------ |
| 标签不可变（labels immutable）               | series 身份稳定 → 标签只需存一次（字典编码），点里只放 series ID |
| 追加型、时间单调（append-only, monotonic time） | 顺序写 → LSM 友好，天然可按时间分块                      |
| 几乎不更新（effectively no updates）         | 可以放弃原地更新能力，换取更高写吞吐                         |

**值得讲的翻车案例：容器重启为什么引爆基数？（why container restarts explode cardinality）**
因为 instance 从 10.0.0.5 变成 10.0.0.6，这就是**两个不同的 series**。旧 series 不会立刻消失（要等陈旧淘汰），于是每次重启都留下一批僵尸 series。K8s 里 pod IP 频繁变化时，基数随重启次数线性增长。解法：用稳定标识（pod name / workload name）作 label，而不是 IP；或给 series 生命周期设上限。

### 4.2 基数：怎么算、为什么它让节点死（cardinality）

```
series 数 = ∏(每个 label 的取值数)     ← 是乘积，不是相加
```

`http_requests_total` 四个 label：instance(5 万) × status(6) × method(4) × endpoint(20) = **2400 万理论组合**。

**必须区分两个数（面试官特别爱追这个 follow-up）**：

| | 定义 Definition | 治理手段 Governance lever |
|---|---|---|
| 理论组合数 theoretical | 各 label 取值数的乘积 | 减少 label 维度（砍掉 endpoint） |
| **实际活跃 series 数 active** | 保留窗口内**真实收到过点**的 distinct 组合数 | 限制高频变化 label 的取值空间（URL 归一化） |

实战要监控的是**活跃 series 增长率**这个指标本身，不是理论乘积。

**内存三段拆解（回答"为什么 1000 万 series 要 25GB"）**：

```
① 倒排索引 inverted index   每个 (label_name, label_value) 一条 postings list（series ID 数组）
                            一个 series 有 k 个 label → 出现在 k 个 postings 里 ≈ 50–100 B
② series 元数据 metadata     label 集合（intern 后的指针）+ 哈希值        ≈ 300–500 B
③ head chunk                最近 2h 的点（720 点，压缩后）                ≈ 1.4 KB
                            ────────────────────────────────────────
                            合计 ≈ 2–3 KB / series → 1000 万 series ≈ 25 GB
```

Prometheus 官方把"单实例几百万 series"定为舒适区；1000 万以上必须分片（sharding）。

**禁忌 label（forbidden labels）**——"你会加什么 tag"这题既是送分也是送命：

| 禁用 Never use | 原因 Why | 替代 Instead |
|---|---|---|
| user_id / session_id | series 数 = 用户数，内存瞬间爆 | 日志 / trace，用 exemplar 关联 |
| request_id | 每请求一个 series，写入放大无上限 | 日志 |
| 原样 url | /user/123/profile 基数爆炸 | 归一化成 /user/{id}/profile |
| timestamp 当 label | 每个点一个新 series | 时间就是时间轴，不是维度 |
| 错误文本 error message | 组合无限 | 错误码 + 日志 |

> 话术：「label 是可检索维度，但每个取值都乘进 series 数。规范上只允许低基数枚举型 label（<100 取值）进指标；高基数的用户/请求维度只能进日志和 trace，用 exemplar 关联。」

### 4.3 为什么关系库是错的工具（why a relational database is the wrong tool）

**候选：MySQL / Postgres**

| 致命问题 Fatal problem | 细节 |
|---|---|
| 写入模式错配 | 时序是追加 + 时间递增；B 树是原地更新页 + 随机 IO。改一个 16 字节的点可能触发 16KB 页写回 + 页分裂 → **写放大 100–1000×**。1M DPS 下就是 16GB/s 的物理写——物理上不可能 |
| 没有列式压缩 | 行存 16 B/点（8B 时间戳 + 8B 值），列式 + delta/XOR 后 1.4 B → **11× 差距**。165TB 与 15TB 的差别，就是"项目能不能做"的差别 |
| 没有聚合下推 | 没有 per-series 预聚合、没有块内增量聚合的概念 |
| 分区运维债务 | 15 个月保留 = 15 个月度分区 + 定期 drop + 索引重建，全是脚本债 |

它**该**用在哪：**元数据、告警规则、租户配置、审计日志**（QPS 低、要事务、要灵活查询）。说出"用在哪"而不是一刀切否定，才像架构师。

**候选：Cassandra / ScyllaDB** —— LSM 写吞吐高、线性扩展、**多区域原生复制**（正好对上本题需求）。但：没有窗口聚合下推（rate / sum over 5m 要另算）；CQL 弱，按 label 反查要手工设计宽表 + 二级索引（高基数下性能极差）；rollup 管道要自己建；LWW 冲突解决依赖时钟精度。

> 话术：「Cassandra 可以当存储层，但要在它上面自建时序索引和 rollup 管道，等于重造半个体量。除非团队已经在跑 Cassandra 且看重它的多区域复制，否则专用 TSDB 是更好的交易。」

**候选：专用 TSDB（purpose-built TSDB）**

| 选项 | 说明 |
|---|---|
| VictoriaMetrics | 单机性能极强（内存与压缩率优于 Prometheus），有集群版 |
| Thanos | Prometheus + 对象存储 + 全局查询层，多区域友好 |
| Cortex / Mimir | 原生分布式：分片写入 + 对象存储 + 全局查询（Grafana 出品） |
| InfluxDB | 原生时序模型，但集群版闭源商业——这是真实选型约束，提出来显专业 |
| TimescaleDB | PG 扩展：SQL 友好、自动分区、连续聚合（内置 rollup），适合 SQL 熟 + 中等规模 |

> 加分表达：「真实项目里我会先评估 VictoriaMetrics / Thanos 是否覆盖需求，把自研留给真正差异化的 10%。但如果面试官要我从零设计，我能把 LSM、列式时间块、倒排索引这三块原理讲透。」——深度和克制两头得分。

▸ **Say it in English**
> "A series is a metric name plus one specific label combination — it's the unit of indexing, writing and querying. Labels have to be immutable, which is why cardinality is a product and not a sum: instance times status times method times endpoint."
>
> "user_id, session_id, request_id and raw URLs never become labels, because their cardinality is unbounded. Those dimensions belong in logs and traces, correlated with exemplars. Only enumerated labels under about a hundred values belong in metrics."
>
> "This is also why container restarts explode cardinality — the instance label changes from one IP to another, which creates a brand-new series while the old one lingers until staleness eviction."

## 5. 写入路径（Write Path）

```
Agent（本机 pull + 本地聚合 + WAL 缓存）
    │  gRPC + protobuf + snappy，每批 1,000–10,000 点
    ▼
接入网关 ingest gateway（无状态：认证 / 租户隔离 / 限流 / 时间戳对齐 / label 白名单）
    ▼
Kafka（按 hash(series) 分区——保证同 series 有序）
    ├───────────────┬───────────────────┐
    ▼               ▼                   ▼
TSDB 写入器    告警评估器           跨区复制消费者
    ▼
内存 chunk → WAL → 2h block → compaction → 冷对象存储
                                    ↑
                        【rollup 降采样在这里生成 — Day 3】
```

### 5.1 第 1 跳：Agent → 网关（hop 1）

| 决策 Decision | 选择 Choice | 理由 Reason |
|---|---|---|
| 协议 | gRPC（优于 HTTP/1.1） | HTTP/2 多路复用，适合高频小批量且不会连接数爆炸 |
| 批量大小 | 1,000–10,000 点 | 太小 → 每请求开销占比高；太大 → 延迟高、重传代价大 |
| 压缩 | snappy（优于 gzip） | 压缩率略差但 CPU 便宜得多——Agent 跑在**每台**机器上，CPU 是稀缺资源 |
| 认证 | mTLS 或 per-agent bearer token | 可按 Agent 吊销 |
| 幂等键 | (series, timestamp) | 让重试安全 |

网关职责（每一条都是一个"边界处理"得分点）：认证与租户隔离（多租户下不做这个，租户能看别人数据）；限流（**按租户**令牌桶，防单个坏 Agent 拖垮全局）；时间戳对齐（floor 到采集间隔；不齐会把同 series 碎成多段 chunk，压缩率腰斩）；label 白名单校验（未注册的 label 名直接丢弃并回报）；URL 路径归一化；拒绝超未来的时间戳（数据污染 + 攻击面）。

无状态设计，所以 DPS 增长只需加机器——没有状态迁移成本。

### 5.2 第 2 跳：Kafka 的四个理由（hop 2）

1. **削峰 peak shaving** —— Agent 批量上报有突刺，尤其 WAL 在断网恢复后集中补传。
2. **解耦 decoupling** —— 写入器、告警评估器、跨区复制器互不阻塞；**告警不能在 TSDB 维护时停摆**。
3. **缓冲 buffering** —— TSDB 扩容/维护期间数据不丢（保留数小时到一天）。
4. **可重放 replayability** —— 修完 bug 可重放历史数据修复写错的数据。

分区策略：`hash(series_id) % partitions`。**同一个 series 的所有点必须落同一分区**，否则分区之间无法保证顺序，而 TSDB 的 chunk 假设时间递增。乱序到达会导致要么拒绝、要么不断重写 chunk。

分区数：每分区约 5–10 MB/s → 16MB/s 需要 3–5 分区，但要按三年后规模规划（**分区数只能增不能减，改分区数会破坏 key→分区映射**）。

坑：单个超高基数 metric（某服务 500 万 series）造成分区倾斜——一个分区烤糊、其他空闲。解法：这类 metric 单独 topic，或对分区键二次散列。

### 5.3 第 3 跳：TSDB 写入器——内存与磁盘两阶段（hop 3）

**内存阶段**
- 点先写 **WAL**（顺序追加）再进 memtable。
- 为什么 WAL 必须在前面：崩溃后可重放恢复约 2h 的缓冲数据，否则每次重启丢 2h。
- 每个 series 一个 head chunk（约 120 点或 2h 窗口）；满了 → 压缩 → 落成持久 block。

**磁盘阶段**
- block 内：按 series 分组、series 内按时间排序 → **物理连续**。
- block 元数据：min/max 时间、series 列表、chunk 偏移 → 这是查询能**跳过无关 block** 的依据（§6.3）。
- 后台 compaction 把小 block 合成大 block（2h → 6h → 1d → 1w），并顺带算出 rollup。
- 分层存储：近 15 天在本地 NVMe，更早在对象存储（按需拉取 + 本地缓存）。

### 5.4 为什么是 LSM 不是 B 树（why LSM, with numbers）

**B 树的问题**：页 16KB，更新 = 读页 → 改 → 写回 → 可能分裂。改一个 16 字节的点可能付出 16KB 写回 → **写放大 100–1000×**。1M DPS 下是 16GB/s，直接出局。

**LSM 的优势**：写入只做两件事——顺序追加 WAL、更新内存 memtable（无随机 IO）。memtable 满 → 冻结 → 刷成有序 SSTable。写放大主要来自 compaction（多路归并），约 **10–30×**，且全在后台异步、不挡写路径。

**物理上限对比**（这个对比最能说明问题）：顺序写单盘 500MB/s–3GB/s；随机写只有 100–400MB/s（几万次 4KB IOPS）。裸 IO 差 5–10 倍，再乘 10–100 倍写放大——就是"能做"和"不能做"的区别。

**LSM 的代价（主动说，显客观）**：读要查多层（用布隆过滤器 + 稀疏索引缓解）；空间放大（同一份数据在多层共存，靠 compaction 收敛）；compaction 抢 IO 和 CPU（要限速、要和查询错峰）。

**时序场景的额外加成（为什么 TSDB 优于通用 LSM）**：因为数据只追加、时间递增，可以按时间切分 block，**已封存的 block 只读**。只读 block 可以放对象存储，甚至可以只存降采样版本。通用 KV 做不到这个假设。

### 5.5 压缩：1.4 字节/点是怎么来的（where 1.4 bytes/point comes from）

| 内容 Component | 编码 Encoding | 效果 Result |
|---|---|---|
| 时间戳 | 等间隔 → delta；二阶差分（delta-of-delta）为 0 → 1 bit 表示"和上次一样"；抖动用变长编码 | 约 **1.06 bit/点** ≈ 0.13 B（Gorilla）——比原始 8B 小 60 倍 |
| 数值（浮点） | 与前值 XOR，存"前导零数 + 有效位数 + 有效位"。模式重复时只存有效位 | 约 **1.37 B/点**（Gorilla） |
| 标签 | block 内字典编码，每个 distinct 值只存一次；点里带 4–8 B series ID | 标签不在点里重复 |
| **合计** | | **约 12×：16 B → 1.4 B/点** |

报出"Gorilla 论文 1.37 字节/点"这个数字，会立刻把答案从"背架构"抬到"懂原理"。

### 5.6 乱序与迟到数据（out-of-order and late data）

来源：WAL 断网补传、网络重传、跨区延迟、客户端时钟偏斜。
本质矛盾：chunk 假设时间单调递增；迟到点落在已封存 chunk 里，就得重写整个 chunk。

| 情况 Case | 处理 Handling |
|---|---|
| 在新鲜窗口内（仍在内存 head chunk，约近 2h） | 直接插入 + 内存重排——便宜，接受 |
| 超出内存但落在磁盘 block 内 | 标记该 block 需重写，在 compaction 时补进去——昂贵，只对小比例开放 |
| 超出容忍窗口（如 >5 分钟） | **丢弃 + 计数**（out_of_order_dropped） |
| 时间戳在未来 | 直接拒绝（数据污染 + 攻击面） |

> 话术：「我不会为 0.1% 的乱序点牺牲整条写入路径的吞吐。**但丢点必须可见**——要有指标和告警。静默的数据缺失比报错危险得多。」

**配套机制 · 陈旧标记 staleness marking**（最常被漏掉）：series 超过 N 个采集周期没有新点 → 标记 stale → 查询返回"无数据"而不是最后一个值。没有它，一个死掉的服务会永远显示最后的健康值，**告警永不触发**。

### 5.7 幂等与去重（idempotency and deduplication）

重复的三个来源：Agent 重试、Kafka 至少一次投递、跨区复制。
去重粒度：`(series_id, timestamp)` 相同 → last-write-wins。
为什么不做全局去重：要维护"所有近期点的索引"，内存成本与点数同阶——不可行。分片内去重就够，因为**一个 series 永远在一个分片里**（按 series 分片的第二个好处）。跨区：用 `(region, series)` 命名空间隔离，合并时区分而不是去重。

▸ **Say it in English**
> "Time-series writes are append-only, monotonic in time, and effectively never updated. That's the worst possible workload for a B-tree — in-place page updates mean random IO and 100 to 1000 times write amplification, and at a million points per second that's 16 GB/s of physical writes. An LSM only appends to a WAL and updates a memtable, so compaction happens in the background. And because merging makes the points of one series physically contiguous, columnar compression becomes possible."
>
> "Delta-of-delta on timestamps gets us about one bit per point, and XOR on the values about 1.37 bytes per point — that's the Gorilla paper's number — for roughly twelve times overall. That's how 500 terabytes of raw points becomes 44."
>
> "I won't sacrifice the throughput of the entire write path for 0.1% of out-of-order points. Inside the freshness window I insert them, beyond the tolerance window I drop them and count the drops. But drops must be visible, because silent data loss is far more dangerous than an error."

## 6. 查询语言与查询路径（Query Language and Query Path）

### 6.1 监控查询的通用形态（the general shape）

在时间窗 T 内用 label matcher 选出 series 集合 S → 施加窗口函数 f → 再按 label 子集 g 跨 series 聚合。三个特性让 SQL 不合适：

1. **时间桶对齐 time-bucket alignment** —— 不同 step 要重新分桶，SQL 窗口函数的对齐规则繁琐且没有下推空间。
2. **增量计算下推 incremental pushdown** —— TSDB 可在 block 层预存部分聚合（块内 sum），跨 block 只需相加。
3. **稀疏时间轴 sparse time axis** —— 不是每个 series 每个时刻都有点（抓取失败、series 生灭），SQL 的 join 语义处理这种稀疏代价极高。

### 6.2 一条真实告警规则拆解（a real alert rule, decomposed）

```
rate(http_requests_total{status=~"5..", job="api"}[5m])
 │                             └── label matcher：倒排索引查找 → series 集合
 │    └─ metric name
 │                                             └─ [5m]：取窗口内的点
 └─ rate()：窗口函数，计数器 → 每秒速率
            （还处理 counter 重置：用当前值代替差值）
/ rate(http_requests_total{job="api"}[5m])
 └─ 两个向量逐点相除（时间对齐由 DSL 保证）
> 0.01
 └─ 阈值比较 → 布尔向量 → 告警规则输入
```

用 SQL 表达要三层子查询 + 手工对齐时间桶，且优化器什么都下推不了。**这就是"为什么必须用 DSL"的完整论证——不是"更方便"。**

### 6.3 查询路径逐跳（query path, hop by hop）

1. 解析 PromQL → AST（校验 + 提取 series 选择器）。
2. **时间裁剪 time pruning** —— block 元数据有 min/max 时间，范围外的 block 全跳过。查 30 天绝不碰 3 年前的 block。
3. **Series 预筛 pre-filtering（收益最大）** —— label matcher 转成倒排索引操作：
   `status="200"` → 取其 postings list；`status=~"5.."` → 多个 postings 求并集；多条件 → 求交，**从最小的 postings 开始**以减少中间结果。
   → 通常把 1000 万 series 缩到几百个：**砍掉 99.99% 的工作量**。
4. 点读取 + 窗口函数：按 series 顺序读（物理连续），块内增量聚合。
5. 跨 series 聚合：按 `by (label)` 分组。
   **陷阱**：avg 不能直接跨 series 平均——要算 sum / count 再除，因为各 series 点数可能不同（有的实例丢过点）。
6. 结果组装 + 缓存：缓存 key = 归一化 AST + 对齐后的时间范围。

### 6.4 读放大的精确量化（read amplification, quantified）

看板场景：8 个 panel，30 秒刷新。

```
请求量 request rate  8 / 30s = 0.27 QPS                     ← 看起来完全不是问题
单 panel 扫描量      1,000 series × (30 天 / 15s step) = 1.7 亿点
8 个 panel           13.8 亿点 / 次刷新
读带宽               13.8亿 × 1.4 B = 1.9 GB / 30s ≈ 65 MB/s（每个看板用户！）
100 个工程师         6.5 GB/s → 存储层直接崩
```

这就是"读 QPS 只有 0.27、读放大却有 10^4"的精确含义，也是为什么读写比不能只看 QPS。

**解法按性价比排序（present in this order）**：

| 手段 Remedy | 效果 Effect |
|---|---|
| ① 降采样（30 天查询读 1 小时 rollup） | 点数 1.7 亿 → 720 × 1,000 = 72 万，**降 240 倍** |
| ② 查询下推到 rollup 层（预聚合数据放便宜存储） | 减少回源 |
| ③ 结果缓存 + 看板级共享缓存 | 多用户共享同一结果 |
| ④ 查询并发限制 + 每租户配额 | 限制单点爆炸半径 |
| ⑤ 自适应 step（按范围选粒度） | 用户无感 |

> **洞见句（背下来）**：降采样主要不是为了省存储（只省约 1/3），而是为了省**查询放大（240 倍）**。这是"知道要降采样"和"知道为什么"的分界。

### 6.5 生产必备的硬限制（hard limits，很多人漏）

- `max_samples` / `max_series`：单查询最多扫多少点、返回多少 series；超限直接失败并提示缩小范围。没有它，一个 `sum by (instance)` 全量查询就能杀死集群。
- 查询超时 + 取消传播：HTTP 取消必须逐层 cascade，否则后台 goroutine 泄漏。
- 大查询转异步：超过阈值（如 1 亿点）转后台 job，结果落对象存储，客户端轮询。
- 优先级隔离：**告警查询优先于看板查询**——告警不能因为看板抢资源而延迟。这是业务要求，不是技术偏好。

▸ **Say it in English**
> "The read side has a counter-intuitive shape. Eight dashboard panels refreshing every 30 seconds is 0.27 QPS — negligible. But each panel scans a thousand series over 30 days, which is 1.7 billion points. Across eight panels that's 1.9 GB per refresh, about 65 MB/s per user. A hundred engineers with dashboards open is 6.5 GB/s and the storage layer is gone."
>
> "So downsampling isn't mainly about saving storage — that's only a third. It's about saving query amplification, and it saves 240 times. One-hour rollups turn 1.7 billion points into 720 thousand."

## 7. API 设计（API Design）

| 方法 Method | 路径 Path | 用途 Purpose | 设计要点 Design point |
|---|---|---|---|
| POST | `/api/v1/write` | Agent 批量写入 | protobuf `{ timeseries: [{ labels, samples: [{ts, value}] }] }` + snappy。响应是**部分成功 partial success**：`{ accepted, dropped, errors: [{ label, reason }] }`。幂等键 `(series, ts)`。允许服务端时间戳但要有偏斜上限 |
| POST | `/api/v1/query` | 瞬时查询 instant | `expr` + `time` → instant vector；用于告警评估和单点取值 |
| POST | `/api/v1/query_range` | 范围查询（看板主力） | `start`/`end`/`step` → matrix。**step 决定读哪一级 rollup**；要定义 step 小于数据间隔时的语义 |
| GET | `/api/v1/series` | 元数据发现 | `match[]` + `limit`——**limit 必须有**：宽正则会返回 1000 万 series，直接把集群烤化 |
| GET | `/api/v1/labels`、`/api/v1/label/{name}/values` | Grafana 下拉补全 | 必须带结果上限 |
| POST | `/api/v1/rules` | 告警规则 CRUD | `name, expr, for, labels, annotations, group`——评估语义 Day 3 讲 |

**追问预案 · "写接口为什么要返回部分成功？"** 1M DPS 下整批重传代价太高（一批 10000 点里坏 1 个）。返回逐条原因让 Agent 自己决定重试粒度，天然实现背压。

▸ **Say it in English**
> "The write endpoint returns partial success, not all-or-nothing. At a million points per second, retrying a whole batch because one point was rejected is too expensive. Returning per-item reasons lets the agent choose its own retry granularity, and that becomes natural backpressure."

## 8. 失败模式与降级（Failure Modes and Degradation）

每条按 **影响 / 降级 / 恢复（impact / degradation / recovery）** 讲：

| 失败 Failure | 影响 Impact | 降级 Degradation | 恢复 Recovery |
|---|---|---|---|
| TSDB 写入跟不上 | 积压增长，看板数据越来越旧（是"变慢"不是"挂"，更难发现） | Kafka 就是缓冲 → **队列 lag 是核心告警指标**；写入器按分区无损扩 | 扩容后按 lag 追平 |
| 网关 / 网络中断 | 边缘数据丢失 | Agent 本地 WAL 缓存 1–4h；满时按优先级丢（先丢 debug 级，保业务关键） | 恢复后按序补传——注意会形成写入尖峰，Kafka 要能承接 |
| 索引 / 元数据服务挂 | 查询无法定位 series | 读路径退化为缓存 label→series_id 映射；写入继续（新 series 进 pending 区） | 从 block 元数据重建索引，不需要原始数据 |
| 看板把集群打爆 | 告警也失效（业务影响最大） | 查询并发限流 + 租户配额 + 大查询降级到 rollup + 告警优先级隔离 | — |
| Kafka 分区热点 | 少数 series 拖慢全局，其他分区空闲 | 哈希加盐；超高基数 metric 单独 topic | 监控分区吞吐方差 |
| 时钟偏斜 | 点写入错误时间，chunk 顺序与聚合被污染 | 拒绝超偏斜阈值的点并计数；查询时按区域容忍（Day 3 多区域话题） | — |

## 9. 演进路线（Evolution Roadmap，每版都有升级信号）

| 版本 Version | 范围 Scope | 升级触发信号 Trigger |
|---|---|---|
| v0 | 数十台主机：单机 Prometheus + 本地盘 + Alertmanager + Grafana。**主动说"v1 我不做多区域、不做降采样，因为不需要"** | 活跃 series 逼近 100 万；索引内存 >70%；查询 P99 上升 |
| v1 | 数千台主机：结构不变，运维加固 | 写入 lag 持续 >0；存储成本增速快于业务 |
| v2 | 5 万台 / 1M DPS：接入网关 + Kafka + 分片 TSDB（hash(tenant, series)）+ 对象存储 + rollup 降采样 + 查询限流 | 跨区带宽成为主成本项；跨区查询延迟不可接受 |
| v3 | 多区域：区域自治（本地写/查/告警）+ 跨区 rollup 同步 + 全局查询层 | 单个租户的基数增长影响全局 |
| v4 | 治理：series 配额 + label 白名单 + 每租户成本归属 + SLO 看板 | — |

用"信号驱动演进"而不是"单机→分布式→多区域"的空话，展示的是运维视角。

## 10. Part 1 自测题（Self-Test）

中英双问，**用英文回答**（answer in English, out loud, no notes）：

1. 面经 #3 的 "multi-region" 指采集端在多区域、查询端在多区域、还是要全球视图？三种理解分别改设计的哪一块？哪一个属于 v1？
   *In interview #3, does "multi-region" mean collectors in multiple regions, queriers in multiple regions, or a global view? Which part of the design does each reading change, and which one is v1?*
2. 采集间隔从 10s 改到 60s：DPS、线带宽、年存储各降多少？怎么论证这个取舍可接受？
   *Going from 10s to 60s intervals: how much do DPS, wire bandwidth and annual storage drop? Make the case that the trade-off is acceptable.*
3. 为什么 pull 是 Prometheus 的默认？给出 pull 的 3 个真实代价 + 各自的补法——再指出哪一个代价**没有完全的补法**。
   *Why is pull Prometheus's default? Give three real costs of pull plus your mitigation for each — and name the one cost no mitigation fully removes.*
4. 把 M1 Part 1 压成 5 句话。
   *Compress all of M1 Part 1 into five sentences.*

### 六句必背（the six lines worth memorizing）

1. 瓶颈不是 QPS，而是「**基数 × 时间**」的存储与查询放大。
   *"The bottleneck is not QPS — it's the **cardinality × time** product for storage and query amplification."*
2. **边缘 pull、骨干 push**——不是二选一。
   *"**Pull at the edge, push on the backbone** — it's not either/or."*
3. 聚合时存 **max/min/sum/count，不要存 avg**——尖峰才是信号。
   *"When aggregating, store **max/min/sum/count, not avg** — the spike is the signal."*
4. 丢点**必须可见**——静默丢失比报错危险。
   *"Dropped points **must be visible** — silent loss is more dangerous than an error."*
5. 降采样主要不是省存储（只省 1/3），而是省**查询放大（240 倍）**。
   *"Downsampling is not mainly about saving storage (only ~1/3) — it saves **query amplification (240×)**."*
6. 没有**陈旧标记**，死掉的服务会一直显示最后的健康值，告警永不触发。
   *"Without **staleness handling**, a dead service keeps reporting its last healthy value and the alert never fires."*

---

## 术语对照表（Glossary）

| 中文 | English | 一句话 |
|---|---|---|
| 数据点/秒 | DPS (data points per second) | 本类系统的容量单位，不是 QPS |
| 时间序列 | series / time series | metric name + 一组 label 的确定组合 |
| 标签 / 维度 | label / dimension | 可检索维度，取值数直接乘进基数 |
| 基数 | cardinality | series 数，内存杀手 |
| 基数爆炸 | cardinality explosion | 高基数 label（user_id/URL）导致索引内存失控 |
| 倒排索引 | inverted index | (label,value) → series ID 列表，查询预筛的基础 |
| 拉取 / 推送 | pull / push | 采集模型；正解是边缘 pull + 骨干 push |
| 抓取 | scrape | pull 模型的动作 |
| 服务发现 | service discovery (SD) | pull 模型的前置依赖 |
| 短命任务 | short-lived job | pull 的盲区，需 Pushgateway 补 |
| 降采样 / 预聚合 | downsampling / rollup | 生成粗粒度聚合，主要省查询放大 |
| 保留策略 | retention policy | 分层：15 天原始 + 1 年分钟 + 3 年小时 |
| 压缩比 | compression ratio | 时序列式约 12×，1.4 B/点 |
| 时间戳二阶差分 | delta-of-delta | 时间戳编码，约 1.06 bit/点 |
| 写放大 | write amplification | B 树 100–1000×，LSM 10–30× |
| 预写日志 | WAL (write-ahead log) | 崩溃恢复，防丢 2h 内存数据 |
| 日志结构合并树 | LSM tree | 顺序写 + 后台 compaction，时序写入正解 |
| 压实 / 合并 | compaction | 小块合并成大块，顺便生成 rollup |
| 块 | block | 时间分片的物理存储单位，元数据带 min/max 时间 |
| 乱序 | out-of-order | 迟到点，按窗口分级处理，超出则丢弃并计数 |
| 陈旧标记 | staleness | 无新点即返回"无数据"，防僵尸值 |
| 僵尸数据 | zombie / stale value | 死了的服务仍显示最后健康值 |
| 背压 | backpressure | pull 天然有，push 需要补 |
| 削峰 | peak shaving | 队列的核心价值之一 |
| 队列堆积 | consumer lag | Kafka 的第一告警指标 |
| 读放大 | read amplification | 读 QPS 小但扫描量巨大（10^4） |
| 查询下推 | query pushdown | 把聚合推到存储层/rollup 层 |
| 热点 | hotspot | 明星用户 / 超高基数 metric |
| 时钟偏斜 | clock skew | push 模型的隐藏风险 |
| 幂等 | idempotency | (series, ts) 去重 |
| 分片 | sharding | 按 hash(series) 切分，同 series 同分片 |
| 无状态 | stateless | 网关可水平扩的前提 |
| 对象存储 | object storage | 冷数据唯一可行选择 |
| 租户隔离 | tenant isolation | 多租户系统的网关职责 |
| 白名单 | allowlist | label 名强制注册 |
| 配额 | quota | 每租户 series / 查询量上限 |
| 部分成功 | partial success | 写接口返回 accepted/dropped |
| 窗口函数 | window function | rate / sum over 5m |
| 时间桶对齐 | time-bucket alignment | step 决定分桶 |
| 自适应步长 | adaptive step | 按范围自动选粒度 |
| 降级 | degradation | 先保告警，再看板 |

---

# Part 2 · 深水区（Deep Water, Day 3）

- [ ] 降采样与保留策略（多大窗口留多久；多级 rollup 设计与查询时自动选择）
  *Downsampling & retention (how long to keep which granularity; multi-tier rollups and automatic selection at query time)*
- [ ] 多区域聚合（面经 #3 的核心：本地自治 + 跨区 rollup + 全局查询合并 + 时区/时钟偏斜）
  *Multi-region aggregation (the crux of interview #3: local autonomy + cross-region rollups + global query merge + time zones / clock skew)*
- [ ] 告警评估窗口（`for` 语义、抖动抑制、评估与写入解耦、告警风暴分组）
  *Alert evaluation windows (`for` semantics, jitter damping, decoupling evaluation from ingest, alert-storm grouping)*
- [ ] 基数治理（label 白名单、series 配额、超限降级、活跃 series 监控）
  *Cardinality governance (label allowlists, per-series quotas, graceful degradation on breach, active-series monitoring)*
