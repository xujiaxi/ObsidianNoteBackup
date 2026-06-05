# 🎯 面试复习清单

## 📅 今日复习（2026-06-04）

### 需要回顾
- [ ] **图 BFS/DFS** — LC133 克隆图（**BFS/DFS + HashMap 原→克隆重映射，visited 防死循环**）、LC200 岛屿数量（**Sinking Island 沉岛算法，DFS 四方向遍历淹没陆地**）、LC207 课程表（**Kahn's Algorithm BFS 入度表拓扑排序 or DFS 三色标记法环检测**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**右指针扩展直至遇到重复，左指针跳到重复字符后一位，HashSet/HashMap 维护窗口**）、LC76 最小覆盖子串（**通用模板：右扩直到满足全部字符，左缩直到不再满足，记录最小长度时的左右索引**）

### 重点坑
- [ ] **图：LC207 拓扑排序环检测** — Kahn's Algorithm 核心是找到入度为 0 的节点入队，每弹出一个就减少其邻居的入度；如果处理完的节点数 ≠ 总节点数，说明存在环；DFS 三色标记（白/灰/黑）中，遍历到灰色节点即发现 BACK EDGE 表示有环
- [ ] **图：LC200 沉岛边界检查顺序** — 方向数组 `dx = {0,0,1,-1}, dy = {1,-1,0,0}`，遍历邻居时必须**先判断越界再判断值**（`if r<0 || r>=m || c<0 || c>=n || grid[r][c]!='1'`），顺序反了会 NPE
- [ ] **滑动窗口：LC76 needs/window 计数器混淆** — `needs` 存储目标串目标计数，`window` 存储当前窗口实际计数；仅当 `window[c] == needs[c]` 时 `match++`；左侧收缩时 `window[d] == needs[d]` 时 `match--`；容易忘记匹配数增减条件

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握 DFS/BFS（LC200 岛屿），**反向思维从海岸边 DFS/BFS，维护两个可达集合（太平洋 + 大西洋），最后取交集**
- [ ] **图**：[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)（Medium）— 关联已掌握图的连通性思维，**HashSet 存所有数，从序列起点（`num-1` 不在 set 中）开始向后计数，O(n) 时间**
- [ ] **树**：[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)（Hard）— 关联已掌握树遍历（LC102 层序 + LC105 构造），**BFS/DFS 序列化为字符串，反序列化用队列/递归重建；注意处理 null 占位符**
- [ ] **区间**：[Merge Intervals](https://leetcode.com/problems/merge-intervals/)（Medium）— 关联已掌握排序思维，**按 start 排序后遍历，当前 end >= 下一个 start 则合并取最大 end，否则加入结果**
- [ ] **区间**：[Insert Interval](https://leetcode.com/problems/insert-interval/)（Medium）— 关联已掌握 Merge Intervals 思维，**分三段处理：左侧不重叠直接加入 → 合并重叠区间 → 右侧不重叠直接加入**

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
