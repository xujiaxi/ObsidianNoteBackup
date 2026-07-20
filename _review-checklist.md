# 🎯 面试复习清单

## 📅 今日复习（2026-07-19）

### 需要回顾
- [ ] **动态规划：股票系列状态机** — Best Time to Buy and Sell Stock I-IV（LC121/122/123/188）、With Cooldown（LC309）、With Transaction Fee（LC714）— **核心：I（一次交易）→ `minPrice` 扫描 + `maxProfit = max(maxProfit, price - minPrice)`。II（无限次）→ 贪心累加所有 `price[i] > price[i-1]` 的差值。III（两次交易）→ 左右遍历法或 4 状态 DP（buy1/sell1/buy2/sell2 四个变量滚动）。IV（k 次）→ `dp[i][k][0/1]` 三维 DP，k >= n/2 时退化无限次（贪心），否则 2k 个变量空间优化。Cooldown → 冻结一天，状态要扩展 cooldown 维度。Transaction Fee → 卖出时扣 fee，`dp[i][0] = max(dp[i-1][0], dp[i-1][1] + price[i] - fee)`。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：LC1 HashMap 一遍扫 `target - num` 匹配。LC53 Kadane 算法——`maxEndingHere = max(num, maxEndingHere + num)`（负贡献舍去），`maxSoFar = max(maxSoFar, maxEndingHere)`。LC153 二分找转折点——`nums[mid] < nums[right]` 说明右边有序，最小值在左半；否则最小值在右半。LC33 先定位有序侧——`nums[mid] <= nums[right]` 则右半有序，否则左半有序，再判断 target 是否在有序半内决定搜索方向。**

### 重点坑
- [ ] **Kadane 算法 `maxEndingHere` 更新方式**：必须用 `maxEndingHere = max(num, maxEndingHere + num)` 而非 `maxEndingHere += num`。反例：`nums = [-2, 1]` —— 如果 `maxEndingHere += num`，第一步 -2，第二步 maxEndingHere = -2 + 1 = -1；正确做法第二步 maxEndingHere = max(1, -2+1) = 1（直接从 1 重新开始）。**Kadane 的本质是「要么接续累加，要么从当前位置另起炉灶」。**
- [ ] **股票 IV（k 次交易）的空间缩退化**：当 `k >= n/2` 时，问题退化为无限次交易（LC122 贪心累加正 diff），**必须单独处理**，否则 `dp[k][2]` 的 O(nk) 会超时/爆内存。`dp[0][1] = -inf` 初始化不能忘记——第 0 天不可能持有股票。另一种常见坑：买入不算次数，卖出才算一次完整交易，循环中 `for t in range(1, k+1)` 注意 dp 维度含义。
- [ ] **旋转数组二分查找的有序半判断**：用 `nums[mid]` 与 `nums[right]` 比较。当 `nums[mid] <= nums[right]` 时右半有序，否则左半有序。注意边界条件——`<=` 而不是 `<` 处理 mid == right 的情况。**容易犯的错误**：用 `nums[mid] < nums[left]` 判断，在数组长度为 2 时左半判断出错。统一用右边界比较更可靠。
- [ ] **Two Sum HashMap 的重复值处理**：如果题目要求返回的是索引（而非值），遇到 `target - num` 等于 num 本身时，需要检查 `map[target - num] != i`（自己不能是自己），要在插入 map 之前判断。如果先插入再判断，会拿到同一个索引。正确顺序：`if complement in map: return [map[complement], i]`，然后再 `map[num] = i`。

### 建议刷的新题
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC1/LC53（扫描两次 O(n) 模式）。**核心**：先从左到右扫一遍构建 left 前缀积数组，再从右到左同步乘上 right 后缀积，空间可优化到 O(1)（输出数组不算额外空间）。**坑**：注意不能使用除法，需纯乘法构造。边界：`prefix[i] = prefix[i-1] * nums[i-1]`，`prefix[0] = 1`。
- [ ] **动态规划**：House Robber（Medium）— 关联已掌握股票系列状态机（选/不选的二维状态）。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`——不抢当前（继承 i-1）或抢（i-2 + 当前）。空间优化到两个滚动变量。**坑**：base case `dp[0] = nums[0]`，`dp[1] = max(nums[0], nums[1])`，注意处理好长度为 1 的边缘情况。
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握 LC1 Two Sum（HashMap 对）。**核心**：排序 + 固定第一个数，双指针找 `target = -nums[i]`。去重关键——外层 `i > 0 && nums[i] == nums[i-1]` 跳过，内层 `while left < right && nums[left] == nums[left+1] left++`。**坑**：不排序无法做双指针去重；去重逻辑写错会导致漏解或多解。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握股票系列 DP 思维。**核心**：斐波那契 `dp[i] = dp[i-1] + dp[i-2]`，O(1) 空间滚动变量。**坑**：base case `dp[1]=1, dp[2]=2` 容易写反；面试中注意不能用递归（栈溢出），用迭代。
- [ ] **字符串/DP**：Longest Palindromic Substring（Medium）— 关联已掌握 LC3/LC76 滑动窗口。**核心**：中心扩展法 O(n²)——每个位置（n 个字符 + n-1 个间隙）为中心向两边扩展；或 DP O(n²)——`dp[i][j] = (s[i]==s[j] && (j-i<=2 || dp[i+1][j-1]))`。**坑**：中心扩展法要注意回文可奇可偶，需要两轮循环（单字符中心、双字符中心）。DP 法注意遍历顺序——左端 i 从右向左，右端 j 从左向右才能用到 `dp[i+1][j-1]` 的子结果。

## 历史复习记录
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
