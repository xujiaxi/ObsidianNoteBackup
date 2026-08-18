# 🎯 面试复习清单

## 📅 今日复习（2026-08-17）

### 需要回顾
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76） — **核心：通用模板——外层 `while` 扩展右指针，满足条件后内层 `while` 收缩左指针，每步更新答案。LC3 用 HashMap/数组记录字符最后出现位置，遇重复字符时 `left = max(left, 上次位置+1)`；LC76 用 need 计数 + matched 判断窗口是否覆盖全部目标字符，覆盖后收缩左指针并更新最小窗口。**面试口述**：先说明适用场景（连续子串 + 极值问题），再讲「扩展-收缩」两阶段。**坑：收缩左指针时必须同步更新窗口状态（计数/长度）；LC76 的 matched 别每步重新扫描。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、II（LC122）、III（LC123）、IV（LC188）、Cooldown（LC309）、Transaction Fee（LC714） — **核心：状态机 `dp[i][0]` 不持有 / `dp[i][1]` 持有。LC121 一遍遍历维护 minPrice 和 maxProfit；LC122 贪心累加所有上升段；LC123/188 加交易次数维度 k；LC309 卖出后需冷却一天（买入时用 i-2 的状态）；LC714 卖出时统一扣手续费。**面试口述**：先分清「只能买卖一次 vs 可多次」，再决定用贪心还是状态机 DP。**坑：转移顺序「先更新不持有（卖出），再更新持有（买入）」；base case `dp[0][1] = -prices[0]`；手续费只在卖出扣一次。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 哈希表边遍历边查 `target - num`，先查后存；LC53 Kadane——`curr = max(num, curr + num)`，负贡献直接丢弃重新开始；LC153 与右边界 `nums[right]` 比较判断最小值所在半区；LC33 先判断 mid 落在哪一半有序，再决定搜索方向。**面试口述**：哈希/双指针/二分都是 O(n) 或 O(log n) 的「空间换时间」套路，先问数据是否有序、是否允许额外空间。**坑：LC1 先查后存避免同一元素用两次；LC153 与右边界比较比左边界更稳；LC33 循环条件 `l <= r` 与有序半区判断易写错。**（LC53 负前缀直接丢弃，是 Kadane 的精髓；LC121 可以看成「只交易一次」的简化版 DP。）**

### 重点坑
- [ ] **滑动窗口状态同步**：LC76 收缩左指针时必须同步更新窗口内字符计数和 matched；忘记更新会导致窗口「假覆盖」、答案错乱。模板记忆：外层 while 扩 right → 内层 while 缩 left → 每次移动都同步状态 → 满足条件时更新答案。
- [ ] **股票 DP 状态机转移顺序**：先更新「不持有」（今天卖出 = 昨天持有 + prices[i] - fee），再更新「持有」（今天买入 = 昨天不持有 - prices[i]）；LC309 冷却要求买入时用 i-2 的不持有状态；LC714 手续费在卖出时统一扣，别两边都扣；LC188 记得 k 从 1 开始、交易次数维度别越界。
- [ ] **Kadane 与旋转二分边界**：LC53 当 `curr + num < num` 时从 num 重新开始（负前缀丢弃）；LC153 用 `nums[mid] > nums[right]` 判断最小值在右半；LC33 用 `nums[mid] >= nums[l]` 判断左半有序，二分边界写错会死循环或漏解——写完用旋转数组在中间/两端的三组用例自测。

### 建议刷的新题
- [ ] **滑动窗口**：Longest Repeating Character Replacement（LC424，Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：窗口合法条件 `窗口长度 - 窗口内最大字符频次 <= k`，用频次数组 + maxCount 维护；不满足时收缩左指针。**坑**：maxCount 只增不减也能保证正确性（窗口只会变大），别在收缩时重新计算。
- [ ] **数组**：3Sum（LC15，Medium）— 关联已掌握 LC1 Two Sum + 排序思想。**核心**：排序后固定第一个数，剩下两个数用双指针从两端收缩；注意去重——固定数和双指针都要跳过相同值。**坑**：先排序再去重；双指针移动时 `while (l < r && nums[l] == nums[l-1]) l++` 防止重复三元组。
- [ ] **数组**：Product of Array Except Self（LC238，Medium）— 关联已掌握数组两遍遍历思路（前缀思想）。**核心**：第一遍从左到右累乘前缀积，第二遍从右到左乘后缀积，输出数组不算额外空间 → O(1) 空间。**坑**：不能用除法（含 0 会崩），必须用前缀×后缀两遍遍历。
- [ ] **DP**：House Robber（LC198，Medium）— 关联已掌握股票系列 DP 状态转移。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`（抢当前则跳过上一家），滚动两个变量优化到 O(1) 空间。**坑**：base case 处理 `dp[0]` 和 `dp[1]`；注意不能连续抢相邻两家。
- [ ] **DP**：Maximum Product Subarray（LC152，Medium）— 关联已掌握 LC53 Maximum Subarray 的 Kadane 思想。**核心**：因为负负得正，同时维护当前最大积和最小积：`max_cur = max(num, max_cur * num, min_cur * num)`，`min_cur` 同理取最小。**坑**：交换 max/min 或忘记同时更新两者会漏掉负数翻转的情况；与 LC53 的差异就在「乘法符号翻转」。

## 历史复习记录
- 2026-08-17：滑动窗口 & 字符串、动态规划（股票系列）、数组 & 二分查找
- 2026-08-16：图论 BFS/DFS、链表、树与递归
- 2026-08-15：动态规划（股票系列）、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-08-14：链表、树与递归、滑动窗口 & 字符串
- 2026-08-13：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-12：动态规划（股票系列）、链表、树与递归
- 2026-08-11：数组 & 二分查找、图论 BFS/DFS、滑动窗口 & 字符串
- 2026-08-10：链表、树与递归、间隔 / 设计题（堆）
- 2026-08-09：图论 BFS/DFS、数组 & 二分查找、动态规划（股票系列）
- 2026-08-08：链表、树与递归、滑动窗口 & 字符串
- 2026-08-07：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-06：滑动窗口 & 字符串、动态规划（股票系列）、树与递归
- 2026-08-05：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-04：动态规划（股票系列）、树与递归、链表
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
