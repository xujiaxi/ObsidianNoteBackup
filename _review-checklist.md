# 🎯 面试复习清单

## 📅 今日复习（2026-06-09）

### 需要回顾
- [ ] **树（递归/构造/BFS）** — LC104 最大深度（**递归：max(depth(left), depth(right)) + 1，O(n)**）、LC226 翻转二叉树（**递归交换左右子树，返回 root**）、LC102 层序遍历（**BFS：用 Queue 按层出队入队**）、LC105 从前序+中序构造二叉树（**前序首元素是根，在中序中找索引切分左右子树，递归构造**）、LC235 BST 最近公共祖先（**利用 BST 大小关系：p,q 同侧递归，分列两侧则返回当前**）
- [ ] **链表** — LC206 反转链表（**迭代：prev=null，依次翻转 next 指针**）、LC141 环形检测（**快慢指针：fast 走2步，slow 走1步，相遇则有环**）、LC21 合并两个有序链表（**Dummy 节点，双指针逐次比较拼接**）、LC19 删除倒数第 N 个节点（**快慢指针：fast 先走 N 步，同时前进，fast 到底时 slow 指向倒数N**）

### 重点坑
- [ ] **二叉树递归返回值别忘处理** — LC105 构造二叉树等递归题中，递归返回后别忘了把左/右子树挂到 root 上（`root.left = build(...)`），否则子树丢失
- [ ] **链表 Dummy 节点的使用时机** — 当操作可能涉及头节点变更（如反转、删除）时，创建 `dummy = ListNode(0)` 可以统一逻辑，最后返回 `dummy.next`

### 建议刷的新题
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握 LC153/LC33 二分查找/数组，**Kadane 贪心：`maxEnding = max(nums[i], maxEnding + nums[i])`**，高频且是 DP 基础
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3+LC76 滑动窗口，**窗口内维护最高频字符，`windowLen - maxFreq ≤ k`，否则收缩左指针**
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿数量，**从四条边界逆流 DFS/BFS，标记能流向太平洋/大西洋的格子，取交集**
- [ ] **DP 入门**：Climbing Stairs（Easy）— 关联已掌握递归/分治思维，**`dp[i] = dp[i-1] + dp[i-2]`，斐波那契递推**，为后续 Coin Change / House Robber 打基础
- [ ] **Trie**：Implement Trie (Prefix Tree)（Medium）— 关联已掌握树结构，**设计类题，TrieNode 包含 children[26] 和 isEnd 标记**，高频系统设计延伸

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

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：20 题**

## 待复习（按优先级）

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
