# 🎯 面试复习清单

## 📅 今日复习（2026-06-23）

### 需要回顾
- [ ] **图（Graph）**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：DFS/BFS 遍历框架，三色标记法检测环（白/灰/黑），沉岛法将访问过的陆地标记为 '0' 避免重复；Clone Graph 用 HashMap<Node, Node> 记录已克隆节点防环。**
- [ ] **滑动窗口（Sliding Window）**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76） — **核心：外层 while 扩展右指针，内层 while 收缩左指针；维护一个窗口内字符频次的 HashMap；LC76 是最难的滑动窗口变体，用 need/have 两个 map 或 Counter 维护覆盖情况。**
- [ ] **二分查找（Binary Search）**：Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：旋转排序数组中优先和右边界 nums[right] 比较，判断 mid 在哪一半边；注意寻找特定 target vs 寻找边界的模板差异。**

### 重点坑
- [ ] **图 DFS 递归时未标记已访问节点导致死循环 / StackOverflow** — Clone Graph 和 Course Schedule 都必须用 visited / recStack / 染色法防止无限递归；尤其是有向图，不能只在入栈时标记，出栈时也要将 recStack 置灰。
- [ ] **滑动窗口收缩时过度收缩** — 内层 while 的退出条件要仔细确认，不能想当然地收缩到窗口不满足条件为止；Minimum Window Substring 中要在每次满足条件时记录当前最小窗口，而不是等 while 结束后。
- [ ] **旋转排序数组二分查找的边界错** — mid 和 right 比较时，= 的情况别漏掉；如果 nums[mid] == nums[right]，不能确定 mid 在哪半边，只能 right--（最坏 O(n)）。LC153 和 LC33 逻辑有细微差异，别混用。
- [ ] **Minimum Window Substring 中 missing 计数器 vs 实际覆盖混淆** — missing 是还缺多少个字符，窗口每包含一个所需字符就减一，但不能重复计数；需要另一个 map 统计窗口中实际出现次数，再和 need 比较。

### 建议刷的新题
- [ ] **数组 / 双指针**：Three Sum（Medium）— 关联已掌握的双指针/哈希思维（Two Sum 扩展）。**排序后固定一个数，左右指针向中间收。注意去重（i > 0 && nums[i] == nums[i-1]）以及 left/right 指针移动时的去重。**
- [ ] **数组 / 前缀和**：Product of Array Except Self（Medium）— 关联已掌握的数组遍历技巧。**第一遍从左到右算 prefix product，第二遍从右到左算 suffix product，两边相乘得到结果。不能在 O(n) 额外空间內直接用输出数组存储前缀积。**
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握的滑动窗口框架。**维护窗口内每个字符的频率，用 maxFreq 记录窗口中出现最多的字符次数，窗口大小 - maxFreq > k 说明替换不够用，需要收缩。核心是三变量 (left, maxFreq, freqMap)。**
- [ ] **树 / 递归**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握的树递归（LC104/226/105 的递归思维延伸）。**后序遍历，每个节点返回以该节点为端点的最大路径和，全局维护 max 记录任何路径的最大和。注意节点值可能是负数，不能简单取正。**
- [ ] **链表 / 进阶**：Merge K Sorted Lists（Hard）— 关联已掌握的 Merge Two Sorted Lists（LC21）。**优先级队列（MinHeap）维护 K 个链表头，每次取出最小值加入结果；或模拟归并排序逐两两合并。注意堆的比较器写法。**

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
| String | 1 | `string/` |
| Heap | 1 | `heap/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Dynamic Programming | 0 | `dynamic-programming/` |
| Greedy | 0 | `greedy/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：22 题**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表** — LC206 + LC141 + LC21 + LC19
