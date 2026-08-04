# 🎯 面试复习清单

## 📅 今日复习（2026-08-03）

### 需要回顾
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133） — **核心：LC200 沉岛算法——遍历到 '1' 计数 + DFS/BFS 把整片岛屿原地改成 '0'，避免重复计数；LC207 判环——DFS 三色标记（0 未访问 / 1 访问中 / 2 已访问），回溯遇到「访问中」即环，或 Kahn 算法 BFS（入度 0 入队，出队数 < 节点总数即有环）；LC133 克隆图——HashMap 存「原节点→克隆节点」，克隆邻居前先查表，防无限递归与重复创建。**面试口述**：图论先问「有向/无向、是否连通」；判环三件套——三色 DFS、Kahn 拓扑、并查集；克隆题一律「先建节点再连边」。**坑：LC200 沉岛必须原地改 '0' 或标记 visited，漏标会重复计数；四方向搜索先判越界；LC207 只用布尔 visited 会在 DAG 上误判成环（见重点坑）。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating（LC3）、Minimum Window Substring（LC76） — **核心：通用模板——外层 while 扩展右指针，内层 while 满足条件时收缩左指针并更新答案；LC3 用 dict 记字符最后出现位置，重复时左指针跳 `max(left, last+1)`；LC76 用 need 计数器 + have 变量（已满足的字符种类数），`have == len(need)` 时窗口合法，收缩时恢复计数。**面试口述**：先定「何时扩大 / 何时收缩 / 何时更新答案」三件事；LC3 更新答案在收缩后，LC76 更新答案在收缩过程中（求最小窗口）。**坑：LC76 收缩时必须同步恢复 need 计数并更新 have，漏掉会「假合法」；LC3 左指针用 `max(left, last+1)` 防止被旧位置拉回去。**
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 贪心——按开始时间排序，小顶堆存各会议室「结束时间」，新会议开始 ≥ 堆顶结束就 pop 复用再 push，否则 push 新开，堆大小即最少会议室数；LC348 行列 + 两条对角线各维护计数器，落子 +1 / -1，绝对值 == n 即胜；LC362 时间戳队列——hit 入队 (timestamp, count)，getHits 先弹出 `timestamp <= t - 300` 的旧记录，队列长度即 300 秒内点击数。**面试口述**：设计题先问「读多写多、数据规模、并发」；区间题先排序；堆的题想清楚「堆里存什么」——LC253 存结束时间。**坑：LC253 必须先排序否则贪心失效；堆顶比较用 `<=`（同时刻结束可复用）；LC362 同一秒多次 hit 要合并计数否则队列膨胀；LC348 别漏副对角线（`row + col == n - 1`）。**

