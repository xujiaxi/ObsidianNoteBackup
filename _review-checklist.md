# 🎯 面试复习清单

## 📅 今日复习（2026-07-25）

### 需要回顾
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：LC3 经典滑动窗口，外层 `while` 扩展右指针 right 前进，内层 `while` 在出现重复字符时收缩左指针 left，期间用 HashSet/HashMap 记录窗口内字符保证 O(n)。LC76 进阶滑动窗口——HashMap 计数目标串 char 频次形成 `need`，遍历 s 时维护 `window` 计数和 `valid` 个数（window 中匹配 need 的字符种类数），合法窗口（valid == need.size）则收缩 left 直到不合法，过程中记录最小长度和起点。**关键模板**：`while right < s.length(): { expand right; while 窗口合法: 更新答案; 收缩 left; }`。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：LC1 HashMap 一次遍历，`map.containsKey(target - nums[i])` 命中返回两 index，O(n)。LC53 Kadane's 算法 `maxSoFar = max(maxSoFar, maxEndingHere += nums[i]); maxEndingHere = Math.max(0, maxEndingHere)`，注意全负数组时要单独累加判断。LC153/LC33 旋转数组二分——**与 nums[right] 比较**（比与 left 更可靠），`nums[mid] > nums[right]` 则最小值在 `[mid+1, right]`；`nums[mid] < nums[right]` 则最小值在 `[left, mid]`。LC33 找特定目标：先判哪半有序，再层层 fall through。**
- [ ] **设计题**：Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362）— **核心：LC348 `n×n` 棋盘，rows[n]、cols[n]、diag、antiDiag 计数，任一维度 `abs(count) == n` 即胜，O(1) 每次 move。LC362 击中计数器——维护 `Queue<Integer>` 时间戳（或 TreeMap/Deque），`hit(t)` 溢出队首 5 分钟以外的旧记录再入队，`getHits(t)` 同样弹出过期再返回队列 size。**坑**：时序空隙必须处理（同一时间戳多次 hit 累加），并发场景常被 follow-up。**

### 重点坑
- [ ] **LC3 滑动窗口收缩时机误判**：典型错误是「**只要出现重复就立即收缩**」，但正确做法应该是「**当窗口内 right 指向字符已存在时才收缩 left 至让其不再重复**」，不能盲目只收缩一格。其次，**收缩时要同步移除HashSet/HashMap 中 left 指向字符**，否则下一轮依旧误判为重复，导致死循环或答案错误。**面试口述**：窗口内状态（此处 HashSet）和指针移动必须成对维护，「先更新数据结构再移动指针」或「先移动指针再更新数据结构」的顺序一旦错乱，next 状态就不一致。
- [ ] **LC153/LC33 二分查找的左/右边界选择与溢出**：旋转数组二分**与 nums[right] 比较比与 nums[left] 比较**更不容易踩坑——与 left 比较时 `[1,2,3,4,5]`（未旋转）和 `[4,5,1,2,3]` 旋转的判断逻辑容易混淆；与 right 比较时统一为「大于右半则最小在右半，小于右半则最小可能在左（含 mid）半」，直观稳定。`mid = (left + right) / 2` **整数溢出**陷阱，必须用 `mid = left + (right - left) / 2`（或 `>>> 1` 无符号位移）。**面试口述**：先讲为什么与 right 比较、再用溢出安全的 mid 公式，体现对细节的敏感度。
- [ ] **LC33 旋转数组「先定位有序半，再 fall through」逻辑顺序**：取 mid 后**第一步先判断 `nums[mid]` 是否就是 target**，否则**第二步判断左半 `[left..mid]` 是否有序**（`nums[left] <= nums[mid]`），有序则看 target 是否落在该半范围内（更新 right 或 left），否则有序的必是右半（更新另一端边界）。**最易错**：把判断「哪半有序」的 `nums[left] <= nums[mid]` 用等号写错，[2,1] 这类小例因子集会绕错；以及忽略循环没终止的边界条件（`left <= right` 必须带等号用于直接命中 target 的场景）。
- [ ] **LC53 Maximum Subarray 的「Kadane's 重置策略」**：`maxEndingHere += nums[i]`，**是否重置**有 variants——若 `maxEndingHere < 0` 即被重置为 0（适合「子数组至少包含一个正数」的弱条件问题），但**全负数组时会错误返回 0**。**正确做法**：要么 `maxSoFar` 初始化为 Integer.MIN_VALUE 且不重置为 0 而是 `Math.max(0, x)`，要么直接用「DP」写法 `dp[i] = Math.max(nums[i], dp[i-1] + nums[i])`。**面试口述**：主动说出这道题有两种主流写法（累加重置 vs DP），并说明全负边界下两种写法的等价性。

