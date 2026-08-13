# 🎯 面试复习清单

## 📅 今日复习（2026-08-12）

### 需要回顾
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、II（LC122）、III（LC123）、IV（LC188）、含冷却期（LC309）、含手续费（LC714） — **核心：股票系列本质是「持有 / 不持有」两状态的状态机 DP，`dp[i][0]` 持有、`dp[i][1]` 不持有，初始化 `dp[0][0] = -prices[0]`。LC121 一次交易可贪心——维护历史最低价，`profit = max(profit, price - minPrice)`；LC122 无限次交易——只要 `prices[i] > prices[i-1]` 就累加差价；LC123 最多两次——拆左右两段（前缀最大利润 + 后缀最大利润）相加；LC188 k 次——k ≥ n/2 时退化为无限次交易；LC309 冷却期——卖出后隔一天才能买，需三状态或错位一天；LC714 手续费——卖出时 `- fee`。**面试口述**：先确认「交易次数限制」「是否有冷却期 / 手续费」，再决定用贪心还是状态机 DP。**坑：初始化 `dp[0][持有]` 漏写；LC309 转移顺序写反会「当天卖当天买」。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 迭代反转——`prev / curr / next` 三指针，先存 `next = curr.next` 再改 `curr.next = prev`，最后整体前移。LC141 快慢指针——`slow` 一步、`fast` 两步，相遇即有环。LC21 合并——`dummy` 哨兵节点 + 双指针比较，谁小接谁。LC19 删除倒数第 N——`dummy` + 快指针先走 N 步，再快慢同步走，慢指针停在待删节点前一个。**面试口述**：先想「是否需要 dummy 节点」「空链表 / 单节点 / 删头节点」边界。**坑：反转时先存 next 再改指向，否则断链；`fast` 移动前判空。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree（LC105）、Validate BST（LC98）、LCA of BST（LC235）/ Binary Tree（LC236） — **核心：LC104 后序——`max(left, right) + 1`；LC100 递归比较左右子树；LC226 反转——swap 左右后递归；LC102 层序——BFS + queue 按层记录；LC105 重建——前序首元素为根，中序定位切分左右区间递归；LC98 验证 BST——中序遍历严格递增或递归传 `(min, max)` 区间；LC235 BST 的 LCA 按值比较走左右，LC236 普通树 LCA 后序递归、左右都非空即答案。**面试口述**：先定「前/中/后序还是层序」与「递归返回值代表什么」。**坑：LC98 只比较左右孩子会漏判（要整棵子树区间约束）；LC105 中序索引定位别算错。**
### 重点坑
- [ ] **股票状态机「持有 / 不持有」的初始化与转移顺序**：`dp[0][持有] = -prices[0]` 别漏；LC309 冷却期——卖出后第二天才能买，转移顺序写反会「当天卖当天买」；LC714 手续费只在卖出时扣一次，别在买入时扣。
- [ ] **链表反转的三指针顺序**：先 `next = curr.next` 存下家 → 再 `curr.next = prev` 改指向 → 最后移动指针，顺序错一步就断链；删除类题目（LC19、删头节点）一律用 dummy node 简化边界。
- [ ] **LC98 验证 BST 的区间约束**：只检查「左 < 根 < 右」会漏判——`[5,1,4,null,null,3,6]` 局部合法、整体非法；必须递归传 `(min, max)` 区间，或中序遍历严格递增。
- [ ] **树 DFS 深递归 StackOverflowError**：理解 Stack vs Heap 内存模型，深度递归（如链表状树）数据量不大也可能栈溢出；面试可提「显式栈 / 迭代」替代方案。

### 建议刷的新题
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握 LC206 反转 + LC141 快慢指针 + LC21 合并。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两段。**坑**：找中点后记得断开两段链表；交替合并时别丢链。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握 LC100 Same Tree。**核心**：遍历每个节点，判断「以该节点为根的子树是否与目标树相同」（Same Tree 递归）。**坑**：子树必须整棵匹配，不能只匹配部分路径。
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握 LC98 中序遍历。**核心**：BST 中序遍历即升序，数到第 k 个即答案；迭代栈版可提前终止。**坑**：递归版别遍历完整棵树再取；计数器需传引用 / 全局变量。
- [ ] **动态规划**：House Robber（LC198，Medium）— 关联已掌握股票系列「持有 / 不持有」状态思想。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，相邻不能同时取。**坑**：基线 `dp[0]`、`dp[1]` 初始化；空间可滚动优化为两个变量。
- [ ] **动态规划 / 贪心**：Jump Game（LC55，Medium）— 关联已掌握 LC122 贪心 + LC53 前缀思维。**核心**：维护最远可达 `maxReach = max(maxReach, i + nums[i])`，`i > maxReach` 即不可达。**坑**：贪心即可，无需 DP 数组；`maxReach >= n-1` 可提前返回。

## 历史复习记录
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
