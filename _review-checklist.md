# 🎯 面试复习清单

## 📅 今日复习（2026-06-08）

### 需要回顾
- [ ] **图 DFS/BFS** — LC133 克隆图（**DFS/BFS 遍历同时用 HashMap<Node, Node> 映射原节点↔克隆节点，避免重复复制**）、LC200 岛屿数量（**沉岛算法：遍历到 '1' 就 DFS 淹成 '0'，cnt++**）、LC207 课程表（**拓扑排序 Kahn's Algorithm：计算入度 → 入度 0 入队 → 出队后减少邻接入度，或在 DFS 中用三色标记法检测环**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**右指针扩展窗口，遇到重复字符收缩左指针直到无重复，用 Set/Map 记录字符位置**）、LC76 最小覆盖子串（**通用模板：外层 while 右移 right 扩展直到覆盖全 t，内层 while 收缩 left 优化，用 HashMap 计数和 need 变量跟踪进度**）

### 重点坑
- [ ] **拓扑排序入度更新别忘了** — Kahn's Algorithm 中，从队列取出节点后，一定要遍历其所有邻接节点并 `indegree[neighbor]--`，入度归零时入队。忘记更新入度会导致死循环或漏判环
- [ ] **滑动窗口 right 和 left 的职责分工** — 外层 `while(right < n)` 只负责右移右指针扩张窗口、加入新字符；内层 `while(满足条件)` 只负责左移左指针收缩窗口、更新结果。不要把收缩逻辑放进外层循环

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握 LC200 岛屿数量，**DFS/BFS 从四条边界向内逆流搜索，标记能流向太平洋/大西洋的格子，取交集**，矩阵 DFS 经典变体
- [ ] **数组**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— 关联已掌握二分查找/数组思维，**Kadane 算法：`maxEndingHere = max(nums[i], nums[i] + maxEndingHere)`，O(n) 贪心**，大厂高频
- [ ] **滑动窗口**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握 LC3+LC76 滑动窗口模板，**窗口内维护最高频字符频次，`windowLen - maxFreq ≤ k` 时可替换，否则收缩左指针**，面试常考变体
- [ ] **图**：[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)（Medium）— 关联已掌握图遍历/集合思维，**HashSet 去重后只找序列起点（`!set.contains(num-1)`），O(n)**，常考
- [ ] **DP 入门**：[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)（Easy）— 关联已掌握树递归思维（LC104 最大深度），**`dp[i] = dp[i-1] + dp[i-2]`，斐波那契递推**，DP 专题第一题，为后续 Coin Change / House Robber 打基础

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

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
