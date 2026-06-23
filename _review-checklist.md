# 🎯 面试复习清单

## 📅 今日复习（2026-06-22）

### 需要回顾
- [ ] **树**：Maximum Depth of Binary Tree（LC104）、Invert Binary Tree（LC226）、Construct Binary Tree from Preorder and Inorder（LC105）、Lowest Common Ancestor of BST（LC235/LC236） — **核心：递归三要素（终止条件 + 递归逻辑 + 返回值），Invert 是最经典的递归分治+后序遍历，Construct 用 preorder[0] 定位中序根节点再划分子区间，LCA 利用 BST 性质或递归查找；注意 LCA of BST 和 LCA of Binary Tree 的区别。**
- [ ] **链表**：Reverse Linked List（LC206）、Remove Nth Node From End（LC19）、Merge Two Sorted Lists（LC21） — **核心：反转链表用三指针（prev/curr/next），哨兵节点 dummy 统一头尾操作；Remove Nth 快慢指针或先走 n 步再一起动；Merge 用 dummy 头简化边界，尾插法逐个比较。**

### 重点坑
- [ ] **反转链表时未更新 next 指针或丢失后续链表** — 先从 curr.next 保存 nextTemp，再让 curr.next 指向 prev，然后同步移动 prev 和 curr。顺序必须对：先保存 next → 改 curr.next → prev 和 curr 前移。
- [ ] **快慢指针找倒数第 n 个节点时索引差一错** — fast 先走 n+1 步还是 n 步取决于要找的是倒数第 n 个还是第 n+1 个。推荐先让 fast 走 n 步，然后 slow/fast 同步前进，fast 到末尾时 slow 正好在倒数第 n+1 个，便于做删除操作。
- [ ] **Construct Binary Tree 时 preorder 起始索引越界** — 用中序根节点位置计算左子树长度 leftLen = in_root_idx - in_left， preorder 子区间起始是 pre_left + 1，右子树起始是 pre_left + 1 + leftLen，容易算错。写的时候先标清楚各个区间的 [left, right)。
- [ ] **BST LCA 和普通二叉树 LCA 混淆** — BST 可以直接比较 val 决定走左/右子树；普通二叉树不能直接比较，必须两边都递归，看哪边返回 non-null 来决定结果。

### 建议刷的新题
- [ ] **数组 / 前缀和**：Product of Array Except Self（Medium）— 关联已掌握的数组遍历技巧，**从左到右算 prefix product，从右到左算 suffix product，两边相乘得到结果。不能使用除法，且要在 O(n) 完成。**
- [ ] **动态规划 / 入门**：Climbing Stairs（Easy）— 关联递归思维（已掌握的树/链表递归），**斐波那契数列的 DP 写法：dp[i] = dp[i-1] + dp[i-2]，基础DP入门。**
- [ ] **字符串 / 哈希表**：Valid Anagram（Easy）— 关联已掌握的哈希表用法，**用长度为 26 的数组计数或 HashMap 统计字符频率，思路简单但常用于面试热身。**
- [ ] **栈**：Valid Parentheses（Easy）— 关联已掌握的链表/栈操作，**遇到开括号入栈，闭括号检查栈顶匹配。经典面试第一题，考察基础数据结构。**
- [ ] **链表 / 进阶**：Merge K Sorted Lists（Hard）— 关联已掌握的 Merge Two Sorted Lists（LC21），**用 MinHeap（PriorityQueue）维护 K 个头节点，每次弹出最小加入结果；或逐两两合并（复杂度更高）。是 LC21 的直接扩展。**

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Design | 2 | `design/` |
| Array | 1 | `array/` |
| Heap | 1 | `heap/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Dynamic Programming | 0 | `dynamic-programming/` |
| Greedy | 0 | `greedy/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| String | 0 | `string/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：21 题**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC visibly + LC207  + LC inconsiderately
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** —
- [x] **Intervals / 区间** — LC253 会议室 II
- [x] **树** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表** — LC206 + LC141 + LC21 + LC19
