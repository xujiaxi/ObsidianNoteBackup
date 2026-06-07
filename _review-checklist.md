# 🎯 面试复习清单

## 📅 今日复习（2026-06-06）

### 需要回顾
- [ ] **图 DFS/BFS** — LC133 克隆图（**DFS/BFS 用 HashMap 存新旧节点映射，先创建新节点再递归邻居，避免环中无限递归**）、LC200 岛屿数量（**沉岛算法：遍历到 '1' 时 count++ 并 DFS 沉掉整个岛屿**）、LC207 课程表（**拓扑排序：Kahn 算法计算入度，BFS 从入度 0 开始逐层移除**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**双指针 + HashSet/数组，右指针扩展，遇到重复则收缩左指针直到无重复**）、LC76 最小覆盖子串（**双指针 + 计数数组，先扩展右指针到覆盖所有 t，再收缩左指针找最优解**）
- [ ] **二分查找** — LC153 旋转数组最小值（**与右边界 `nums[right]` 比较，`while(left < right)` 模板，不要求找 target**）、LC33 搜索旋转排序数组（**先判断 mid 在左段还是右段，再根据 target 范围缩小区间**）

### 重点坑
- [ ] **图 DFS 克隆图顺序** — 克隆图时必须先 `map.put(node, new Node(node.val))` 再加入 map，再递归处理邻居 neighbors，否则在环状图中会因重复 dfs 同一节点而无限递归，导致 StackOverflowError
- [ ] **滑动窗口收缩条件** — 窗口满足条件后（如 LC76 count == tLen），收缩左指针时先更新结果再移动左指针，且左指针移出窗口后要恢复计数（`sCount[sChar[left]]--`），注意左右指针的边界处理
- [ ] **二分查找旋转数组边界选择** — 与右边界 `nums[right]` 比较比左边界更可靠；找最小值用 `while(left < right)` 模板避免死循环，`left = mid + 1` / `right = mid` 的移动规则需熟记

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握图 DFS（LC200），**反向思维：从四条边界分别向内地 DFS，标记能流入 Pacific 和 Atlantic 的格子，最后求交集**
- [ ] **图/数组**：[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)（Medium）— 关联已掌握图遍历（LC200），**用 HashSet 去重，只从 `num-1` 不在集合中的数开始计数**，哈希表思维
- [ ] **数组**：[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)（Medium）— 关联已掌握二分查找模式（LC153），**Kadane 算法 O(n)：`maxEndingHere = max(nums[i], maxEndingHere + nums[i])`**，经典 DP 入门
- [ ] **字符串**：[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)（Easy）— 关联已掌握栈数据结构（BFS 层序使用 queue），**栈匹配括号：左括号 push，右括号检查栈顶是否匹配，最后栈空则有效**
- [ ] **树**：[Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)（Medium）— 关联已掌握 BST 性质 + LCA（LC235），**中序遍历 BST 递增，第 k 个访问的节点即为答案**，可用迭代栈实现

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
