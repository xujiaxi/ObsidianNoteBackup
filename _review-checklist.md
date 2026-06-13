# 🎯 面试复习清单

## 📅 今日复习（2026-06-12）

### 需要回顾
- [ ] **二分查找（旋转数组 / 变种）**：LC153 旋转排序数组最小值、LC33 搜索旋转排序数组 — ** rotated sorted array 核心是与右边界 `nums[right]` 比较**，`nums[mid] > nums[right]` 说明最小值在右半，`mid < right` 则最小值在左半（含 mid）。搜索时同样先判断哪半边有序，再在有序侧用常规二分。牢记 **不要和 `nums[left]` 比**（容易误判）。
- [ ] **图（DFS/BFS / 拓扑排序）**：LC133 克隆图、LC200 岛屿数量、LC207 课程表 — 图的三种经典考法：**克隆图用「旧→新」HashMap 避免重复克隆 + DFS/BFS 遍历邻居**；**岛屿数量用「沉岛法」DFS/BFS 标记访问过为 '0'**；**课程表用 Kahn 算法（入度表 + 队列）或 DFS 三色标记（0=未访问, 1=访问中, 2=已完成）检测环，拓扑排序输出顺序**。
- [ ] **滑动窗口（变长 / 定长）**：LC3 无重复字符最长子串、LC76 最小覆盖子串 — 通用模板：**外层鸡毛掸开 right，满足条件时用内 while 缩 left**。LC3 用 HashSet 判断重复，`right` 进，`left` 滑到无重复；LC76 用 HashMap 维护 need/have 计数，`validCount == need.size()` 时尝试收缩左边界，**注意先恢复 `have[s[left]]` 再 `left++`**。

### 重点坑
- [ ] **二分查找 mid 溢出问题** — `mid = left + (right - left) / 2`，不要用 `(left + right) / 2`。旋转数组搜索时，先判断 `nums[mid]` 与 `nums[right]` 关系，不要和 `nums[left]` 比。
- [ ] **克隆图忘记标记 visited（旧→新映射）** — 克隆时先放入 HashMap 再递归邻居，否则同一个节点会被克隆多次，形成循环引用或遗漏边。
- [ ] **课程表 DFS 三色标记返回值处理** — 遇到 `state == 1`（灰）说明有环，返回 false；但 DFS 函数返回后要注意**短路处理**，只要一个邻接点有环就整体有环，不要继续遍历。
- [ ] **滑动窗口收缩时漏恢复计数** — 收缩 `left` 前，先 `have[s[left]]--`，再判断 `have[s[left]] < need[s[left]]` 才减 `validCount`，顺序和条件都不能错。
- [ ] **链表反转断链 / 快慢指针初始化** — 反转时保存 `next = cur.next` 再改 `cur.next = prev`；环检测 fast/slow 都从 head 出发，相遇后 slow 重置 head 同速找入口。

### 建议刷的新题
- [煲汤] **数组**：Two Sum（Easy）— 关联已掌握 HashTable 思维，**`map[target - num]` 一次遍历求补数**，面试最经典的 warm-up 题。
- [ ] **DP 入门**：Climbing Stairs（Easy）— 关联已掌握递归/分治思维，**`dp[i] = dp[i-1] + dp[i-2]`，斐波那契递推**，为 Coin Change / House Robber 打基础。
- [ ] **数组双指针**：Container With Most Water（Medium）— 关联已掌握双指针思想，**左右指针向中间收缩，每次移动高度较小的一边**，面试高频面积/贪心题。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3 / LC76 滑动窗口，**窗口内维护最高频字符，`windowLen - maxFreq ≤ k`，否则收缩左指针**。
- [ ] **图 / DFS+BFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿数量，**从四条边界逆流 DFS/BFS，标记能流向太平洋/大西洋的格子，取交集**。

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

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
