# 🎯 面试复习清单

## 📅 今日复习（2026-05-24）

### 需要回顾
- [ ] **链表综合**：LC206 反转链表（`prev/curr/next` 三指针迭代 + 递归）、LC141 环检测（快慢指针，**相遇后找入口：慢指针重置到头，快慢同速走，再次相遇即入口**）、LC21 合并有序链表（哨兵节点 + 递归）、LC19 删除倒数第 N 个（快指针先走 N 步，慢指针与快指针同步走，**注意 dummy 节点处理头节点删除**）
- [ ] **树分治/构造**：LC104 最大深度（分治 `max(maxDepth(left), maxDepth(right)) + 1`）、LC226 翻转二叉树（递归 swap 左右子树）、LC102 层序遍历（BFS 队列，**每层提前记录 queue.size() 作为本层循环次数**）、LC105 构造二叉树（preorder[0] 为根 → inorder 定位左右子树大小 → 递归构造，**注意传入 preorder/inorder 的索引偏移量**）、LC235 BST 的 LCA（利用 BST 大小关系 O(h)：`p.val < root.val && q.val < root.val` → left；`p.val > root.val && q.val > root.val` → right；否则 root 即为 LCA）

### 重点坑
- [ ] **链表反转指针丢失** — `next = curr.next` 必须在 `curr.next = prev` **之前**保存，顺序一错就断链。递归版要记得返回新头节点（原尾节点）
- [ ] **树构造题索引偏移** — LC105 用 inorder 中根节点的位置（`int rootIndex = inorderMap.get(preorder[preStart])`）计算左子树大小（`int leftSize = rootIndex - inStart`），然后 preorder 的 `preStart` 和 inorder 的 `inStart/inEnd` 都要同步偏移，**最容易 off-by-one**
- [ ] **BST vs 普通二叉树 LCA 混淆** — BST 的 LCA 用大小关系 O(h) 解决；普通二叉树（LC236）需要后序遍历回溯，`if (root == null || root == p || root == q) return root`，**两种题解法不同，面试时先确认有没有 BST 性质**

### 建议刷的新题
- [ ] **链表**：[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握 LC21 合并两个有序链表，扩展到 K 个用优先队列 O(n log k) 或分治归并，**面试常考 Follow-up**
- [ ] **树/验证**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握树递归框架 + BST LCA，用** min/max 边界递归**（`isValid(root, null, null)` 逐层传递允许范围）或中序遍历递增检查
- [ ] **树/路径**：[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)（Hard）— 关联已掌握 LC104 最大深度分治模式，后序遍历 + **全局变量跟踪最大路径**，每个节点返回 `max(left, right) + root.val`（负值截断为 0），**后序遍历 Hard 签到题**
- [ ] **滑动窗口**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握 LC3/LC76 滑动窗口通用模板，将窗口收缩条件从「无重复」变为「窗口大小 - 最多字符频次 ≤ k」，**滑动窗口最频繁扩展题型**
- [ ] **数组/子数组**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— Kadane 算法（维护 `currMax = max(nums[i], currMax + nums[i])`，全局 `maxSum = max(maxSum, currMax)`），O(n) 贪心，**面经出现率 Top 5**，关联已掌握二分查找思维转向 DP/贪心模式

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）

## 待复习（按优先级）

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
