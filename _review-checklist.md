# 🎯 面试复习清单

## 📅 今日复习（2026-08-11）

### 需要回顾
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 哈希表——「先查 `target - nums[i]` 再存入」，一次遍历 O(n)；LC121 维护历史最低价，`profit = max(profit, price - minPrice)`；LC53 Kadane——`maxEndingHere = max(nums[i], maxEndingHere + nums[i])`，`maxSoFar` 取全局最大；LC153/LC33 旋转数组二分——与 `nums[right]` 比较（比左边界更可靠）判断哪半边有序，LC33 先判「左半有序还是右半有序」再决定 target 落在哪边。**面试口述**：二分题先确认数组是否有序/部分有序、是否有重复元素；哈希题先想「空间换时间」。**坑：LC1 先存入再查询会重复使用同一个元素；LC153 用 `nums[mid] > nums[right]` 判断最小值在右半；LC33 的 `lo <= hi` 边界与区间收窄别写错。**
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——DFS/BFS 遍历到 '1' 即岛屿计数 +1，并把访问过的陆地置 '0' 防止重复访问；注意四方向越界检查。LC207 拓扑排序——Kahn's BFS：统计入度，入度为 0 的课程入队，逐个出队并减少依赖课程入度，最后出队数 == 课程总数则无环；DFS 版用三色标记（0 未访问 / 1 访问中 / 2 已完成），递归路径上遇到「访问中」即有环。LC133 克隆图——哈希表存 `old -> new` 映射，BFS/DFS 遍历时邻居已克隆则直接取映射，否则新建并入队/递归。**面试口述**：图题先问「有向还是无向」「是否允许修改输入」；环检测优先想拓扑排序。**坑：LC200 忘记沉岛会死循环/重复计数；LC207 只用「已访问」集合判环会漏判——必须区分「访问中」与「已完成」。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）、Longest Common Prefix（LC14） — **核心：通用模板——外层 while 扩展右指针，内层 while 满足条件时收缩左指针。LC3 用 `int[128]` 计数窗口内字符，出现重复则收缩左指针直到无重复，答案 = 最大窗口长度。LC76 用 need 计数 + `valid` 匹配数（need 中已满足的字符种类数）：右扩时若 `window[c] == need[c]` 则 `valid++`，收缩时若 `window[c] == need[c]` 则 `valid--`，`valid == need.size()` 时更新最小窗口。LC14 纵向比较——以第一个字符串为基准逐列比较，遇到不匹配或越界即返回。**面试口述**：滑动窗口题先确认「何时扩张、何时收缩、何时更新答案」三件事。**坑：LC76 更新答案要放在收缩左指针之前（窗口仍覆盖时）；LC3 收缩时记得把左指针字符计数减掉；`valid` 增减时机写反会导致永远不满足。**
### 重点坑
- [ ] **LC153/LC33 旋转数组二分「与右边界比较」**：最小值/搜索题统一与 `nums[right]` 比较——`nums[mid] > nums[right]` 说明最小值在右半；LC33 先判断哪半有序再二分。坑：`lo < hi` 与 `lo <= hi` 混用、`mid` 与边界相等时的处理。
- [ ] **LC207 环检测「三色标记」**：DFS 必须区分「访问中（灰）」与「已完成（黑）」，递归路径上再次遇到灰色节点才是有环；只用一个 visited 集合判环会漏判。Kahn's BFS 则检查「出队节点数 == 节点总数」。
- [ ] **LC76 最小覆盖子串「valid 计数与收缩时机」**：`valid` 只在 `window[c] == need[c]` 的临界点 ±1；更新答案必须在收缩左指针**之前**；用 `int[128]` 数组代替哈希表，避免装箱与 Integer 缓存问题。
- [ ] **LC1 Two Sum「先查后存」+ Java 比较坑**：先 `containsKey(target - nums[i])` 再 `put`，否则同一个元素会被用两次；Java 中两个 `Integer` 对象比较必须用 `.equals()`（-128~127 之外会踩缓存坑），HashMap 的 values 尤其要注意。

### 建议刷的新题
- [ ] **滑动窗口**：Longest Repeating Character Replacement（LC424，Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：窗口内 `windowLen - maxCount <= k` 时右扩，否则收缩左指针；`maxCount` 为窗口内出现次数最多的字符数。**坑**：收缩时 `maxCount` 不必回退（历史最大值即可，答案只增不减）。
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握 LC200 Number of Islands 的 DFS/BFS。**核心**：从四条边界**反向** DFS/BFS，分别标记能流到太平洋/大西洋的格子，两个 boolean 矩阵都为 true 的格子即答案。**坑**：从海向陆地反向推（水往低处流，反向即往高处走）；别从每个格子正向 DFS，会超时。
- [ ] **数组**：Maximum Product Subarray（LC152，Medium）— 关联已掌握 LC53 Maximum Subarray 的 Kadane。**核心**：同时维护 `maxProd` 与 `minProd`（负负得正），遇 0 重置为 1。**坑**：只维护最大值会漏掉「两个负数相乘变大」的情况。
- [ ] **数组 / 双指针**：3Sum（LC15，Medium）— 关联已掌握 LC1 Two Sum 的哈希/双指针思想。**核心**：排序后固定 i，双指针 l/r 逼近 `-nums[i]`；跳过重复元素去重。**坑**：先排序是前提；去重要同时处理 i、l、r 三处重复。
- [ ] **图论 / 回溯**：Word Search（LC79，Medium）— 关联已掌握 LC200/LC133 的 DFS 遍历。**核心**：网格 DFS + 回溯，访问过的格子临时标记（如置 '#'）再恢复；首字母不匹配直接剪枝跳过。**坑**：回溯后必须恢复现场；别忘记越界检查。

## 历史复习记录
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
