# 🎯 面试复习清单

## 📅 今日复习（2026-06-11）

### 需要回顾
- [ ] **树（递归 / 构造 / 遍历）**：LC104 最大深度、LC226 翻转、LC102 层序、LC105 从前序+中序构造二叉树、LC236/235 LCA — 树递归的 5 种核心场景：深度计算、镜像翻转、层序遍历、前序/中序构造、BST/普通树 LCA。**递归终止条件 + 当前层逻辑 + 递归返回值** 是根本框架，LCA 需区分 BST（利用大小比较）和普通树（后序遍历找 p/q）。
- [ ] **链表（双指针 / 反转 / 合并）**：LC206 反转、LC141 环检测（快慢指针）、LC21 合并有序链表、LC19 删除倒数第 N 个 — **反转时保存 prev/current/next 三步走**；**环检测注意 fast/slow 都从 head 出发，相遇后再将 slow 重置为 head，同速前进找入口**。
- [ ] **设计 / 综合题**：LC348 设计 Tic-Tac-Toe（**行/列/对角线计数，O(1) 判定胜负**）、LC362 设计 Hit Counter（**滑动窗口 + 二分 / 循环队列维护时间戳**）— 高频 系统设计/面向对象 面试题，注意边界和并发。

### 重点坑
- [ ] **树构造递归下标越界** — LC105 用前序+中序构造时，`rootVal` 在中序中的索引 `inIdx` 划分左右子树长度，务必用 `inIdx - inStart` 作为前序左子树长度，递归参数极易错位。
- [ ] **链表反转漏接尾节点** — 反转前保存 `next = cur.next`，再 `cur.next = prev`，然后 `prev = cur; cur = next`，顺序不可颠倒，否则断链。
- [ ] **LCA 普通树 vs BST 混淆** — BST 直接利用 `root.val` 与 `p.val/q.val` 的大小关系剪枝；普通树需递归左右子树查找，后序判断。
- [ ] **滑动窗口收缩漏更新计数** — 收缩 `left` 前，先恢复 `map[s[left]]` 的计数，再 `left++`；`validCount` 只在 `need[c] == have[c]` 时增加，不是每次都会。

### 建议刷的新题
- [ ] **数组**：Two Sum（Easy）— 关联已掌握 HashTable 思维，**`map[target - num]` 一次遍历求补数**，DP/双指针的基础。
- [ ] **DP 入门**：Climbing Stairs（Easy）— 关联已掌握递归/分治思维，**`dp[i] = dp[i-1] + dp[i-2]`，斐波那契递推**，为 Coin Change / House Robber 打基础。
- [ ] **图 / DFS+BFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿数量，**从四条边界逆流 DFS/BFS，标记能流向太平洋/大西洋的格子，取交集**。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3 / LC76 滑动窗口，**窗口内维护最高频字符，`windowLen - maxFreq ≤ k`，否则收缩左指针**
- [ ] **数组双指针**：Container With Most Water（Medium）— 关联已掌握 LC3/LC76 双指针思想，**左右指针向中间收缩，每次移动高度较小的一边**，面试高频经典题。

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
