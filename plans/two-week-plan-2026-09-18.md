# 两周面试冲刺计划（2026-09-18 → 2026-10-01）

> 来源面经：https://docs.google.com/document/d/1Nm7YgNjKC2cfH4OF7QX5Y7T-shspyIwcoR9ZScSINcU/edit
> 题号解码明细：`plans/mianjing-question-map.md`
> 覆盖：面经 Coding 32 条（去重后 24 个可执行项）+ Design 17 条（归并为 10 个母题）
> 强度：工作日 3h（2h coding + 1h design），周末 5h
> 现状基线：Blind 75 完成 22/75，图/链表/树/滑窗/股票 DP 已成体系（见 `_review-checklist.md`）

## 0. 每日固定节奏

| 时段 | 内容 | 时长 |
|---|---|---|
| Block A | 当天第 1 题：**先限时 25min 独立写**，超时也停手，再看解析，最后**合上解析重写一遍** | 60–75min |
| Block B | 当天第 2 题（第 3 题如果是 easy 就一起塞这里） | 45–60min |
| Block C | 热手复刷：从 `_review-checklist.md` 当日轮换组里挑 1 组，只写关键函数/口述 | 20min |
| Block D | System Design 专题：按母题产出 `system-design/{theme}.md` | 60–75min |
| Block E | 收尾：更新笔记 + 勾选 `_review-checklist.md` + 记录今日卡点 | 15min |

**硬性规则**
1. 每道新题完成后写笔记到 `leetcode/{topic}/{题号}-{英文名}.md`（YAML frontmatter），做完同步 `_index.md` 计数与 `knowledge/blind-75-overview.md` 的 `[x]`。
2. 每题都要能在**不看代码**的情况下 60 秒口述：思路 → 复杂度 → 边界 → 一个优化方向。
3. 面经题一律按**变种**准备，不是按原题准备。下面每道题后面都写了「面试官会追问什么」。
4. 卡住超过 30min 的题当天必须留档到 `_review-checklist.md` 的重点坑区，Day 13 集中收割。

## 1. 优先级总表

### Tier S — 必须手写 + 口述零失误（9 项）

