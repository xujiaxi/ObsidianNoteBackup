# 🎯 面试复习清单

## 📅 今日复习（2026-06-05）

### 需要回顾
- [ ] **树递归/遍历** — LC104 最大深度（**递归 base case null 返回 0，左右子树 max + 1**）、LC226 翻转二叉树（**递归先翻转左右子树再交换**）、LC102 层序遍历（**BFS queue，每层记录当前队列 size**）、LC105 从前序与中序构造二叉树（**前序第一个为根，中序定位根索引，递归构建左右子树**）、LC235 BST 的 LCA（**利用 BST 性质，p<root<q 则 root 为 LCA**）
- [ ] **链表操作** — LC206 反转链表（**迭代三指针 prev/curr/next，递归两种方式**）、LC141 环检测（**快慢指针，相遇即有环**）、LC21 合并两个有序链表（**dummy node + 双指针逐个比较**）、LC19 删除链表倒数第 N 个节点（**dummy node + 快慢指针，快指针先走 n 步**）

### 重点坑
- [ ] **树递归 base case 顺序** — 必须先判 `root == null` 再取值（如 `root.val`），顺序反了直接 NPE；后序遍历中 `int left = maxDepth(root.left)` 之前一定先 check null
- [ ] **链表 dummy node 使用** — LC19 和 LC21 中 `dummy.next = head`，最后返回 `dummy.next`；操作时用 `prev = dummy` 遍历，注意循环结束后 `prev.next` 可能为 null 需要处理
- [ ] **LC102 BFS 层序遍历** — 每层开始时先取 `int size = queue.size()`，用 `for` 循环处理当前层而非 `while(!queue.isEmpty())`，否则找不到分层边界

### 建议刷的新题
- [ ] **树**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 关联已掌握递归遍历（LC104），**同时递归比较两棵树的左右子树：都 null 则 true，一个 null 则 false，值不同则 false**
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握 LCA + BST 性质（LC235），**中序遍历递增 or 递归传 min/max 区间约束每个节点值范围**
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握反转链表（LC206）+ 快慢指针（LC141），**三步法：快慢指针找中點 → 反转后半部分 → 交错合并两个链表**
- [ ] **树**：[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)（Easy/Medium）— 关联 Same Tree + 树遍历，**遍历 s 树的每个节点用 Same Tree 比较是否与 t 相同**
- [ ] **树**：[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)（Hard）— 关联后序遍历（LC104），**后序遍历同时返回「以当前节点为端点的单边最大路径」，全局变量更新「含当前节点的最大路径和」**

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

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：20 题**

## 待复习（按优先级）

- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
