# 🎯 面试复习清单

## 📅 今日复习（2026-05-25）

### 需要回顾
- [ ] **图 DFS/BFS**：LC133 克隆图（**DFS 递归 + HashMap 记录已克隆节点**，避免无限递归）、LC200 岛屿数量（沉岛算法：遇到 '1' 则 DFS 沉没整岛，**注意边界检查 + visited 数组或直接修改原数组**）、LC207 课程表（拓扑排序 Kahn 算法：入度数组 + BFS 队列，**检测环：最终入队列的节点数是否等于总节点数**）
- [ ] **二分查找**：LC153 旋转数组最小值（**与右边界 `nums[right]` 比较**，`nums[mid] > nums[right]` → 最小值在右侧，否则在左侧）、LC33 搜索旋转排序数组（先二分找旋转点，再在有序半区二分找目标，或**一次二分判断 target 与 nums[mid] 是否在同一有序半区**）

### 重点坑
- [ ] **图 DFS 递归栈溢出** — 图过大时递归 DFS 可能导致 StackOverflowError，**优先考虑 BFS（队列显式迭代）**，特别是 LC200 岛屿数量在大矩阵时
- [ ] **拓扑排序环检测漏判** — 只检查入度为 0 的节点入队，但**最终要比较入队节点数是否等于 `numCourses`**，否则有环时队列提前空但并非所有节点都被处理
- [ ] **二分查找边界混淆** — 旋转数组最小值用 `nums[mid] > nums[right]` 判断；搜索目标值时用 `if (target >= nums[left] && target < nums[mid])` 判断 target 是否在左半有序区，**两个题模板不同不要混淆**

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握图的 DFS/BFS + 沉岛思维，从边界反向逆流 BFS/DFS，**多源反向遍历经典题**
- [ ] **数组/双指针**：[3Sum](https://leetcode.com/problems/3sum/)（Medium）— 排序 + 双指针 O(n²)，关联二分查找的有序思维，**面经出现率 Top 3**
- [ ] **图/哈希**：[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)（Medium）— HashSet O(n)，关联图连通分量的「连通区间」思维，**最优解与并查集同构**
- [ ] **数组/双指针**：[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)（Medium）— 左右指针贪心收缩短板，关联二分查找的左右边界操控思维
- [ ] **矩阵/回溯**：[Word Search](https://leetcode.com/problems/word-search/)（Medium）— 矩阵 DFS + 回溯（恢复现场），关联图 DFS 遍历 + 岛屿问题的矩阵搜索模式

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
