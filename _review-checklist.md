# 🎯 面试复习清单

## 📅 今日复习（2026-05-26）

### 需要回顾
- [ ] **树综合**：LC104 最大深度（**分治：`max(left, right) + 1`，不要用遍历思维**）、LC102 层序遍历（BFS 队列，**每层先取 `size` 再出队**）、LC105 构造二叉树（**前序定根，中序分左右，递归构造**）、LC226 翻转（**后序翻转：左右交换再递归**）、LC235 LCA（BST 特性：**同时大于/小于则往对应方向走，否则当前节点即 LCA**）
- [ ] **链表综合**：LC206 反转链表（**三指针 prev/curr/next，防止 next 断裂**）、LC141 环检测（快慢指针，**fast 走两步 slow 走一步，判空：`fast != null && fast.next != null`**）、LC21 合并有序链表（**哨兵节点 + 两两比较、合并后直接接剩余**）、LC19 删除倒数第 N（**快慢指针 + dummy 节点，快指针先走 N 步**）
- [ ] **滑动窗口**：LC3 无重复字符最长子串（**窗口内用 Set/Map 判重，重复时收缩左指针直到不重复**）、LC76 最小覆盖子串（**needMap + haveCount 双计数，满足条件时收缩左指针找最小**）

### 重点坑
- [ ] **树递归栈溢出** — 退化链表场景（如斜树）深度可达 O(n)，递归 DFS 可能 StackOverflow，**考虑用 BFS/迭代栈兜底**
- [ ] **链表反转指针时序** — 三指针必须 `next = curr.next` → `curr.next = prev` → `prev = curr` → `curr = next`，**顺序不能乱，否则链表断裂**
- [ ] **滑动窗口收缩条件混淆** — LC3 有重复时收缩，LC76 当 need 全部满足时收缩。**前者用 Set 判重，后者用计数判包含；注意 LC3 收缩到重复移除才停，LC76 收缩到不满足条件才停，逻辑相反不要搞混**

### 建议刷的新题
- [ ] **树**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 关联已掌握的树 DFS 递归遍历（LC104），**同步遍历两棵树逐节点比较，递归最简实现**
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握的树遍历 + LCA 的 BST 特性，**中序遍历升序 / 递归传递 `(min, max)` 范围**
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— **综合性最强链表中频题**：关联已掌握的快慢指针找中点（LC141）+ 反转链表（LC206）+ 合并链表（LC21），一道题考三个技能
- [ ] **链表**：[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握的合并两个有序链表（LC21），**优先队列 O(n log k) 或分治合并，高频 Hard**
- [ ] **滑动窗口/字符串**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握的滑动窗口模板（LC3/LC76），**窗口内最多替换 k 个字符，核心是 `windowSize - maxFreq <= k`**

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |
| Design | 1 | `design/` |

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：18 题**

## 待复习（按优先级）

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
