# 🎯 面试复习清单

## 📅 今日复习（2026-06-26）

### 需要回顾
- [ ] **链表（Linked List）**：Reverse a Linked List（LC206）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End Of List（LC19）— **核心：dummy node 简化头节点操作；双指针（快慢指针）找倒数第 n 个；反转时先保存 next 到临时变量，再调整 cur.next = prev，三指针顺序 prev/cur/next 不能乱。**
- [ ] **树（Tree）**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Construct Binary Tree from Preorder and Inorder Traversal（LC105）— **核心：递归 base case 空树返回 0/None；分治先序找根、中序分左右区间；镜像反转递归交换左右子树。**
- [ ] **字符串（String）**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：滑动窗口模板：外层扩 right，内层 while 满足条件时收缩 left；HashMap 存字符最后出现位置或 need 字典 + formed 计数器。**

### 重点坑
- [ ] **链表反转时忘记保存 next 指针导致断链** — 反转前必须先用 temp = cur.next 保存，再 cur.next = prev，最后 prev = cur, cur = temp；顺序不能乱，否则链表会断。
- [ ] **递归处理二叉树时 base case 返回后上层不判空** — 比如求深度时 root 为 None 返回 0，但上层计算 max(left, right) 时若子问题的返回值直接用于索引可能越界，注意区分「空节点的返回值」和「实际业务逻辑」。
- [ ] **最小覆盖子串收缩 left 时 formed 条件判断与更新顺序** — 先检查当前 window 是否满足 formed == required，再收缩；收缩过程中每移动一次 left 都要更新 window 字符计数和 formed 状态。

### 建议刷的新题
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists（LC21），用分治法两两合并或最小堆维护 k 个指针，时间复杂度 O(N log K)。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握知识：Same Tree（LC100）递归比较结构，先序遍历匹配根节点，再递归判断子树是否相同。
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握知识：数组遍历，Kadane 算法维护当前和与最大和，经典贪心/DP 入门，时间 O(n) 空间 O(1)。
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
