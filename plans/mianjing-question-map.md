# 面经题目解码表

> 原始来源：Google Doc 面经列表（Coding 32 条 / Design 17 条）
> 用途：把面经里的黑话/谐音题号还原成可执行的 LC 题号，方便核对与刷题
> 生成日期：2026-09-18

## 解码规则

面经用汉字谐音数字躲避筛选。已确认的映射（用已知题反推验证）：
`尔/儿=2、伞/叁/霰=3、思=4、乌=5、留=6、齐/其=7、疤/巴=8、玖=9、灵=0`

验证样本：`叁思齐` = 3-4-7 = LC 347（Top K Frequent Elements，且原文「只能用 heap 不能用 quick select」与题义吻合）。

## Coding 逐条映射

| 面经# | 原文摘要 | 还原题号 | 备注 |
|---|---|---|---|
| 1 | binary tree 找距 target 最近的节点 | LC 270 的普通二叉树版 | 普通树只能 O(n) DFS 比 abs；BST 才用 O(h) 二分下降 |
| 2 | Trie 设计字典，add/search | **LC 208** | Implement Trie (Prefix Tree) |
| 3 | course schedule 2 改 input，topo sort | **LC 210** | 追问是「relation map 能不能省」= 空间优化型争辩，见下 |
| 4 | 变种 Group Anagrams：add/remove/largestGroup | **LC 49 变种** | 本组最有价值：write-optimized vs read-optimized 权衡 |
| 5 | 两个岛之间最短距离 | **LC 934** | 面经 13–17 是同一题的详细解法复述 |
| 6 | find connected components in the graph | **LC 323** | 无向图连通分量（Union-Find 或 DFS） |
| 7 | BST 找与 target 差的绝对值最小的 node | **LC 270**（原文「似力扣伍叁零」= 530 是 Minimum Absolute Difference in BST，非本题） | 530 顺手做，easy |
| 8 | 图，起点终点，每条路径取最大边，求所有路径最大值中的最小 | **LC 1631** | 面经 22 同题（用 Dijkstra 变体） |
| 9 | 刷题网尔伞而其 | **LC 2327**（待核对） | 尔伞而其 = 2-3-2-7；LC 2327 Number of People Aware of a Secret。**未 100% 确认，做前先看题干** |
| 10 | 每轮往表里加一个数字，要拿到第 k 名才能进下一轮，求最小所需数字 | **LC 703 + 贪心变种** | 母题是「大小为 k 的堆维护第 k 大」，答案是每轮第 k 大的最大值 |
| 11 | 蠡口的留疤 | **LC 68** | 留=6、疤=8 → Text Justification（Hard，字符串模拟） |
| 12 | 《商品，价格，关注度》string list，输出低价高关注度商品 | 多关键字排序（参考 **LC 2512**） | 考 comparator 写法与稳定性，非难题 |
| 13 | 力扣 玖叁肆 最短桥 | **LC 934** | 同面经 5 |
| 14–17 | 934 的解法叙述（DFS 标岛 → BFS 扩水） | **LC 934** | 要点：island1 标 -1、island2 标 -2、多源 BFS 层层扩展 |
| 18 | 城市间距离图，求两城最短距离，无向权重图 | **LC 743 / 1334** | Dijkstra 模板题 |
| 19 | 字符串中最长重复子串 + 优化 hashcode + 二分 | **LC 1062 / 1044** | 原文链接片段 `longest…eating-substring` → 1062；1044 是 binary search + rolling hash 的 Hard 版 |
| 20 | 斯灵巴 | **LC 408** | 斯=4、灵=0、巴=8 → Valid Word Abbreviation |
| 21 | 儿shi霰 + 追问「合并时链表太长本地内存写不下」 | **LC 23** | Merge k Sorted Lists；追问考外部归并排序（K 路 + 磁盘缓冲 + 多轮合并） |
| 22 | 两个数组存 edge 与长度，起点终点，求最短路径中最长的 edge | **LC 1631** | 同面经 8；原文点明用 Dijkstra |
| 23 | 链表的值按「利口乌丝」方式填入矩阵 | **LC 54 变种** | 乌丝=5、4 → Spiral Matrix，输入换成链表 |
| 24 | Implement a circuit breaker | 非 LC（并发 OOD） | 状态机 closed/open/half-open + 滑动窗口失败率 + 线程安全 |
| 25 | 叁思齐变种，不能用 quick select，只能 heap | **LC 347** | 流式/变种场景下 quickselect 退化的原因要讲清 |
| 26 | 利口 638 | **LC 638** | Shopping Offers（DFS+记忆化 / 完全背包变体） |
| 27 | LRU Cache | **LC 146** | HashMap + 双向链表（或 OrderedDict） |
| 28 | deserialize 和 serialize binary tree | **LC 297** | 前序 + `#` 占位；BFS 版 |
| 29 | 1point3acres 链接 | — | 仅链接，无题目内容 |
| 30 | Document classes for a "job runner"（并行、并发上限、STDOUT/STDERR 入库、heartbeat） | 非 LC（OOD/并发） | 给的 JobQueue / SystemCommand 接口是关键，按接口反推类图 |
| 31 | Library 管理图书出借（borrow/return/listBooks，设计 User/Book 类） | 非 LC（OOD） | 考 OOP 与 code quality，不考算法 |
| 32–33 | 空 | — | — |

