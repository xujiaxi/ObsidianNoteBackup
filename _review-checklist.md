# 🎯 面试复习清单

## 📅 今日复习（2026-05-21）

### 需要回顾
- [ ] **图 DFS/BFS**：LC133 克隆图（DFS 递归克隆 + HashMap 缓存已克隆节点，**注意** `visited.containsKey(node)` 优先判断避免无限递归）、LC200 岛屿数量（沉岛算法：遍历网格遇到 '1' → DFS 标记为 '0' → count++，**外层双层 for 嵌套 DFS 的写法是核心模式**）、LC207 课程表（拓扑排序：Kahn's Algorithm BFS 入度表或 DFS 三色标记环检测，**关键是构建邻接表 `List<List<Integer>>` + 入度数组 `int[] indegree`**）
- [ ] **二分查找**：LC153 旋转数组最小值（与右边界 `nums[right]` 比较：`if nums[mid] > nums[right] → left = mid + 1` 最小值在右边；`else → right = mid` 最小值在左边，**mid 与右边界比较比左边界可靠**）、LC33 搜索旋转排序数组（先判哪边有序：`if nums[left] <= nums[mid]` 左边有序 → 判断 target 是否在左侧区间；否则右边有序 → 判断是否在右侧区间）

### 重点坑
- [ ] **图 visited 标记位置** — BFS 入队时立即标记 visited（`visited.add(neighbor); queue.offer(neighbor);`），不要在出队时才标记。否则同一节点被多个邻居入队 → 队列膨胀 → 重复处理 → 死循环或 `OutOfMemoryError`
- [ ] **二分查找 mid 边界** — `mid = left + (right - left) / 2` 必须用此写法防止 `(left + right)` 整数溢出；LC153 中 `while (left < right)` 用 `right = mid`（不 -1）因 mid 可能是最小值，LC33 中 `while (left <= right)` 用 `right = mid - 1` / `left = mid + 1`（精确匹配），**两个模板的 while 条件和 right 赋值不同，混用会死循环**
- [ ] **LC207 入度表与邻接表构建** — 先初始化 `indegree[i] = 0` 和空的邻接表 `graph[i] = new ArrayList<>()`，遍历 `prerequisites` 数组时：`indegree[course]++` 和 `graph[prerequisite].add(course)`。**常见误**：方向弄反 → 拓扑排序结果不对

### 建议刷的新题
- [ ] **图/DFS**：Pacific Atlantic Water Flow（Medium）— 从四条边界分别逆向 DFS，两套 visited 矩阵记录能到达太平洋/大西洋的格子，取交集即可。关联已掌握的 LC200 沉岛算法坐标遍历 + LC133 图 DFS 递归模式，同一套「从边界逆向遍历」思想是高频变体
- [ ] **树/BST**：Validate Binary Search Tree（Medium）— 中序遍历记录 prev，检查是否单调递增；或递归传递 (min, max) 区间约束每个节点值范围。关联已掌握的树递归框架（LC104 分治 + LC235 BST 性质），BST 类题目核心基础，面经必考
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 滑动窗口内维护字符频率，`windowSize - maxFreq <= k` 时收缩左指针，否则扩展右指针取最大窗口。关联已掌握的 LC3 滑动窗口通用模板（`while` 扩展右指针 → `while` 条件收缩左指针），为 LC76 最小覆盖子串再巩固
- [ ] **区间**：Merge Intervals（Medium）— 按 start 排序后遍历：`if (curr.start <= prev.end)` 说明重叠 → 合并；否则加入结果列表。关联已掌握的 LC21 合并有序链表（「当前能否与上一个合并」的思维一脉相承），为 Interval 专题打基础
- [ ] **DP 入门**：House Robber（Medium）— 一维 DP：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，空间可优化为 O(1) 滚动数组。关联已掌握的 LC104 `max(left, right) + 1` 分治递归模式（同一类「取或不取」的 max 决策），DP 专题最佳突破口

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
