# 🎯 面试复习清单

## 📅 今日复习（2026-05-23）

### 需要回顾
- [ ] **图 DFS/BFS**：LC133 克隆图（DFS 递归/迭代 BFS + **HashMap 缓存已克隆节点避免循环**）、LC200 岛屿数量（沉岛算法：遇到 '1' 就 DFS 淹没整块陆地并计数 → 递归将 `grid[i][j] = '0'`，**注意检查边界条件 `if (i<0||i>=m||j<0||j>=n||grid[i][j]=='0') return`**）、LC207 课程表（拓扑排序 Kahn 算法：BFS 构建入度表 + 邻接表 → 入度为 0 的节点入队 → 依次出队减邻居入度 → 最后检查是否所有节点都出队，**环检测 = 出队节点数 ≠ 总节点数**）
- [ ] **二分查找**：LC153 旋转数组最小值（**与右边界 `nums[right]` 比较** — 若 `nums[mid] < nums[right]` 则在左侧有序区，收缩右边界；否则在右侧无序区，收缩左边界；循环结束返回 `nums[left]`）、LC33 搜索旋转排序数组（先找最小值分界点 → 确定 target 在左/右半段 → 在有序段做标准二分，**或者一次性二分：判断 mid 在左/右半，再判断 target 位置决定收缩方向**）

### 重点坑
- [ ] **图 DFS visited 遗漏** — LC133 克隆图必须用 HashMap 缓存已克隆节点，否则陷入无限递归。LC200 沉岛后要立即标记 `grid[i][j]='0'`，**否则下次 DFS 又会来一次导致栈溢出。一次性标记**，不要在递归返回后再标记
- [ ] **二分查找边界判断混淆** — LC33 中 `nums[mid] >= nums[left]` 判断 mid 在左半还是右半，容易搞反。**记忆口诀**：`mid >= left` → mid 在左半（有序段是 left~mid）；否则 mid 在右半（有序段是 mid~right）。然后用 `target` 在有序段内再决定收缩方向
- [ ] **LC207 拓扑排序空转处理** — BFS 建图时，如果有节点没有前驱课程但也**没有后继课程**，它们不会被加入邻接表，但仍要从入度表里所有入度为 0 的节点开始。**常见 Bug**：只遍历邻接表的 key 而非所有 0→n-1 节点

### 建议刷的新题
- [ ] **图/DFS**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 从四条边界向内 DFS/BFS，标记能流到太平洋/大西洋的格子，最后取交集。关联已掌握的 LC200 岛屿 DFS 框架，将「沉岛」思维扩展到「从边界反向逆流」，图论边界扩散经典考法
- [ ] **数组/哈希**：[Two Sum](https://leetcode.com/problems/two-sum/)（Easy）— 哈希表存 `(value → index)`，一次遍历查 `target - nums[i]`。关联已掌握的 LC3 滑动窗口 HashMap 用法，是「空间换时间」思维起点，**电面必考**
- [ ] **树遍历**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 同时递归遍历两棵树的每个节点。关联已掌握的树递归框架（LC104 分治 + LC226 翻转），强化「同时遍历多棵树」的比较模式，Quick Win
- [ ] **双指针/容器**：[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)（Medium）— 左右双指针根据高度较短的边向内收缩。关联已掌握的滑动窗口收缩思维（LC3/LC76），将「窗口伸缩」思维迁移到「双指针逼近」，**高频面试题**
- [ ] **链表综合**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 三步法：快慢指针找中点 → 反转后半段 → 交替合并。关联已掌握的 LC206 反转链表 + LC141 快慢指针，链表多操作组合题，**面经 Top 50 常客**

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