## 面经高频信号（决定优先级）

- **LC 934 出现 6 次**（面经 5、13、14、15、16、17）→ 全plan 最高优先级
- **图/最短路类题共 6 条**（6、8、18、22 + 934 系列）→ 图是最集中的主题
- **设计数据结构类 5 条**（2、4、27、28 + 24）→ LRU/Trie/序列化/熔断必须手写
- **堆与 Top K 3 条**（10、21、25）→ 堆的三种用法（TopK/合并/流式）
- **OOD 3 条**（30、31、24）→ 边界清晰的类图 + 接口设计，别写伪代码糊弄
- HackerRank 环境**没有 `sortedcontainers`**（面经 4 提醒）→ 手写堆/桶的退路要提前准备

## Design 逐条映射

| 面经# | 原题                                             | 归入母题                    | 计划中的日子  |
| --- | ---------------------------------------------- | ----------------------- | ------- |
| 1   | Design a KYC system                            | M6 IAM/KYC              | Day 10  |
| 2   | Design a Review Service                        | M3 Feed/UGC             | Day 5   |
| 3   | Multi-Region Metrics Monitoring System         | M1 Metrics              | Day 2–3 |
| 5   | design youtube deep dive uploading large video | M8 Video                | Day 11  |
| 6   | design IAM system                              | M6 IAM/KYC              | Day 9   |
| 7   | design PKI                                     | M7 PKI                  | Day 10  |
| 8   | Uber                                           | M10 Geo/Dispatch        | Day 11  |
| 9   | online ticket booking system                   | M9 Booking/Inventory    | Day 8   |
| 10  | notification system                            | M2 Notification         | Day 4   |
| 11  | 设计 search 系统                                   | M4 Search               | Day 6   |
| 12  | 游戏实时 Leaderboard，10M DAU（考点：跳表）                | M5 Leaderboard          | Day 7   |
| 13  | pricing notification system                    | M2 Notification 变体      | Day 4   |
| 14  | News Feed system                               | M3 Feed/UGC             | Day 5   |
| 15  | Metric 收集和查询系统                                 | M1 Metrics 变体           | Day 2–3 |
| 16  | 库存管理系统（电商）                                     | M9 Booking/Inventory 变体 | Day 8   |

## 面经暴露的追问套路（每条都要准备 30 秒答案）

1. **LC 3 的拓扑排序空间反转**：面试官说「degree map 留着、relation map 可以省」——他想要的是邻接表方向反转（存 `node → 依赖它的节点`），这样 kahn 里不用查原图。原作者的困惑点在于 input 是 dependency map。**准备答案**：正向邻接表 O(V+E) 空间换 O(1) 更新 vs 反向邻接表省一半空间；先反问「input 是否可变 / 能否预处理」。
2. **LC 4 的 read vs write optimized**：写多读少 → 不维护有序结构，`largestGroup()` 时 O(n) 扫；读多写少 → 维护有序结构，三个操作 O(log n)。指标：读/写比例、延迟 SLA、组数量级。
3. **LC 21 的内存溢出追问**：链表放不下本地内存 → 外部归并排序（K 路 + 分块排序落盘 + 多轮合并），讲清缓冲区大小与 I/O 次数。
4. **HackerRank 无第三方库**：手写最大堆（存负数）、手写桶、手写有序结构。
