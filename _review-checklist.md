# 🎯 面试复习清单

## 📅 今日复习（2026-06-15）

### 需要回顾
- [ ] **二分查找**：LC153 旋转排序数组最小值 + LC33 搜索旋转排序数组 — **核心：比较 mid 和 right 判断哪半边有序；找最小值时 `nums[mid] > nums[right]` → 最小值在右半；找目标值时先判断哪半边有序，再决定搜索范围**。注意 mid 计算防溢出用 `left + (right - left) / 2`。
- [ ] **图 DFS/BFS**：LC133 克隆图 + LC200 岛屿数量 + LC207 课程表 — **克隆图用 HashMap 做旧节点到新节点的映射，DFS/BFS 复制邻居；岛屿数量用沉岛法（Sinking Island）标记访问；课程表用拓扑排序（Kahn's BFS 或 DFS 三色标记法检测环）**。图问题一定先画邻接关系。
- [ ] **滑动窗口**：LC3 无重复字符最长子串 + LC76 最小覆盖子串 — **通用模板：外层 while 扩展 right，内层 while 不满足条件时收缩 left。LC3 用 HashSet/HashMap 记录字符位置；LC76 用 need[] 计数器 + have/need 统计满足情况，收缩时更新最小窗口**。

### 重点坑
- [ ] **二分查找找错半边** — 旋转数组中判断哪半边有序是 `nums[mid] > nums[right]` 还是 `nums[mid] < nums[right]`，务必想清楚 mid 落在哪一段。找最小值时 `nums[mid] < nums[right]` 说明最小值在左半（含 mid），否则在右半（不含 mid）。
- [ ] **克隆图忘记 clone 邻居** — 递归/迭代时，新节点创建后要记得设置新节点的邻居列表，不能只创建节点不连边。同时要用 visited Map 避免重复克隆。
- [ ] **拓扑排序入度计算错误** — 课程表的图不是直接给的邻接表，要自己构建。注意入度数组初始化为 0，每处理一个节点就将其邻居入度减 1。Kahn 算法终止时如果处理节点数 != 总数说明有环。
- [ ] **滑动窗口收缩时机** — 每次 right 扩展后，先更新状态（频率/count），再用内层 while 检查是否满足条件并收缩 left。收缩时也要同步更新状态。不要先收缩再检查。
- [ ] **LC76 窗口包含条件判断** — 用 `need[256]` 记录需要的字符数，`have` 记录满足 need 的字符种类数。当 `have == needSize` 时才尝试收缩 left。注意字符可能重复，不能简单用 Set。

### 建议刷的新题
- [ ] **数组**：Two Sum（Easy）— 关联已掌握 HashMap / 双指针用法，**用 HashMap 存储 `值→索引` 实现 O(n)**，是面试最经典开场题。
- [ ] **数组**：Maximum Subarray（Medium）— 关联滑动窗口/前缀和思想，**Kadane 算法：维护以当前元素结尾的最大子数组和**，`dp[i] = max(nums[i], dp[i-1] + nums[i])`，空间可优化到 O(1)。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联递归/DP 入门，**`dp[i] = dp[i-1] + dp[i-2]`**，注意边界条件 `dp[0]=1, dp[1]=1`。是理解 DP 状态转移的最佳热身题。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 合并两个有序链表 + 堆/分治，**PriorityQueue 维护 k 个头节点不断 poll/offer，或归并分治合并**。是链表进阶必刷题。
- [ ] **树**：Validate Binary Search Tree（Medium）— 关联已掌握树递归，**递归时传入 min/max 区间约束当前节点值范围**，或者中序遍历验证严格递增。注意不是 `root.val > left && root.val < right`，而是整个子树都在区间内。

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

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：20 题**

## 待复习（按优先级）

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
