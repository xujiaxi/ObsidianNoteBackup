# 🎯 面试复习清单

## 📅 今日复习（2026-06-30）

### 需要回顾
- [ ] **树（Tree）**：Maximum Depth of Binary Tree、Same Tree、Invert Binary Tree、Level Order Traversal、Construct Binary Tree、Validate BST、Lowest Common Ancestor of BST — **核心：递归 vs. 迭代的树遍历；BST 特性利用（左<根<右）；LCA 的两种场景（普通二叉树 vs. BST）；前序+中序重建树的索引映射技巧；反转树的指针交换顺序。**
- [ ] **滑动窗口（Sliding Window）**：Longest Substring Without Repeating Characters、Minimum Window Substring — **核心：通用模板「外层 while 扩展 right，内层 while 收缩 left」；LC3 用 HashMap/数组维护字符最新位置去重；LC76 用 needMap + formed 计数判断窗口是否合法，注意「全包含」和「最小覆盖」的收缩条件。**
- [ ] **链表（Linked List）**：Reverse Linked List、Linked List Cycle、Merge Two Sorted Lists、Remove Nth Node From End — **核心：反转的迭代三指针（prev/curr/next）；快慢指针判环（相遇后慢指针重新从头走）；虚拟头节点简化边界；双指针同步前进合并有序链表。**

### 重点坑
- [ ] **树重建时索引越界**：Construct Binary Tree from Preorder and Inorder 中，用 inorderIndexMap 查根的位置后，左子树长度 = inorderRootIndex - inorderLeft；preorder 的分割是 [preLeft+1, preLeft+1+leftSize) 和 [preLeft+1+leftSize, preRight)，容易把左子树的 preorder 区间算错。
- [ ] **滑动窗口收缩时的 formed 计数维护**：Minimum Window Substring 中，只有当 windowCount[c] == needCount[c] 时才增加 formed；收缩时同样只有相等时才减少。用 `>` 或 `<` 判断会导致 formed 计数失真，漏掉最小窗口。
- [ ] **链表反转时指针丢失**：Reverse Linked List 中，忘记先保存 `next = curr.next` 就修改 `curr.next = prev`，会导致链表断链丢失后续节点。标准三步：存 next → 改指向 → 前移 prev/curr。

### 建议刷的新题
- [ ] **树**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握知识：树的递归后序遍历，当前节点作为「拐点」时路径和 = 左子树最大贡献 + 根值 + 右子树最大贡献，注意负数只选正贡献。
- [ ] **树 / 递归**：Subtree of Another Tree（Easy）— 关联已掌握知识：Same Tree 的扩展，遍历 root 的每个节点作为起点，用 Same Tree 逻辑判断是否匹配 subRoot。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握知识：Tree / 递归的扩展，本质是斐波那契数列，dp[i] = dp[i-1] + dp[i-2]，可优化到 O(1) 空间。
- [ ] **数组 / 前缀和 + 哈希表**：Contains Duplicate（Easy）— 关联已掌握知识：Two Sum 的 HashMap 思想，遍历存 set，O(n) 时间判断重复。
- [ ] **字符串 / 双指针**：Valid Palindrome（Easy）— 关联已掌握知识：链表双指针 + 字符预处理，左右指针向中间逼近，跳过非字母数字字符，不区分大小写比较。

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
