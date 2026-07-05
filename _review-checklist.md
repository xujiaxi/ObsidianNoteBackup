# 🎯 面试复习清单

## 📅 今日复习（2026-07-04）

### 需要回顾
- [ ] **树与递归（Tree & DFS）**：Construct Binary Tree from Preorder and Inorder Traversal、Lowest Common Ancestor of BST、Validate Binary Search Tree — **核心：前中序构建树时，preorder 首元素是根，在中序中找到根位置划分左右子树；BST 中 LCA 利用大小关系左右搜索；区间校验 `(min, max)` 递归判断。**
- [ ] **链表（Linked List）**：Reverse a Linked List、Merge Two Sorted Lists、Remove Nth Node From End — **核心：反转链表的三指针迭代法（prev/cur/next）；合并链表 dummy 哨兵节点 + 双指针；双指针找倒数第 N 个（fast 先走 N 步）。**
- [ ] **动态规划入门 — 股票系列**：Best Time to Buy and Sell Stock（Python 版含完整系列）— **核心：一维 DP 状态机 `hold[i]` vs `sold[i]`，多状态递推；空间压缩到 O(1)。**

### 重点坑
- [ ] **递归终止条件写错**：Construct Binary Tree 中 preorder 索引越界检查；mergeTwoLists 中有一条链表为空时直接返回另一条，不要遗漏。
- [ ] **链表反转指针断裂**：反转前先把 next 保存到临时变量，否则断链后无法继续遍历。
- [ ] **双指针 fast/slow 边界**：Remove Nth Node 时 fast 先走 N+1 步（含 dummy），保证 slow 停在待删节点的前一个。否则易删错节点。
- [ ] **滑动窗口收缩后忘记同步更新**：收缩左指针后，`window[c]` 减少后如果 `window[c] < need[c]`，必须 `valid--`。漏掉会导致 valid 虚高，窗口不满足条件。
- [ ] **Java Integer 比较**：务必用 `.equals()`，而非 `==`，因为超过 Integer Cache (-128~127) 会缓存未命中导致错误。

### 建议刷的新题
- [ ] **链表 / 分治+优先队列**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists + 堆操作。最小堆维护 K 个链表头，每次 pop 最小值并将 next 推入堆。时间 O(N log K)。
- [ ] **树 / 递归**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握知识：树 DFS + 后序遍历。递归返回以当前节点为端点的最大路径和，全局维护 maxSum，注意「路径」不能分叉，返回值取 `max(left, right, 0) + node.val`。
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板。窗口内允许替换 k 次使字符相同，维护 maxFreq，当 `right-left+1-maxFreq > k` 时收缩 left。
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 双指针。先用左遍历求左侧乘积，再反向遍历用右侧乘积乘入；常数空间 O(1) 的输出空间解法。

## 历史复习记录
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

**Blind 75 完成：20 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