| 题目 | 面经来源 | 核心考点 | 状态 |
|---|---|---|---|
| [LC 934 Shortest Bridge](https://leetcode.com/problems/shortest-bridge/) | 5, 13–17（出现 6 次） | DFS 标岛（-1/-2 原地标记）+ 多源 BFS 扩水，step 计数 | [ ] |
| [LC 347 Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | 25 | 堆 vs 桶 vs quickselect；**为什么变种里只能 heap** | [ ] |
| [LC 23 Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | 21 | 最小堆 vs 分治；+ 外部归并排序追问 | [ ] |
| [LC 146 LRU Cache](https://leetcode.com/problems/lru-cache/) | 27 | HashMap + 双向链表；哨兵 head/tail；并发追问 | [ ] |
| [LC 297 Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | 28 | 遍历序一致 + `#` 占位；前序/BFS 两版 | [ ] |
| [LC 1631 Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) | 8, 22 | 最小化路径最大边：Dijkstra / 二分+BFS / 并查集排序边（三解都要会） | [ ] |
| [LC 68 Text Justification](https://leetcode.com/problems/text-justification/) | 11 | 字符串模拟，左对齐/右对齐/最后一行三个分支 | [ ] |
| [LC 49 Group Anagrams + add/remove/largestGroup 变种](https://leetcode.com/problems/group-anagrams/) | 4 | write-optimized vs read-optimized 的取舍（本plan最重要的一问） | [ ] |
| [LC 210 Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | 3 | Kahn 拓扑排序 + 邻接表方向反转的空间优化争论 | [ ] |

### Tier A — 高频，必须能一次写对（10 项）

| 题目 | 面经来源 | 核心考点 | 状态 |
|---|---|---|---|
| [LC 208 Implement Trie](https://leetcode.com/problems/implement-trie-prefix-tree/) | 2 | 字典树 add/search/startsWith；dict of dict 版 | [ ] |
| [LC 323 Number of Connected Components](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | 6 | Union-Find（含路径压缩+按秩合并）优先 | [ ] |
| [LC 270 Closest BST Value](https://leetcode.com/problems/closest-binary-search-tree-value/) + LC 530 + 普通二叉树版 | 7, 1 | BST 二分下降 O(h) vs 普通树 O(n) DFS | [ ] |
| [LC 743 Network Delay Time](https://leetcode.com/problems/network-delay-time/) | 18 | Dijkstra 手写堆版；无向/有向权重图 | [ ] |
| [LC 1062](https://leetcode.com/problems/longest-repeating-substring/) / [LC 1044](https://leetcode.com/problems/longest-duplicate-substring/) Longest Repeating Substring | 19 | 二分答案 + rolling hash 增量计算 | [ ] |
| [LC 408 Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) | 20 | 双指针；跳过 0 开头的数字 | [ ] |
| [LC 54 Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) + 链表输入变种 | 23 | 边界收缩四指针；链表节点按螺旋填入 n×m 矩阵 | [ ] |
| [LC 638 Shopping Offers](https://leetcode.com/problems/shopping-offers/) | 26 | 记忆化 DFS / 完全背包状态压缩 | [ ] |
| [LC 703 Kth Largest in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) + 面经比赛变种 | 10 | 固定大小 k 的小顶堆；答案是每轮第 k 大的最大值 | [ ] |
| 多关键字排序题（参考 [LC 2512](https://leetcode.com/problems/reward-top-k-students/)） | 12 | comparator 写法、稳定性、`sorted(key=lambda)` 元组技巧 | [ ] |

### Tier B — OOD / 并发 / 待确认（4 项）

| 题目 | 面经来源 | 核心考点 | 状态 |
|---|---|---|---|
| Implement a Circuit Breaker | 24 | closed/open/half-open 状态机、滑动窗口失败率、超时、线程安全 | [ ] |
| Job Runner OOD | 30 | 线程池 + 并发上限、heartbeat、STDOUT/STDERR 分流落库、类图 | [ ] |
| Library 借阅管理 OOD | 31 | borrow/return/listBooks + User/Book 类设计 + 单元测试 | [ ] |
| LC 2327（待核对） | 9 | 先看题干确认，若不是该题则跳过换 934/1631 加强 | [ ] |

### Tier C — 顺手复刷（已掌握，只为了热手）

LC 200 Number of Islands、LC 207 Course Schedule、LC 133 Clone Graph、LC 215 Kth Largest、LC 322/518 背包、LC 1334 Floyd。

## 2. 十四天日程

### Week 1 — 高优先补齐

**Day 1 · 9/18 周五 · 网格图与答题框架**
- Coding：[934 Shortest Bridge] + [323 Connected Components] + 复刷 LC 200（限时 15min 手写）
- 追问预演：934 为什么不能直接用 BFS 从两个岛同时扩（可以，但要讲清多源 BFS 与 step 计数）；323 Union-Find 的路径压缩复杂度
- Design：**答题框架**——写 `system-design/framework.md`：需求澄清 5 问 → 容量估算模板（QPS/存储/带宽）→ 高层组件 → 深挖 → 失败模式。用一道熟悉的题（News Feed）跑通框架
- 产出：`leetcode/graph/0934-shortest-bridge.md`、`leetcode/graph/0323-number-of-connected-components.md`、`system-design/framework.md`

**Day 2 · 9/19 周六 · 堆与 Top K**
- Coding：[347 Top K Frequent] + [23 Merge k Sorted Lists]（+ 外部排序追问口述） + [703 + 面经比赛变种]
- 追问预演：347 的「heap 与 quickselect 各自何时退化」；23 的「链表超过内存怎么办」→ 外部归并排序
- Design：**M1 Metrics Part 1**（面经 3、15）——`system-design/metrics-monitoring.md`：采集（Agent push/pull）、时序数据模型、写入路径、查询语言
- 产出：`leetcode/heap/0347-*.md`、`leetcode/heap/0023-*.md`、`leetcode/heap/0703-*.md`、`system-design/metrics-monitoring.md`

**Day 3 · 9/20 周日 · 设计数据结构**
- Coding：[146 LRU Cache] + [208 Implement Trie] + [49 变种 add/remove/largestGroup]
- 追问预演：LRU 的线程安全版（锁粒度 / ConcurrentHashMap + 分段）；49 变种的 read vs write 权衡（**指标：读写比、SLA、组数量级**）；HackerRank 无 `sortedcontainers` → 手写堆/桶
- Design：**M1 Metrics Part 2**——降采样与保留策略、多区域聚合（面经 3 的 multi-region）、告警评估窗口、基数爆炸
- 产出：`leetcode/design/0146-*.md`、`leetcode/trie/0208-*.md`、`leetcode/hash-table/0049-*.md`

**Day 4 · 9/21 周一 · 字符串与哈希**
- Coding：[68 Text Justification] + [1062 / 1044 Longest Repeating Substring] + [408 Valid Word Abbreviation]
- 追问预演：68 的边界（单个超长单词、最后一行左对齐、空格分配余数）；1044 的 rolling hash 溢出与冲突处理
- Design：**M2 Notification**（面经 10、13）——`system-design/notification-system.md`：扇出、模板、去重、重试与死信、投递状态机、限流、价格变动触发器（面经 13 的 pricing 变体）
- 产出：`leetcode/string/0068-*.md`、`leetcode/binary-search/1062-*.md`、`leetcode/string/0408-*.md`、`system-design/notification-system.md`

**Day 5 · 9/22 周二 · 图与最短路**
- Coding：[210 Course Schedule II] + [1631 Path With Minimum Effort] + [743 Network Delay Time]
- 追问预演：210 的邻接表方向反转（面经 3 的核心争论，**必须准备一段自圆其说的回答**）；1631 三种解法的时间/空间对比
- Design：**M3 Feed / UGC**（面经 2、14）——`system-design/feed-and-review.md`：推拉模式与扇出写放大、Review Service 的聚合评分与一致性、反作弊
- 产出：`leetcode/graph/0210-*.md`、`leetcode/graph/1631-*.md`、`leetcode/graph/0743-*.md`、`system-design/feed-and-review.md`

**Day 6 · 9/23 周三 · 树与矩阵**
- Coding：[297 Serialize/Deserialize] + [270 Closest BST Value（含 530 与普通二叉树版）] + [54 Spiral Matrix + 链表变种]
- 追问预演：297 为什么必须保留空节点；270 的 BST 二分下降与 follow-up（272：找 k 个最近值，双栈/中序队列）
- Design：**M4 Search**（面经 11）——`system-design/search-system.md`：倒排索引、分词、分片、相关性排序、NRT 增量索引、深翻页
- 产出：`leetcode/tree/0297-*.md`、`leetcode/tree/0270-*.md`、`leetcode/array/0054-*.md`、`system-design/search-system.md`

**Day 7 · 9/24 周四 · 阶段模拟 + Leaderboard**
- Coding：阶段模拟 **45min × 2 题**，从 Day1–6 中随机抽（建议盲抽：934 + 347，或 1631 + 146），全程计时、不查资料，结束后写复盘
- 补漏：Day1–6 里任何未写完/未口述顺的题重做
- Design：**M5 Leaderboard**（面经 12）——`system-design/realtime-leaderboard.md`：**跳表（Redis ZSet）深挖**、10M DAU 的写合并、分片与榜单合并、快照重算、作弊检测
- 产出：模拟复盘写入 `_review-checklist.md`，`system-design/realtime-leaderboard.md`

### Week 2 — 补缺 + 全真

**Day 8 · 9/25 周五 · DP 与交易系统**
- Coding：[638 Shopping Offers] + 复刷 [322 Coin Change]/[518 Coin Change II] 背包模板 + [2327（待核对，不是则换 934 加强版）]
- 追问预演：638 的记忆化 key 设计（tuple 状态）与剪枝；背包「恰好装满 vs 至多」的初始化差异
- Design：**M9 Booking & Inventory**（面经 9、16）——`system-design/booking-and-inventory.md`：防超卖（乐观锁/分布式锁/预扣减）、座位锁定 TTL、支付超时回滚、热点库存分桶
- 产出：`leetcode/dynamic-programming/0638-*.md`、`system-design/booking-and-inventory.md`

**Day 9 · 9/26 周六 · OOD 与并发（面经最容易翻车的一块）**
- Coding：Circuit Breaker（面经 24）+ Job Runner OOD（面经 30）+ Library OOD（面经 31）
- 要点：按面经给的 `JobQueue`/`SystemCommand` 接口反推类图（JobExecutor、ThreadPool、Semaphore 限流、HeartbeatMonitor、LogWriter），写清每个类的职责与协作；Circuit Breaker 画出状态机图；Library 写出完整类 + 边界测试用例
- Design：**M6 IAM**（面经 6）——`system-design/iam.md`：认证 vs 授权、RBAC/ABAC、token 生命周期（JWT 与撤销）、会话存储、审计日志、多租户隔离
- 产出：`knowledge/ood-patterns.md`（类图 + 接口设计 + 测试点）、`system-design/iam.md`

**Day 10 · 9/27 周日 · 排序/贪心 + 安全设计**
- Coding：面经 12 商品排序变种（多关键字 + 稳定性）+ 面经 10 比赛变种二刷（换写法：桶/堆各一遍）+ LC 2512
- Design：**M7 PKI**（面经 7）与 **M6 KYC 扩展**（面经 1）——`system-design/pki.md`、`system-design/kyc.md`
  - PKI：CA 层级、证书签发/吊销（CRL vs OCSP）、私钥保护（HSM）、根 CA 离线
  - KYC：文档上传流水线、OCR + 第三方核验、PII 合规（GDPR/加密存储）、审核状态机
- 产出：`leetcode/sorting/*.md`、`system-design/pki.md`、`system-design/kyc.md`

**Day 11 · 9/28 周一 · 视频/存储与地理空间**
- Coding：1631 三解二刷（Dijkstra → 二分+BFS → 并查集排序边，一天内换实现）+ 复刷 LC 1334
- Design：**M8 Video 上传**（面经 5）+ **M10 Uber**（面经 8）——`system-design/video-upload.md`、`system-design/ride-hailing.md`
  - Video 深挖（这是面试官明确说要做 deep dive 的题）：分片上传/断点续传、对象存储与 CDN 预热、转码流水线（队列 + 分片并行）、播放清单生成
  - Uber：Geohash/QuadTree 附近查询、派单匹配、ETA、峰值削峰
- 产出：`system-design/video-upload.md`、`system-design/ride-hailing.md`

**Day 12 · 9/29 周二 · 全真模拟 1**
- Coding：**45min × 2 全真模拟**，从 Tier S 里随机抽两道，全程英文口述思路（模拟真实轮次）
- Design：**白板 45 分钟**随机抽一题（Metrics 或 Feed），从需求澄清开始完整走一遍，录音回听
- 复盘：把卡点写进 `_review-checklist.md`，明确 Day 13–14 要补什么

**Day 13 · 9/30 周三 · 全真模拟 2 + 弱项收割**
- Coding：Tier A 里还没拿下的题集中收割 + **模板默写**（Dijkstra 堆版、Kahn 拓扑、中序遍历、TopK 堆、Union-Find、rolling hash）+ 所有 Tier S 的边界用例默写
- Design：随机抽一题（IAM 或 Booking）+ 精读所有 `system-design/*.md`，把每个母题压成**5 分钟电梯版**
- 反问清单：整理 3 个好问题（团队规模/发布节奏/技术债）

**Day 14 · 10/1 周四 · 收口**
- Coding：面经全部题目**只看题干口述**（每题 30 秒讲思路 + 复杂度 + 一个坑），卡壳的立刻回看笔记；只看错题本，不开新题
- 项目 BQ（面经 Coding 部分第 1–3 条）：准备「最 proud 的项目 / 特别在哪 / 会换什么做法」三段 90 秒陈述，每段带数字
- Design：三个最高概率母题的电梯陈述（Metrics、Notification、Feed）+ 各自 3 个深挖点的速答
- 收尾：清空 `_review-checklist.md` 待办，检查 git 已推送

## 3. System Design 母题地图（17 题 → 10 母题）

| 母题 | 面经原题 | 必答组件 | 深挖点（面试官最可能追的） |
|---|---|---|---|
| **M1** Metrics/Monitoring | 3、15 | 采集 Agent、时序库、聚合层、查询 API、告警引擎 | 基数爆炸、迟到/乱序数据、多区域一致性与聚合、降采样保留策略 |
| **M2** Notification | 10、13 | 触发器、模板、优先级队列、投递工作器、状态机、死信 | 幂等键、at-least-once 去重、限流与退避、价格变动的实时性 |
| **M3** Feed/UGC | 2、14 | 写扩散 vs 读扩散、Feed 存储、排序服务、评论/评分 | 扇出写放大、名人问题、Review 聚合评分一致性、反作弊 |
| **M4** Search | 11 | 倒排索引、分词器、分片、相关性打分、索引管道 | NRT 增量索引、深翻页、拼写纠错、多语言分词 |
| **M5** Leaderboard | 12 | Redis ZSet（跳表）、写合并、分区分片、快照 | **跳表 vs B 树**（面经明确被扣分）、10M DAU 写入合并、榜单跨分片合并、作弊检测 |
| **M6** IAM/KYC | 6、1 | 认证服务、授权引擎、token 服务、审计、KYC 审核流水线 | JWT 撤销、RBAC vs ABAC、多租户、PII 加密与合规、第三方核验失败重试 |
| **M7** PKI | 7 | CA 层级、签发服务、吊销分发（CRL/OCSP） | 私钥保护（HSM）、根 CA 离线、证书轮换、时钟偏斜 |
| **M8** Video | 5 | 分片上传、对象存储、转码队列、CDN | 断点续传、上传深挖（multipart/校验）、转码并行与成本、首帧延迟 |
| **M9** Booking/Inventory | 9、16 | 库存服务、锁定服务、订单服务、支付对账 | 防超卖（乐观锁 vs 分布式锁 vs 预扣）、锁 TTL、支付超时回滚、热点分桶 |
| **M10** Geo/Dispatch | 8 | 位置上报、Geo 索引、匹配引擎、ETA | Geohash/QuadTree 对比、派单公平性、峰值削峰、位置数据过期 |

**设计题统一产出模板**（每份 `system-design/{theme}.md` 都按此结构写）
```
## 需求澄清（功能性 / 非功能性 / 规模假设）
## 容量估算（QPS、存储、带宽、机器数）
## API 设计
## 数据模型与存储选型（含为什么不是另一个）
## 高层架构（组件 + 数据流）
## 深挖点（3 个，每个 5 分钟）
## 失败模式与降级
## 演进路线（v1 → v2）
```

## 4. 每日验收标准

当天算过关的条件（自测用）：
1. 三道题都能**不看代码**口述思路 + 复杂度，其中至少一道能白板默写完整实现。
2. 每道题能说出**一个坑**和**一个优化方向**。
3. 设计题写完文档后，能对着文档**不看稿讲 5 分钟**。
4. `_review-checklist.md` 已更新，新笔记已入库（`_index.md` 计数 + Blind 75 勾选）。

## 5. 风险与预案

| 风险 | 预案 |
|---|---|
| 某天题量做不完 | 优先保 Tier S；Tier A 顺延到 Day 13 收割；**不做无题号的泛刷** |
| 设计题没思路 | 回 `system-design/framework.md` 的 5 问模板硬套，先讲容量估算争取时间 |
| 面经 9（LC 2327）核对不上 | 直接放弃该条，把时间给 934/1631 的变种练习 |
| HackerRank 环境 | **提前在无第三方库假设下练手写堆/桶**（面经 4 的提醒） |
| 面试提前到来 | 保底方案：Day1–5 + Day 7 模拟 + Day 14 收口（7 天核心版） |
| 时间还有富余 | 加练：272 Closest BST Value II、1102 Path With Maximum Minimum Value、778 Swim in Rising Water |

## 6. 进度追踪

| Day | 日期 | Coding | Design | 完成 |
|---|---|---|---|---|
| 1 | 9/18 | 934 / 323 / 200复刷 | 框架 + 容量估算 | [ ] |
| 2 | 9/19 | 347 / 23 / 703变种 | M1 Metrics P1 | [ ] |
| 3 | 9/20 | 146 / 208 / 49变种 | M1 Metrics P2 | [ ] |
| 4 | 9/21 | 68 / 1062+1044 / 408 | M2 Notification | [ ] |
| 5 | 9/22 | 210 / 1631 / 743 | M3 Feed/Review | [ ] |
| 6 | 9/23 | 297 / 270+530 / 54变种 | M4 Search | [ ] |
| 7 | 9/24 | 模拟 2 题 + 补漏 | M5 Leaderboard | [ ] |
| 8 | 9/25 | 638 / 322+518 / 2327 | M9 Booking | [ ] |
| 9 | 9/26 | Circuit Breaker / Job Runner / Library | M6 IAM | [ ] |
| 10 | 9/27 | 排序变种 / 比赛变种 / 2512 | M7 PKI + M6 KYC | [ ] |
| 11 | 9/28 | 1631 三解 / 1334复刷 | M8 Video + M10 Uber | [ ] |
| 12 | 9/29 | 全真模拟 ×2 | 白板 ×1 + 录音复盘 | [ ] |
| 13 | 9/30 | Tier A 收割 + 模板默写 | 5 分钟电梯陈述 | [ ] |
| 14 | 10/1 | 全题目口述 | 母题速答 + 项目 BQ | [ ] |
