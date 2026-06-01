# 🎯 面试复习清单

## 📅 今日复习（2026-05-31）

### 需要回顾
- [ ] **图 DFS/BFS** — LC133 克隆图（**DFS 递归 / BFS 队列 + HashMap<原节点, 拷贝> 防重复**）、LC200 岛屿数量（**沉岛：遇到 1 就 DFS/BFS 沉掉整块，计数++**）、LC207 课程表（**拓扑排序：Kahn BFS 入度表 / DFS 三色标记检测环**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**ASCII 频次数组 + 右扩左缩，左边频次>1 时持续收缩**）、LC76 最小覆盖子串（**计数数组 + valid 变量跟踪匹配进度，窗口满足条件后收缩左边界记录结果**）
- [ ] **二分查找** — LC153 旋转数组最小值（**与 nums[right] 比较，中 > 右则最小值在右半，否则左半**）、LC33 搜索旋转排序数组（**先定 mid 在左/右半，再判 target 位置，二分搜索**）

### 重点坑
- [ ] **图：DFS 克隆图栈溢出** — 深拷贝用 BFS 更安全，DFS 递归深度可能随图变大爆栈；拓扑排序 Kahn 算法必须正确维护入度表，队列中所有入度变 0 的节点都要入队
- [ ] **滑动窗口：收缩条件写错** — LC76 必须用 valid 计数变量跟踪 t 中字符种类是否全部覆盖，不要直接用窗口频次与 t 频次逐字符比较（O(n·m)）；LC3 右移左指针时频次数组别忘了减 1
- [ ] **二分查找：旋转数组边界混乱** — 与右边界 nums[right] 比较比左边界更可靠；LC33 先判 mid 落在左半（nums[mid] >= nums[left]）还是右半，再决定 target 在哪一侧

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握 DFS/BFS（LC200 岛屿），**反向思维：从太平洋/大西洋边界出发 DFS/BFS 向中心搜索，取交集即可；标记两个布尔矩阵而非沉岛，避免状态冲突；面试高频**
- [ ] **滑动窗口/字符串**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握滑动窗口（LC3/LC76），**滑动窗口 + 字符频率统计 + `窗口长度 - 最高频次 ≤ k` 决定收缩；易错：maxFreq 只需和当前字符频率比较即可，不需要扫全表**
- [ ] **数组**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— 关联已掌握二分查找，**经典 Kadane 算法 O(n)：dp[i] = max(nums[i], dp[i-1] + nums[i])；同时也支持分治 O(n log n)，面试 follow-up 常问**
- [ ] **图**：[Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)（Medium）— 关联已掌握 DFS/BFS（LC200 岛屿）和并查集，**DFS 遍历/Union-Find 两种实现都要会；与 LC200 岛屿本质 identical，只是变到图表示**
- [ ] **数组**：[Two Sum](https://leetcode.com/problems/two-sum/)（Easy）— **最佳 warm-up 题，HashMap 一 pass：存值到下标映射，每步检查 target - nums[i] 是否已在 map 中；面试天天见，必须 2 分钟内写完无 bug**

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
