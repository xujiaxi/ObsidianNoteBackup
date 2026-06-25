# 🎯 面试复习清单

## 📅 今日复习（2026-06-24）

### 需要回顾
- [ ] **树（Tree）**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）— **核心：递归终止条件（空节点）、后序遍历返回值定义；Invert Tree 要先递归再交换左右子树。**
- [ ] **树（Tree）进阶**：Construct Binary Tree from Preorder and Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235）— **核心：LC105 中序定位根节点、递归构建子树；BST 验证用 long 防止 INT_MIN/INT_MAX 溢出问题。**
- [ ] **链表（Linked List）**：Reverse Linked List（LC206）、Detect Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node（LC19）— **核心：双指针 / 快慢指针框架；反转时注意 prev/curr/next 三指针顺序；Dummy Node 处理头节点删除。**

### 重点坑
- [ ] **BST 验证误用自我身高的 min/max 逻辑** — 不能只看 root.val > left.val && root.val < right.val，整个右子树必须都大于当前节点值；递归时传 (root, min, max) 区间， inflight 用 long。**
- [ ] **链表反转过程中指针丢失** — 必须先保存 next = curr.next，再改 curr.next = prev；顺序反了会导致链表断开，无法继续遍历。**
- [ ] **构造二叉树时 preorder 数组下标越界** — 递归前务必检查 `preorder_start > preorder_end` 或 `inorder_start > inorder_end`；根节点位置由中序 map 决定，注意长度 = end - start + 1。**
- [ ] **Remove Nth Node 快慢指针初始位置** — fast 要先走 n 步；如果链表长度等于 n，fast 会变成 null，此时直接返回 dummy.next 即可（删除头节点）。

### 建议刷的新题
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握的递归思维。**经典的斐波那契数列 DP，dp[i] = dp[i-1] + dp[i-2]；注意空间优化到 O(1) 只用两个变量滚动。**
- [ ] **动态规划**：Coin Change（Medium）— 关联已掌握的数组遍历 + 递归。**完全背包问题入门，dp[amt] = min(dp[amt], dp[amt - coin] + 1)；初始化用 INF + 1 避免溢出；无法凑出时返回 -1。**
- [ ] **数组 / 前缀和**：Product of Array Except Self（Medium）— 关联已掌握的数组遍历技巧。**第一遍从左到右算 prefix product，第二遍从右到左算 suffix product，两边相乘得到结果；可以 O(1) 额外空间（除输出数组外）。**
- [ ] **字符串 / 双指针**：Valid Anagram（Easy）— 关联已掌握的哈希表思维。**用长度为 26 的数组统计字符频次，空间 O(1)；也可以用 sort 后比较，但空间不是最优。**
- [ ] **堆 / TopK**：Top K Frequent Elements（Medium）— 关联已掌握的哈希表 + otaide 数据结构。**先用 Counter 统计频率，再用 heapq.nlargest(k, counter.items(), key=lambda x: x[1])；或手写大小为 k 的最小堆。**

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

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：22 题**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
