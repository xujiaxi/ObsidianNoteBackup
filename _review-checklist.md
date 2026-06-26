# 🎯 面试复习清单

## 📅 今日复习（2026-06-25）

### 需要回顾
- [ ] **滑动窗口（Sliding Window）**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：外层 while 扩 right，内层 while 满足条件时收缩 left；HashMap 存字符最后出现位置；最小覆盖子串用 need 字典 + formed 计数器判断是否满足条件。**
- [ ] **二分查找（Binary Search）**：Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：与右边界 nums[right] 比较通常更可靠（处理旋转数组最小值）；找特定值 vs 找边界的模板差异；避免 mid = (left + right) // 2 溢出，用 mid = left + (right - left) // 2。**
- [ ] **图论（Graph）**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：DFS 用 visited 集合或三色标记法（白-灰-黑）检测环；拓扑排序用 Kahn's 算法（入度表）；沉岛法做 DFS 原地标记访问过的陆地。**

### 重点坑
- [ ] **旋转排序数组二分查找中，与左边界比较导致死循环** — 与 left 比较时，如果 nums[left] < nums[mid] 无法判断最小值在左半还是右半，推荐与 right 比较（if nums[mid] > nums[right]）
- [ ] **滑动窗口收缩时忘记更新有效窗口计数** — 最小覆盖子串中，每次收缩 left 都要重新检查 formed 条件，不要直接缩小到不满足条件为止再判断；判断"满足"需要当前窗口已经覆盖了所有 required 字符。
- [ ] **Number of Islands 标记 visit 后直接 DFS 不检查合法性** — 先检查边界 `r<0 or r>=m or c<0 or c>=n`，再检查 `grid[r][c] != '1'`，先验后验避免 IndexError；用FAST用 DFS 沉岛法修改 grid 节省额外空间。
- [ ] **图克隆时递归进入死循环** — Clone Graph 必须用 `visited` 字典缓存已克隆的节点；若重复创建新节点会导致无限递归。** 回国功能为了避免这种情况，可以在 DFS 或 BFS 中维护 visited 映射。

### 建议刷的新题
- [ ] **数组 / 前缀和**：Product of Array Except Self（Medium）— 关联已掌握双指针技巧。从左到右先算前缀积，再从右到左遍历算后缀积，两边相乘即答案；O(1) 额外空间（除输出数组）技巧是用 output 数组做前缀积，再用一个变量维护 suffix。
- [ ] **数组 / 双指针**：3Sum（Medium）— 关联已掌握排序 + 双指针先确定一个数，再用双指针找两数之和，跳过重复元素是关键；注意去重时 `i>0 && nums[i]==nums[i-1]` 的判断时机，避免漏解。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握递归思维。经典的斐波那契数列 DP，dp[i] = dp[i-1] + dp[i-2]；注意空间优化到 O(1) 只需两个变量滚动；面试时先写递归式再优化。
- [ ] **字符串**：Valid Anagram（Easy）— 关联已掌握哈希表思维。用长度为 26 的数组统计字符频次，空间 O(1)；也可用 sort 后比较，但数组表法更快。
- [ ] **堆 / TopK**：Top K Frequent Elements（Medium）— 关联已掌握哈希表 + 优先队列。先用 Counter 统计频率，再用 heapq.nlargest(k, counter.items(), key=lambda x: x[1])；或手写大小为 k 的最小堆；注意 Python 的 `heapq` 最小堆默认行为。

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Sliding Window | 2 | `sliding-window/` |
| Design | 2 | `design/` |
| Binary Search | 2 | `binary-search/` |
| Array | 1 | `array/` |
| String | 1 | `string/` |
| Heap | 1 | `heap/` |
| Greedy | 1 | `greedy/` |
| Backtracking | 0 | `backtracking拥有了 backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 calamit  Pointers` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 timeout `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：22 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x旋律] **链表基础** — LC206 + LC141 + LC21 + LC19
