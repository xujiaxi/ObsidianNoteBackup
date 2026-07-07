# 🎯 面试复习清单

## 📅 今日复习（2026-07-05）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph、Course Schedule、Number of Islands — **核心：图的克隆用 HashMap 映射旧节点到新节点；Course Schedule 用入度表 Kahn 算法或三色标记法检测环；Number of Islands 沉岛法（将 '1' 标记为 '0'）避免重复访问。**
- [ ] **二分查找**：Find Minimum in Rotated Sorted Array、Search in Rotated Sorted Array — **核心：旋转排序数组中与右边界 `nums[right]` 比较更可靠，判断哪半段有序；找最小值时 mid 与 right 比，找目标值时先判断有序半段再二分。**
- [ ] **数组基础**：Two Sum、Best Time to Buy and Sell Stock — **核心：Two Sum 用 HashMap 存已遍历元素，空间换时间 O(N)；股票一次交易最小值买入最大值卖出，遍历维护 minPrice 和 maxProfit。**

### 重点坑
- [ ] **二分查找边界条件**：while(left <= right) 还是 while(left < right)？返回 left 还是 right？旋转数组中点偏移一格导致死循环，务必手写模板并测试。
- [ ] **图的克隆中遗漏邻居**：Clone Graph 遍历邻居时既要创建邻居节点也要建立双向连接，别忘了 `newNode.neighbors.add(...)` 的双向处理。
- [ ] **Course Schedule 忽略有向边方向**：入度出度方向搞反会导致拓扑排序结果错误，建图时确认清楚 `adj[u].push(v)` 的方向性。
- [ ] **滑动窗口收缩后忘记同步更新**：收缩左指针后，`window[c]` 减少后如果 `window[c] < need[c]`，必须 `valid--`。漏掉会导致 valid 虚高，窗口不满足条件。
- [ ] **Java Integer 比较**：务必用 `.equals()`，而非 `==`，因为超过 Integer Cache (-128~127) 会缓存未命中导致错误。

### 建议刷的新题
- [ ] **树 / 递归遍历**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握知识：树 DFS + 后序遍历。递归返回以当前节点为端点的最大路径和，全局维护 maxSum，注意「路径」不能分叉，返回值取 `max(left, right, 0) + node.val`。
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 双指针。先用左遍历求左侧乘积，再反向遍历用右侧乘积乘入；常数空间 O(1) 的输出空间解法。
- [ ] **链表 / 分治+优先队列**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists + 堆操作。最小堆维护 K 个链表头，每次 pop 最小值并将 next 推入堆。时间 O(N log K)。
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板。窗口内允许替换 k 次使字符相同，维护 maxFreq，当 `right-left+1-maxFreq > k` 时收缩 left。
- [ ] **数组 / 双指针+排序**：3Sum（Medium）— 关联已掌握知识：Two Sum + 排序 + 双指针去重。排序后固定一个数，双指针在右侧找两数之和为 target 的补数；注意跳过重复元素避免结果重复。

## 历史复习记录
- 2026-07-04：树与递归、链表、动态规划入门 — 股票系列
- 2026-07-03：数组 & 二分查找、图论 BFS/DFS、字符串 & 滑动窗口

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |
| Greedy | 1 | `greedy/` |
| Heap | 1 | `heap/` |
| String | 1 | `string/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation |  Bella | `bit-manipulation/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：20 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **数组基础** — LC1 + LC121
