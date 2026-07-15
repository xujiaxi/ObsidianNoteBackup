# 🎯 面试复习清单

## 📅 今日复习（2026-07-14）

### 需要回顾
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：Two Sum 哈希表 O(N) 一 pass；Best Time 用 minPrice 和 maxProfit 一遍扫描；旋转数组二分查找与右边界 nums[right] 比较比左边界更可靠；区分查找指定值（while left <= right）和查找旋转点（while left < right）两种模板。**
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：图的邻接表构建；Clone Graph DFS/BFS 用 HashMap 记录原→新节点映射避免重复克隆；Course Schedule 拓扑排序 Kahn 算法（BFS 入度表）和 DFS 三色标记法；Number of Islands 沉岛算法（访问过的 1 改为 0）。**

### 重点坑
- [ ] **二分查找边界混淆**：`while (left <= right)` 与 `while (left < right)` 的选择直接影响结果。查找确切值用 `<=`（循环结束时 `right < left`，区间为空）；查找旋转点/边界用 `<`（循环结束时 `left == right`，指向目标位置）。在旋转排序数组中，与 `nums[right]` 比较比 `nums[left]` 更可靠，因为旋转点右侧一定是递增段（LC33/153 模板）。
- [ ] **图遍历未标记已访问**：Clone Graph 中忘记在 HashMap 记录已克隆节点会导致无限递归栈溢出；Number of Islands 中漏掉沉岛标记会导致同一岛屿被重复计数。**黄金原则**：DFS 在递归进入前立即标记 visited，BFS 在入队时标记（而非出队时），确保每个节点只处理一次。

### 建议刷的新题
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握 Two Sum 哈希表（LC1）。排序后固定一个数，双指针在剩余区间内查找两数之和等于当前数的相反数。去重模板（跳过重复值）面试高频，O(N²) 时间 O(1) 空间。
- [ ] **数组/DP**：Maximum Subarray（Medium）— 关联已掌握 Best Time to Buy and Sell Stock（LC121）的一遍扫描思路。Kadane 算法 `cur = max(num, cur + num); maxSum = max(maxSum, cur)` 本质是压缩到 O(1) 空间的 DP，面试最高频题之一，必须能秒。
- [ ] **图 / DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 Number of Islands 的 DFS（LC200）。从四条边界向中间反向 DFS，分别标记能流入太平洋和大西洋的格子，最后取交集。核心思维：反向推导比正向模拟简单得多。
- [ ] **树 / BST**：Kth Smallest Element in a BST（Medium）— 关联已掌握 Validate BST 的中序遍历递增性质（LC98）。BST 中序遍历即有序序列，用递归或迭代栈（显式 Stack）找第 K 个访问节点。掌握 Morris Traversal（O(1) 空间）可加分。

## 历史复习记录
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

**Blind 75 完成：21 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
