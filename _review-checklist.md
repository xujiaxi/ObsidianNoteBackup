# 🎯 面试复习清单

## 📅 今日复习（2026-07-17）

### 需要回顾
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：LC1 用 HashMap边遍历边查（一次遍历），不需要排序；LC121 经典状态 DP（minPrice 滚动、maxProfit 更新），O(n) O(1)；LC53 Kadane 算法——`dp[i] = max(nums[i], dp[i-1]+nums[i])`，注意全负数组时返回的是负数本身；LC153/LC33 旋转数组二分——与 `nums[right]` 比较判定哪 half 有序更可靠，LC33 需先判断 mid 在哪 half，再判断 target 是否落在有序 half，否则缩另一 half。**
- [ ] **链表**（回顾+深化）：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19）— **核心：LC206 三指针法（prev=null, curr, next）每轮反转 1 个指针；LC141 快慢指针（Floyd 龟兔赛跑），相遇即有环，注意 break 后 slow 重置断环；LC21 dummy node 简化头节点，两个指针逐步比较更小的取出；LC19 双指针，快指针先走 n 步再同步走，快到尾时慢指向待删节点的前驱（用 dummy 兜底删头节点）。**

### 重点坑
- [ ] **Maximum Subarray (Kadane) 的全负数组**：很多人初始化 maxSum=0, curSum=0，结果返回 0 是错的——当数组全是负数时最大子数组就是最小的那个负数。正确初始化 `maxSum = nums[0]`、`curSum = nums[0]`，从 index 1 起更新 `curSum = max(nums[i], curSum + nums[i])`。也可以提前先 sort 取最大负数验证。
- [ ] **Remove Nth Node From End 删除头节点的边界**：当 n == 链表长度时 slow=/delete 指针会停在 head，但 fast 走 n 步已到 null，slow 没机会先一步。**必须用 dummy node 让 slow 从 dummy 出发**，这样 slow 停在头节点的前驱，才能正确删除头节点。
- [ ] **Search in Rotated Sorted Array 的 `==` 判定**：比较 mid 与 right 时注意 `nums[mid] == nums[right]` 在本题不会出现（元素不重复），但若改成 Find Minimum II（重复元素）则有陷阱——相等时直接 `right--` 缩边界而不是盲目缩一半。LC33 模板里写 `if (nums[mid] < nums[right]) right = mid`（注意是 mid 不是 mid-1，因为 mid 可能就是答案）。
- [ ] **Floyd 环检测的断环逻辑顺序**：找到环后必须二次走步——slow 回到 head，两指针同速走，相遇点即环入口。常见错误：忘记重置 slow，或先更新指针再判断遇到（应先判断再更新）。

### 建议刷的新题
- [ ] **数组**：Contains Duplicate（Easy）— 关联已掌握 Two Sum（HashMap 计数）。一行 HashSet 搞定，面试中开场热身题；变体题 Contains Duplicate II（k 距离内重复）+ Contains Duplicate III（值差与下标差）一路深入。
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 Two Sum（正向遍历思维）+ Maximum Subarray（前缀区间思想）。**核心：先正向扫累计前缀积 → 再反向扫累计后缀积 → 双扫结果即答案，O(n) O(1)（结果数组不计入辅助空间）**。面试必考，考的是「不使用除法」的巧妙点子。
- [ ] **数组**：Maximum Product Subarray（Medium）— 关联已掌握 Maximum Subarray（Kadane）。**核心变体**：DP 同时维护 max 和 min（因为负负得正），转移时三者取极值：`max[i] = max(num, max[i-1]*num, min[i-1]*num)`、对称同理。
- [ ] **堆**：Top K Frequent Elements（Medium）— 关联已掌握 HashMap 计数（LC1）+ LC253 Meeting Rooms II（堆）。先频率统计再小顶堆求 TopK，桶排序 O(N) 是更优解；和 lc253 双堆思路遥相呼应。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 Validate BST（中序遍历）+ BST 性质。**核心：中序遍历 BST 即遍历升序数组，第 k 个访问到的节点就是答案**。掌握迭代式中序（用栈）可在找到目标后立即停止，比完整中序遍历高效。

## 历史复习记录
- 2026-07-17：数组 & 二分查找、链表
- 2026-07-16：树与递归、图论 BFS/DFS
- 2026-07-15：链表、滑动窗口 & 字符串
- 2026-07-14：数组 & 二分查找、图论 BFS/DFS
- 2026-07-13：树与递归、动态规划
- 2026-07-12：滑动窗口、链表
- 2026-07-11：图论 BFS/DFS、二分查找、数组基础
- 2026-07-07：滑动窗口、链表、树 DFS/BFS
- 2026-07-05：图论 BFS/DFS、二分查找、数组基础
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
| Array | 2 | `array/` |
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

**Blind 75 完成：22 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：31 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