### 建议刷的新题
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3/LC76 的滑动窗口模板。**核心**：窗口内允许至多 k 次字符替换，`right` 扩展同时用 `int[26]` 统计窗口内字符频次；`right - left + 1 - maxCount > k` 时收缩 left（maxCount 是窗口内出现最多次的字符频次，不需要在收缩时即时更新 maxCount，因为窗口长度只增不减）。**坑**：maxCount 的「**懒更新**」是经典实现细节——当 left 收缩时 maxCount 不递减，只保留「最大历史值」，因为窗口有效长度只与 maxCount 的上界有关。
- [ ] **数组/双指针**：Container With Most Water（Medium）— 关联已掌握 LC3 双指针 + LC1 数组。**核心**：贪心双指针从两端 i/j 收缩，每次移动较短的一端（`height[i] < height[j]` 移 i），面积 `Math.min(height[i], height[j]) * (j - i)`，**正确性在于较短端继续固定只会让面积更小**。**坑**：心证「移动较长端可能找到更高板」是错的——高取决于短板，宽度反而在缩小；木桶原理贪心证明要能口述。
- [ ] **字符串/双指针**：Valid Palindrome（Easy）— 关联已掌握 LC3/LC76 字符串遍历 + LC141 快慢指针。**核心**：双指针从两端向中间走，跳过非字母数字字符（`Character.isLetterOrDigit`），比较小写化后的字符。**坑**：空串和纯符号串返回 true；不能用 `reverse().equals()` 因为那要 O(n) 空间，双指针 O(1) 空间更优，面试常 follow-up。
- [ ] **堆/优先队列**：Top K Frequent Elements（Medium）— 关联已掌握 LC1 HashMap 计数 + LC253 Meeting Rooms II 的 PriorityQueue 使用。**核心**：先 HashMap 统计频次，再用最小堆维护 size=k（堆顶最小，Poll 超出 k 的）最后剩余即前 k 高频。**坑**：也可用桶排序（`bucket[freq] = list of nums`）O(n) 但空间取决于最大频次；PriorityQueue 的 Comparator 按 value（频次）排序而非 key；`O(n log k)` 堆解法 vs `O(n)` 桶排序解法，面试需口述两种空间 trade-off。
- [ ] **数组/前缀积**：Product of Array Except Self（Medium）— 关联已掌握 LC53 数组遍历 + LC1 巧用辅助空间。**核心**：输出 `res[i] = 左侧所有数之积 × 右侧所有数之积`，两次遍历「先从左累乘（res[i] 是左侧积前缀），再从右累乘（res[i] *= runningRight）」，**禁用除法**。**坑**：O(1) 额外空间除答案数组外——只能用 1 个 runningRight 变量；常见错误是漏掉初始化 `res[0] = 1`，或在第二遍时把 res[i] 直接赋值为右侧积而非 `\*=` 累乘左侧积。

## 历史复习记录
- 2026-07-25：滑动窗口 & 字符串、数组 & 二分查找、设计题
- 2026-07-24：树与递归、图论 BFS/DFS、动态规划（股票系列）
- 2026-07-23：数组 & 二分查找、链表
- 2026-07-22：树与递归、滑动窗口 & 字符串
- 2026-07-20：图论 BFS/DFS、链表
- 2026-07-19：动态规划、数组 & 二分查找
- 2026-07-18：树与递归、图论 BFS/DFS、滑动窗口 & 字符串
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
| Array | 2 | `array/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
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
