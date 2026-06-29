# 🎯 面试复习清单

## 📅 今日复习（2026-06-28）

### 需要回顾
- [ ] **树（Tree）**：Maximum Depth、Same Tree、Invert Binary Tree、Level Order Traversal、Construct from Preorder/Inorder、Validate BST、LCA of BST — **核心：递归是树问题的基础武器；构造类题目利用前序+中序确定根节点位置；验证 BST 用中序遍历+prev 节点判断；LCA 利用 BST 特性比较值大小决定搜索方向。**
- [ ] **链表（Linked List）**：Reverse Linked List、Detect Cycle、Merge Two Sorted Lists、Remove Nth Node From End — **核心：反转链表是基础和面经高频题，推荐头插法；环检测用快慢指针（龟兔赛跑），相遇即有环；合并有序链表用 dummy 哨兵节点简化头节点处理；删除倒数第 n 个节点先走 n 步再同步前进。**
- [ ] **滑动窗口 / 字符串（Sliding Window / String）**：Longest Substring Without Repeating Characters、Minimum Window Substring — **核心：外层 while 扩展右指针，内层 while 收缩左指针直到满足/破坏条件；哈希表记录字符位置或频次；最小覆盖子串需用 require 和 formed 两个计数器来判断窗口合法性，不要通过比较 substring 方式判断。**

### 重点坑
- [ ] **树递归中返回值选 null 还是 subtree**：递归函数需要返回子树结果时，对只有一个子树的节点容易选错返回。关键是明确函数语义：是求最大值？返回 max(左, 右, 当前)；是 LCA？看左右子树的反馈来决定当前是否为 LCA。
- [ ] **链表反转时漏存 next**：反转链表最经典的 bug 就是进入 while 前没保存 `next = cur.next`，导致指针反转后丢失后续链表。标准三步走：暂存 next → 反转指向 → 后移指针。
- [ ] **滑动窗口内外指针混用**：最小覆盖子串等题中，外层右指针前进后忘记移动左指针，或内层 while 退出的判断条件写错，导致死循环或漏解。建议把收缩条件和子串合法性检查打印出来对照题目要求。

### 建议刷的新题
- [ ] **数组 / 哈希表**：Contains Duplicate（Easy）— 关联已掌握知识：Two Sum 的 HashSet 思路，O(n) 判断重复，空间换时间的经典应用。
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 前缀/后缀思想，先算左积再算右积，O(n) 时间 O(1) 额外空间（输出数组不算）。
- [ ] **字符串 / 哈希表**：Valid Anagram（Easy）— 关联已掌握知识：与 Group Anagrams 同根同源，用 26 长度频次数组统计字符次数即可。
- [ ] **图 / DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握知识：Number of Islands 的 DFS/BFS，反向思维从边界海洋向内灌水，找同时能到达两个洋的格子。
- [ ] **链表 / 分治/堆**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists 的扩展，用最小堆维护 k 个指针或分治法递归两两合并，时间复杂度 O(N log K)。

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
