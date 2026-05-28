# 🎯 面试复习清单

## 📅 今日复习（2026-05-27）

### 需要回顾
- [ ] **图 DFS/BFS**：LC133 克隆图（**DFS 递归 + HashMap 缓存已克隆节点**，避免无限循环；也可用 BFS 层克隆）、LC200 岛屿数量（**沉岛算法**：遇到 '1' 计数后 DFS 沉没整个岛屿，注意边界检查 + 防止重复访问）、LC207 课程表（**拓扑排序 Kahn's Algorithm**：入度数组 + BFS 队列，最终比较入队节点数是否等于 `numCourses` 来检测环）
- [ ] **二分查找**：LC153 旋转数组最小值（**与右边界 `nums[right]` 比较**，`nums[mid] > nums[right]` → 最小值在右半，否则在左半；注意数组未旋转的边界情况）、LC33 搜索旋转排序数组（**一次二分**：先判断 `mid` 落在左/右有序半区，再判断 target 是否在该半区内，以此决定收缩方向）

### 重点坑
- [ ] **BFS vs DFS 选用场景混淆** — BFS 适合求最短路径/层级遍历（如克隆图、层序遍历），DFS 适合求全部路径/连通分量（如岛屿数量、排列组合）。**图过大时优先 BFS 避免递归栈溢出；拓扑排序必须用 BFS（Kahn）或后序 DFS 配合 visited 状态检测环**
- [ ] **二分查找死循环 & 边界溢出** — 计算 mid 始终用 `mid = left + (right - left) / 2` 避免 `(left + right)` 整数溢出。旋转数组最小值：`nums[mid] > nums[right]` 时 `left = mid + 1`，否则 `right = mid`（**不要写 `right = mid - 1`，可能跳过最小值**）

### 建议刷的新题
- [ ] **树/DP**：[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)（Hard）— 关联已掌握的树 DFS 遍历（LC104 最大深度）+ 本周 DP 目标，**后序遍历 + 全局最大值，每层返回 `max(left, right) + node.val`，更新全局 `max(left + right + node.val)`**
- [ ] **数组/DP**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— 关联已掌握的滑动窗口维护思维（LC3/LC76）+ 本周 DP 目标，**Kadane 算法：`cur = max(num, cur + num)`，`maxSum = max(maxSum, cur)`，这是最简单的一维 DP 模板**
- [ ] **DP**：[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)（Easy）— 关联已掌握的树分治（LC104 本质也是分治）+ 本周 DP 目标，**Fibonacci 递推 `dp[i] = dp[i-1] + dp[i-2]`，空间可优化为 O(1)，DP 入门第一题**
- [ ] **区间**：[Merge Intervals](https://leetcode.com/problems/merge-intervals/)（Medium）— 按起点排序 + 遍历合并，关联已掌握的排序思维和链表合并（LC21）的**合并重叠区间模板：排完序后，`cur.end >= next.start` 则合并，否则加入结果，高频 Medium**

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
