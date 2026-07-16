# 🎯 面试复习清单

## 📅 今日复习（2026-07-15）

### 需要回顾
- [ ] **链表**：Reverse Linked List（LC206）、Detect Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19）— **核心：反转链表用三指针 prev/curr/next，先保存 next 再改指针；快慢指针检测环注意 while(fast != null && fast.next != null) 双重判空；合并链表用 Dummy Node 哨兵节点头；删除倒数第 N 个节点用 fast 先走 N 步再同步走。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：通用模板 — 外层 while 右指针扩展并更新状态，内层 while 满足条件时收缩左指针并反向更新状态。LC3 用 Set/Map 记录窗口内字符；LC76 用 need/have 双计数器精确匹配目标子串。**

### 重点坑
- [ ] **链表快慢指针空指针异常**：`while (fast != null && fast.next != null)` 两个条件缺一不可。fast != null 确保节点存在，fast.next != null 确保能走两步。只写 `while (fast.next != null)` 在 fast 为 null 时直接 NPE。反转链表时也容易忘记用 `next = curr.next` 保存下一节点再改指向。
- [ ] **滑动窗口收缩时忘记反向更新**：窗口扩张时增加计数（map[key]++ / have++），但在内层 while 收缩窗口时常常忘记同步减少计数或移除索引。**黄金模板**：扩张（右移）和收缩（左移）的操作必须成对出现——增加什么就减少什么。

### 建议刷的新题
- [ ] **链表**：Reorder List（Medium）— 关联已掌握链表反转（LC206） + 快慢指针（LC141） + 合并链表（LC21）。三步法：找中点、翻转后半、交叉合并。面试高频组合题，一题考三个知识点。
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握 Two Sum 哈希表（LC1）。排序后固定一个数，双指针在剩余区间查找两数之和等于当前数的相反数。去重模板（跳过重复值）面试必考，O(N²) 时间 O(1) 空间。
- [ ] **数组/DP**：Maximum Subarray（Medium）— 关联已掌握 Best Time to Buy and Sell Stock（LC121）的一遍扫描思路。Kadane 算法 `cur = max(num, cur + num)` 本质是退化到 O(1) 空间的 DP，面试最经典之一。
- [ ] **图/DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 Number of Islands（LC200）DFS。从四条边界向中间反向 DFS，分别标记能流入太平洋和大西洋的格子，最后取交集。核心：反向推导比正向模拟简单得多。
- [ ] **树/BST**：Kth Smallest Element in a BST（Medium）— 关联已掌握 Validate BST（LC98）的中序遍历递增性质。BST 中序遍历即有序序列，用递归或迭代栈找第 K 个节点。进阶掌握 Morris Traversal O(1) 空间。

## 历史复习记录
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
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 2 | `array/` |
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

- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