### 重点坑
- [ ] **LC207 环检测必须三色标记**：只用布尔 visited 会把「已完全探索的节点」误判成环——反例 DAG：1→2、1→3、3→2（无环，但 DFS 到 3 发现 2 已访问会误报）。**正确**：0 未访问 / 1 当前路径 / 2 已探索完，遇到 1 才是环；或 Kahn 算法（入度 0 入队，出队数 < 节点数 = 有环）。
- [ ] **LC200 沉岛必须原地标记**：把访问过的 '1' 改成 '0'（或单独 visited 数组），漏标记会重复计数同一座岛甚至死循环；四方向搜索先判 `0 <= r < m and 0 <= c < n` 再递归，防越界。
- [ ] **LC76 收缩窗口要恢复计数**：左指针右移时必须 `need[s[left]] += 1`，且该字符计数从 0 变 1 时 `have -= 1`；只扩展不恢复会让窗口「假合法」、最小长度算错。**口诀**：扩展加计数，收缩减计数，两边对称。
- [ ] **LC253 排序 + 堆存结束时间**：不按开始时间排序贪心直接失效；堆顶是「最早结束的会议」，新会议开始 ≥ 堆顶结束才复用（用 `<=`）；把开始时间存进堆是常见错误。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿 DFS/BFS。**核心**：反向思维——从四条边界向里 DFS/BFS，两个 boolean 矩阵分别记录能流到太平洋/大西洋的格子，最后取交集。**坑**：从边界出发，向内要求 `next >= curr`（水往高处/平处流）；别对每个格子正向 DFS（O((mn)²) 超时）。
- [ ] **图论**：Longest Consecutive Sequence（Medium）— 关联已掌握 LC1 Two Sum 哈希思想。**核心**：HashSet 存全部数字，只从「序列起点」（`num - 1` 不存在）向后连续计数，整体 O(n)。**坑**：对每个数都向内扩展会退化成 O(n²)；用集合做 `num + 1` 查找而不是数组。
- [ ] **滑动窗口 / 字符串**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：窗口长度 - 窗口内最高频字符数 ≤ k 则合法，否则收缩；maxCount 只增不减（历史最大值）不影响正确性且省去收缩时重算。**坑**：更新答案在收缩之后；maxCount 不要每次重新统计。
- [ ] **间隔**：Merge Intervals（Medium）— 关联已掌握 LC253 Meeting Rooms II 的排序 + 区间处理。**核心**：按 start 排序，`curr.start <= prev.end` 即重叠，合并时 end 取 max，否则把 prev 收入结果并移动。**坑**：排序是关键前提；重叠判断用 `<=`（相邻也算重叠）。
- [ ] **堆**：Top K Frequent Elements（Medium）— 关联已掌握 LC253 小顶堆 + LC1 哈希。**核心**：HashMap 统计频率 → 小顶堆维护 Top K（堆满且新频率 > 堆顶就替换），或桶排序 O(n)。**坑**：用「小顶堆」不是大顶堆（大顶堆要维护全部元素才能取 Top K）；堆比较的是频率不是元素值。

## 历史复习记录
- 2026-08-03：图论 BFS/DFS、间隔 / 设计题（堆）、滑动窗口 & 字符串
- 2026-08-02：树与递归、链表、数组 & 二分查找
- 2026-08-01：图论 BFS/DFS、滑动窗口 & 字符串、动态规划（股票系列）
- 2026-07-30：链表、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-07-29：树与递归、滑动窗口 & 字符串、动态规划（股票系列）
- 2026-07-28：数组 & 二分查找、链表、图论 BFS/DFS
- 2026-07-27：树与递归、滑动窗口 & 字符串、间隔题 / 设计题（堆）
- 2026-07-26：链表、图论 BFS/DFS、动态规划（股票系列）
- 2026-07-25：滑动窗口 & 字符串、数组 & 二分查找、设计题
- 2026-07-24：树与递归、图论 BFS/DFS、动态规划（股票系列）
- 2026-07-23：数组 & 二分查找、链表
- 2026-07-22：树与递归、滑动窗口 & 字符串
- 2026-07-20：图论 BFS/DFS、链表
- 2026-07-19：动态规划、数组 & 二分查找
- 2026-07-18：树与递归、图论 BFS/DFS、滑动窗口 & 字符串
- 2026-07-17：数组 & 二分查找、链表
- 2026-07-16：树与递归、图论 BFS/DFS
- 2026-07-15：链表、滑动窗口 & 字符串
- 2026-07-14：数组 & 二分查找、图论 BFS/DFS
- 2026-07-13：树与递归、动态规划
- 2026-07-12：滑动窗口、链表
- 2026-07-11：图论 BFS/DFS、二分查找、数组基础
- 2026-07-07：滑动窗口、链表、树 DFS/BFS
- 2026-07-05：图论 BFS/DFS、二分查找、数组基础
- 2026-07-04：树与递归、链表、动态规划入门 — 股票系列
- 2026-07-03：数组 & 二分查找、图论 BFS/DFS、字符串 & 滑动窗口

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Array | 2 | `array/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Greedy | 1 | `greedy/` |
| Heap | 1 | `heap/` |
| String | 1 | `string/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：22 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：31 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
