# 🎯 面试复习清单

## 📅 今日复习（2026-06-27）

### 需要回顾
- [ ] **图（Graph）**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：DFS 用 visited 或三色标记防环；BFS 用队列逐层扩散；拓扑排序用 Kahn 算法（入度统计）检测有向图环；沉岛时将访问过的陆地直接改 '0' 避免重复访问。**
- [ ] **二分查找（Binary Search）**：Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：与右边界 nums[right] 比较判断哪半有序；找最小值时 mid 与 right 比较，找目标值时先定有序半再判断；注意 while 条件和 return 值的边界处理。**
- [ ] **数组（Array）**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121） resurfaced（LC153/LC33 同属旋转数组系列）— **核心：哈希表存值找 complement；股票问题维护 minPrice 和 maxProfit，一次遍历 O(n)；数组类问题优先考虑双指针/前缀和/哈希表三种武器。**

### 重点坑
- [ ] **二分查找中 `while left < right` 与 `while left <= right` 的边界混淆** — 搜索区间是左闭右开还是左闭右闭决定循环条件和更新逻辑，推荐统一用 `left < right` + `right = mid` / `left = mid + 1` 的模板，避免死循环。
- [ ] **图的 DFS/BFS 忘记标记 visited 导致重复访问或无限递归** — 无论是邻接表还是矩阵，进队列/递归前必须 mark visited，否则不仅 TIME OUT，还可能 StackOverflow。
- [ ] **拓扑排序 Kahn 算法中，入队时减少邻居入度，但忘记在入度为 0 时才入队** — 每次移除节点后遍历其邻居入度 -= 1，只有当 inDegree[neighbor] == 0 时才加入队列；最后要检查已处理节点数是否等于总节点数来判断是否有环。

### 建议刷的新题
- [ ] **数组**：Contains Duplicate（Easy）— 关联已掌握知识：Two Sum（LC1）的 HashSet 思路，直接 O(n) 判断重复，空间换时间的经典应用。
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握知识：数组遍历 + 贪心，Kadane 算法维护当前和与最大和，经典 DP 入门，时间 O(n) 空间 O(1)。
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— 关联已掌握知识：Number of Islands（LC200）的 DFS/BFS，从边界反向灌水，找到同时能流到两个洋的格子。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists（LC21），用分治法两两合并或最小堆维护 k 个指针，时间复杂度 O(N log K)。
- [ ] **字符串**：Valid Anagram（Easy）— 关联已掌握知识：哈希表思维，用长度为 26 的数组统计字符频次，空间 O(1)，注意面试官可能追问 Unicode 扩展到 HashMap。

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Sliding Window | 2 | `sliding-window/` |
| Design | 2 | `design/` |
| Binary Search | 2 | `binary-search/` |
| Array | 1 | `array/` |
| String | 1 | `string/` |
| Heap | 1 | `heap/` |
| Greedy | 1 | `greedy/` |
| Backtracking | 0 | `backtracking拥有了 backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-ขอ让non` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 calamit  Pointers` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 timeout `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：22 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x旋律] **链表基础** — LC206 + LC141 + LC21 + LC19
