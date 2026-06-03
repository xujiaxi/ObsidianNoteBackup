# 🎯 面试复习清单

## 📅 今日复习（2026-06-02）

### 需要回顾
- [ ] **图 DFS/BFS** — LC133 克隆图（**BFS/DFS + HashMap 存 clone，visited 判重防死循环**）、LC200 岛屿数量（**沉岛算法，DFS/BFS/并查集三种解法**）、LC207 课程表（**拓扑排序 Kahn 算法 + 邻接表，入度归零，count != numCourses 即有环**）
- [ ] **滑动窗口** — LC3 无重复字符最长子串（**左右指针 + 数组/Set 判重，右移扩张左移收缩**）、LC76 最小覆盖子串（**needMap + haveMap 计数，while have == need 时收缩左指针，记录最短窗口**）

### 重点坑
- [ ] **图：克隆图忘记 visited 检查** — DFS 递归 clone 时，必须先查 HashMap 是否已 clone 过该节点，否则无限递归 StackOverflow；BFS 用 Queue + visited Set 同样处理
- [ ] **图：拓扑排序环检测漏判** — Kahn 算法最后必须比较 processedCount != numCourses；DFS 三色标记（白/灰/黑）不能漏掉回溯时重置颜色的环节
- [ ] **滑动窗口：收缩时忘记更新 needMap 计数** — 收缩左指针时必须 `windowCounts[leftChar]--` 并检查是否满足 need，否则 valid 状态永久为 true 导致结果错误；窗口长度计算用 `right - left + 1` 易混淆，建议统一为 `end - start + 1`

### 建议刷的新题
- [ ] **图**：[Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/)（Medium）— 关联已掌握 DFS（LC200/LC207），**从太平洋和大西洋边界分别 DFS，记录能流到的格子，最后取交集；逆流思维（从海向陆流）是关键**
- [ ] **图**：[Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)（Medium）— 关联已掌握 HashMap+Set 思维（LC133），**HashSet 存所有数，只从没有前驱的数开始统计，O(n) 时间**
- [ ] **滑动窗口**：[Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)（Medium）— 关联已掌握滑动窗口模板（LC3/LC76），**窗口内维护 maxFreq，`窗口长度 - maxFreq ≤ k` 为合法条件，否则收缩左指针**
- [ ] **树**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 关联已掌握树递归（LC104/LC226），**递归判断 p.val == q.val && isSame(p.left, q.left) && isSame(p.right, q.right)；迭代可用 BFS 双队列**
- [ ] **字符串**：[Group Anagrams](https://leetcode.com/problems/group-anagrams/)（Medium）— 关联已掌握 HashMap 计数（LC3/LC76），**排序字符串作为 key 或字符计数数组作为 key；`String.valueOf(count)` 是优雅的实现方式**

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
