# 🎯 面试复习清单

## 📅 今日复习（2026-05-29）

### 需要回顾
- [ ] **图 DFS/BFS**：LC133 克隆图（**DFS/BFS 深拷贝，HashMap 记录已访问节点避免重复拷贝**）、LC200 岛屿数量（**沉岛算法：DFS 遍历后将 '1' 标记为 '0'，四方向扩散**）、LC207 课程表（**拓扑排序 Kahn 算法：BFS 入度表，入度为 0 入队；DFS 三色标记检测环**）
- [ ] **滑动窗口模板**：LC3 无重复字符最长子串（**右指针扩展，窗口遇到重复字符时收缩左指针直到无重复，maxLen 实时更新**）、LC76 最小覆盖子串（**右指针收集字符，用 need/have 计数器判断是否满足，满足后收缩左指针找最小**）

### 重点坑
- [ ] **图：忘记标记已访问节点** — 克隆图（LC133）中未用 HashMap 记录已克隆节点会导致死循环；岛屿（LC200）中的沉岛标记必须在入栈前完成，否则重复入队爆栈
- [ ] **滑动窗口：收缩时状态更新遗漏** — 左指针移动时，必须同步更新窗口内字符计数和窗口内满足条件的字符数量；**顺序：先更新计数再移动指针，或先移除再判断**
- [ ] **图：拓扑排序入度更新时机** — Kahn 算法中遍历邻居时减入度，入度为 0 才入队；不是一开始把所有节点入队

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握岛屿 DFS（LC200）和图遍历（LC133），**逆向思维：从边界开始 DFS/BFS 标记可达格子，用两集合取交集；面试常考的多源搜索变体**
- [ ] **滑动窗口**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握滑动窗口模板（LC3/LC76），**维护窗口内最高频字符频率 `maxFreq`，`windowLen - maxFreq ≤ k` 时窗口有效；注意 maxFreq 不需要主动减小**
- [ ] **数组**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— 关联已掌握滑动窗口前缀思维，**Kadane 算法：`maxEndingHere = max(num, maxEndingHere + num)`，O(n) 时间 O(1) 空间，面试最常出的 DP 变体之一**
- [ ] **DP 入门**：[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)（Easy）— 关联已掌握分治递归思想（LC104），**Fibonacci 型 DP：`dp[i] = dp[i-1] + dp[i-2]`，空间优化为 O(1)（三个变量滚动），DP 专题第一题**
- [ ] **哈希表/数组**：[Two Sum](https://leetcode.com/problems/two-sum/)（Easy）— 关联已掌握哈希表思维（LC3 窗口查重），**经典 HashMap 一遍遍历：`target - num` 查 map，O(n) 时间，几乎所有面试的暖场题**

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

- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
