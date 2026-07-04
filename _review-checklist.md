# 🎯 面试复习清单

## 📅 今日复习（2026-07-03）

### 需要回顾
- [ ] **数组 & 二分查找（Array & Binary Search）**：Best Time to Buy and Sell Stock、Find Minimum in Rotated Sorted Array、Search in Rotated Sorted Array — **核心：买卖股票维护 minPrice + maxProfit；旋转排序数组二分搜索时与右边界比较更可靠，`if nums[mid] < nums[right]: right = mid` 否则 `left = mid + 1`。**
- [ ] **图论 BFS/DFS（Graph）**：Clone Graph、Course Schedule、Number of Islands — **核心：深拷贝维护 visited map（Node → Clone）；拓扑排序 Kahn 算法入度表 + BFS；岛屿问题用沉岛法原地 mark。**
- [ ] **字符串 & 滑动窗口（Strings & Sliding Window）**：Longest Substring Without Repeating Characters、Minimum Window Substring — **核心：滑动窗口模板——外层 while 扩展右指针，内层 while 收缩左指针；最小覆盖子串维护 need 字典和 valid 计数。**

### 重点坑
- [ ] **二分查找边界条件**：`while (left < right)` vs `while (left <= right)` 容易混淆。查找最小值时与 `nums[right]` 比较通常比 `nums[left]` 更可靠；注意终止时返回 `left` 还是 `right`。
- [ ] **图克隆/深拷贝时修改原节点**：使用 `HashMap<Node, Node>` 维护原节点到新节点的映射，绝不要直接返回原节点或修改原节点的 neighbors。
- [ ] **滑动窗口收缩后忘记同步更新**：收缩左指针后，`window[c]` 减少后如果 `window[c] < need[c]`，必须 `valid--`。漏掉会导致 valid 虚高，窗口不满足条件。
- [ ] **Java Integer 比较**：务必用 `.equals()`，而非 `==`，因为超过 Integer Cache (-128~127) 会缓存未命中导致错误。

### 建议刷的新题
- [ ] **数组 / Kadane 算法**：Maximum Subarray（Medium）— 关联已掌握知识：数组遍历 + 动态规划入门。`dp[i]` 表示以 i 结尾的最大子数组和，转移 `dp[i] = max(nums[i], dp[i-1] + nums[i])`；空间可优化至 O(1)。
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历 + 双指针。先用左遍历求左侧乘积，再反向遍历用右侧乘积乘入；常数空间 O(1) 的输出空间解法。
- [ ] **链表 / 分治+优先队列**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists + 堆操作。最小堆维护 K 个链表头，每次 pop 最小值并将 next 推入堆。时间 O(N log K)。
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板。窗口内允许替换 k 次使字符相同，维护 maxFreq，当 `right-left+1-maxFreq > k` 时收缩 left。
- [ ] **树 / 递归**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握知识：树 DFS + 后序遍历。递归返回以当前节点为端点的最大路径和，全局维护 maxSum，注意「路径」不能分叉，返回值取 `max(left, right, 0) + node.val`。

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
| Bit Manipulation | 0 | `bit-manipulation/` |
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
