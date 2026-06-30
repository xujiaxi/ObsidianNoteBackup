# 🎯 面试复习清单

## 📅 今日复习（2026-06-29）

### 需要回顾
- [ ] **数组 / 二分查找（Binary Search）**：Find Minimum in Rotated Sorted Array、Search in Rotated Sorted Array — **核心：旋转排序数组中，与右边界 `nums[right]` 比较通常比左边界更可靠；寻找特定目标值 vs. 寻找边界的模板差异；处理 `mid` 后如何收缩区间避免死循环。**
- [ ] **图（Graph）**：Clone Graph、Course Schedule、Number of Islands — **核心：BFS 队列/DFS 递归两种克隆图的写法；Course Schedule 的三色标记法检测环（0=未访问, 1=访问中, 2=已完成）；Number of Islands 的沉岛算法避免重复访问。拓扑排序掌握 Kahn 算法（入度表+BFS）。**
- [ ] **数组基础**：Two Sum、Best Time to Buy and Sell Stock — **核心：Two Sum 用 HashMap 存值→索引，一次遍历 O(n)；买卖股票一次遍历记录最小值和最大利润，贪心思想。**

### 重点坑
- [ ] **二分查找区间端点开闭混淆**：`while (left <= right)` 配合 `left = mid + 1` / `right = mid - 1` 是闭区间写法；`while (left < right)` 配合 `left = mid + 1` / `right = mid` 是左闭右开。旋转数组中如果和 `nums[right]` 比较，注意 `mid == right` 时不会死循环，因为 `mid = left + (right - left) / 2` 始终偏左。
- [ ] **图克隆时忘记处理 visited**：Clone Graph 中如果不用 HashMap<Node, Node> 记录已克隆节点，会导致无限递归和重复克隆。DFS 或 BFS 都要先查 visited 再递归/入队。
- [ ] **买卖股票初始化 minPrice 用 Integer.MAX_VALUE 但忘记处理数组为空**：虽然 LeetCode 测试用例通常不会为空，但面试时要提一嘴边界；另外 `maxProfit` 初始为 0 比 `Integer.MIN_VALUE` 更自然，因为允许不交易获得 0 利润。

### 建议刷的新题
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握/helper with Kadane's algorithm，与 Best Time to Buy and Sell Stock 同根同源（最大子段和/最大利润都是线性 DP）。
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 前缀/后缀思想，先算左积再算右积，O(n) 时间 O(1) 额外空间（输出数组不算）。
- [ ] **字符串 / 哈希表**：Valid Anagram（Easy）— 关联已掌握知识：哈希表统计字符频次，和 Group Anagrams 同根同源，用 26 长度频次数组统计字符次数即可。
- [ ] **图 / DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握知识：Number of Islands 的 DFS/BFS，反向思维从边界海洋向内灌水，找同时能到达两个洋的格子。
- [ ] **链表 / 分治/堆**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists 的扩展，用最小堆维护 k 个指针或分治法递归两两合并，时间复杂度 O(N log K)。

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
