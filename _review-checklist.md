# 🎯 面试复习清单

## 📅 今日复习（2026-06-10）

### 需要回顾
- [ ] **图（DFS/BFS/拓扑排序）** — LC133 克隆图（**DFS/HashMap：visited 映射原节点→克隆节点，递归克隆邻居**）、LC200 岛屿数量（**DFS 沉岛法：grid[i][j]=='1' 时 mark 为 '0'，递归四周**）、LC207 课程表（**拓扑排序：入度表 + Kahn BFS，处理有向图环检测**）
- [ ] **二分查找（旋转数组）** — LC153 寻找旋转数组最小值（**与右边界比较：`if nums[mid] > nums[right]` 最小值在右半，`left = mid+1`，否则 `right = mid`**）、LC33 搜索旋转排序数组（**先判断 mid 在左半/右半段，再针对性收缩**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**外层扩展 right，内层 `while` 遇重复收缩 left**，用 HashSet 维护窗口）、LC76 最小覆盖子串（**HashMap 计数 + count 维护有效字符，窗口满足时收缩 left 找最短子串**）

### 重点坑
- [ ] **二分查找边界处理** — LC153 搜索最小值时，和 `nums[right]` 比较；LC33 搜索目标值时，每次先判断 `nums[mid]` 在左半段还是右半段，再决定哪半边缩
- [ ] **BFS 拓扑排序入度更新** — Kahn 算法每出队一个节点，将其邻接点入度 -1，入度归零时才进队；别忘了单独处理所以没有先修课（入度为0）的课程
- [ ] **滑动窗口 HashMap 计数失效** — 收缩 left 前，先恢复 map[s[left]] 的计数，再右移 left；另外 `validCount` 只在 `need[c] == have[c]` 时增加，不是每次都会

### 建议刷的新题
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握 LC153/LC33 二分查找/数组，**Kadane 贪心：`maxEnding = max(nums[i], maxEnding + nums[i])`**，高频且是 DP 基础
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3+LC76 滑动窗口，**窗口内维护最高频字符，`windowLen - maxFreq ≤ k`，否则收缩左指针**
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿数量，**从四条边界逆流 DFS/BFS，标记能流向太平洋/大西洋的格子，取交集**
- [ ] **DP 入门**：Climbing Stairs（Easy）— 关联已掌握递归/分治思维，**`dp[i] = dp[i-1] + dp[i-2]`，斐波那契递推**，为后续 Coin Change / House Robber 打基础
- [ ] **数组双指针**：Container With Most Water（Medium）— 关联已掌握 LC3/LC76 双指针/滑动窗口思想，**左右指针向中间收缩，每次移动高度较小的一边**，面试高频经典题

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
