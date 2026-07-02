# 🎯 面试复习清单

## 📅 今日复习（2026-07-01）

### 需要回顾
- [ ] **图（Graph）**：Clone Graph、Course Schedule、Number of Islands — **核心：DFS 三色标记法（灰黑检测环）VS BFS 拓扑排序（Kahn 算法）；Clone Graph 用 HashMap 映射旧→新节点 + DFS/BFS 复制；沉岛算法（Sinking Island）在 Number of Islands 中：访问到 '1' 时改为 '0' 避免重复访问。**
- [ ] **二分查找（Binary Search）**：Search in Rotated Sorted Array、Find Minimum in Rotated Sorted Array — **核心：旋转数组二分中，优先与右边界比较判断「哪半边有序」；搜索时若 target 落在有序区间内走正常二分，否则去另一半；找最小值时 mid > right → 最小值在右半，否则在左半（含 mid）。**
- [ ] **数组 / 动态规划入门**：Best Time to Buy and Sell Stock — **核心：一次遍历维护「历史最低买入价」和「当前最大利润」，dp[i] = max(dp[i-1], prices[i] - minPrice)，DP 数组可进一步优化到 O(1) 空间。**

### 重点坑
- [ ] **旋转数组二分中判断是否严格小于还是小于等于**：Find Minimum 中 `nums[mid] > nums[right]` 用 `>` 而非 `>=`，因为 `mid == right` 时不会出现；若写为 `>=` 会漏掉最小值在边界的情况。Search 中判断有序区间时也需精确区分，避免死循环或越界。
- [ ] **图 DFS 递归中忘记拷贝邻居列表**：Clone Graph 中如果直接 `for neighbor in node.neighbors: dfs(neighbor)` 可能会因为 `neighbors` 在递归中被修改而导致边遗漏。应先 `for neighbor in node.neighbors.copy()` 或 `list(node.neighbors)` 遍历。
- [ ] **买卖股票时「同一天买卖」的误解**：Best Time to Buy and Sell Stock 中虽然可以同一天卖又买，但只允许「一次交易」（买一次卖一次），不是无限次交易。注意区分原始版（一次）与 II（无限次）的区别。

### 建议刷的新题
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 前缀和思想。先用一遍从左到右的 prefixPass 算每个位置「左边所有乘积」，再从右往左乘上 rightProduct，两轮 O(n)。
- [ ] **链表 / 优先级队列**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists 扩展到 K 条链表，利用小顶堆（PriorityQueue）每次取最小节点，O(N log K) 时间。
- [ ] **数组 / 滑动窗口**：3Sum（Medium）— 关联已掌握知识：排序 + 双指针。先排序，外层固定一个数，内层左右指针找两数之和等于 -nums[i]，注意去重和跳过重复值。
- [ ] **字符串 / 哈希表**：Valid Anagram（Easy）— 关联已掌握知识：字符串基础 + 哈希表。用长度为 26 的数组计数，两字符串字母频次完全相等即为 True；也可用排序比较。
- [ ] **动态规划 / 简单递推**：Climbing Stairs（Easy）— 关联已掌握知识：DP 入门。本质斐波那契，dp[i] = dp[i-1] + dp[i-2]，可优化到 O(1) 空间。注意边界 dp[0]=1, dp[1]=1。

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |
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

**Blind 75 完成：20 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
