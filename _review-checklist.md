# 🎯 面试复习清单

## 📅 今日复习（2026-07-28）

### 需要回顾
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Search in Rotated Sorted Array（LC33）、Find Minimum in Rotated Sorted Array（LC153） — **核心：LC1 一遍哈希表「先查 complement 是否在 dict，再把自己存入」防自匹配，O(n)/O(n)。LC53 Kadane 空间优化版——`prev_max = max(prev_max + nums[i], nums[i])`，**必须用两个变量**（`prev_max` 当前连续和 vs `ans` 全局最大），同变量会累加不相邻元素。LC33 找特定目标用 `while (left <= right)`，mid 切开至少一半有序，先判有序再判 target 是否落在有序区间。LC153 找极值用 `while (left < right)`，**与 `nums[right]` 比较**（左边界有二义性）：`nums[mid] > nums[right]` → `left = mid+1`；否则 `right = mid`（保留 mid 可能就是最小值）。**面试口述**：二分模板分两种——「找目标」用 `<=` + `mid±1`，「找边界/极值」用 `<` + `right = mid`。**
- [ ] **链表**：Reverse Linked List（LC206）、Remove Nth Node From End（LC19）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21） — **核心：LC206 迭代三指针 `prev/curr/next` 每次让 `curr.next = prev`，O(n)/O(1)；递归版 `head.next.next = head` + `head.next = null` 从后往前。LC19 **Dummy + 快慢指针**——快先走 N+1 步（让 slow 停在被删节点前驱），再快慢同走到底；不用 dummy 删头节点要特判。LC141 快慢指针 Floyd——快 2 步慢 1 步，相遇即有环；**坑**：写 `while (fast != null && fast.next != null)` 顺序不能反，先判 fast 非空再判 fast.next。LC21 Dummy 哑节点合并——用 `tail` 指针接较小者，最后把剩余直接接上。**面试口述**：链表题先想「要不要 Dummy」「快慢指针能不能解」「边界是不是要特判」。**
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133） — **核心：LC200 沉岛法——遇 `'1'` → `count++` → DFS 把整岛标 `'0'`，**省 visited 数组**；base case = 越界 + 是水；DFS 求连通分量比 BFS 简洁。LC207 环检测两路：①DFS 三色标记 `0→1(访问中)→2(已完成)`，遇 1 即环，遇 2 剪枝；②BFS Kahn 入度法——入度 0 入队，poll 时后继 `-1`，最终 `count == numCourses` 无环。LC133 HashMap 做「原节点 → 克隆节点」映射，DFS 递归遍历邻居建边。**坑**：LC200 大数据全陆地时 DFS 栈深 = 格子数 → 可能 StackOverflow，改 BFS/迭代 DFS。**面试口述**：图题先建邻接表，再选 DFS（环检测/连通分量）或 BFS（最短路/拓扑排序）；拓扑排序直接把 Kahn 的 poll 顺序记下来就是 Course Schedule II。**

### 重点坑
- [ ] **LC53 Kadane「当前连续和 vs 全局最大不能同变量」**：空间优化版若写 `ans = max(ans + nums[i], nums[i])` 会错——`ans` 存的是全局最大而非当前连续和，累加时把不相邻元素加在一起。必须分两个变量：`prev_max`（dp[i-1] 转移）+ `ans = max(ans, prev_max)`。**坑**：分治法顶层调用要 `divide(0, len(nums) - 1)` 不是 `len(nums)`（越界），右半递归从 `mid+1` 不是 `mid`（无限递归）。
- [ ] **LC33 旋转数组 `nums[left] <= nums[mid]` 的 `<=` 处理两元素 [3,1]**：当 `left == mid`（仅 2 个元素）时，`<` 会漏判左边有序，导致走错分支。**坑**：判断有序用 `<=`，判断 target 落在区间用半开半闭 `[nums[left], nums[mid])`，避免 `nums[mid]` 已确认不等于 target 时仍包含。
- [ ] **LC19 快慢指针「快先走 N+1 步」而非 N 步**：走 N+1 步才能让 `slow` 停在被删节点的前驱；走 N 步 slow 会停在被删节点本身，无法执行 `slow.next = slow.next.next`。**坑**：不用 Dummy Node 时，删除头节点（n == 链表长度）需单独处理——Dummy 让头节点也有前驱，统一逻辑。
- [ ] **LC141 快慢指针 while 条件顺序 `fast != null && fast.next != null`**：先判 `fast` 非空再判 `fast.next`，反了会 NPE。**坑**：快指针初始必须和慢指针同起点（都从 head 出发），写成 `slow = head, fast = head.next` 会让快指针抢跑一步，无环节点会误进入死循环。
- [ ] **LC207 三色标记「状态 2 的剪枝作用」vs 「误把状态 2 当环」**：状态 1 = 当前 DFS 路径上，再次碰见才报环；状态 2 = 该分支已确认无环，再次碰见直接返回 false（剪枝）。**坑**：忘了置 `visited[curr] = 2` 会导致无环节点被重复遍历（虽然结果正确但 TLE）。BFS Kahn 法**不需要 visited 数组**——入度降为 0 才入队，天然防重。
- [ ] **LC200 大数据 DFS StackOverflow**：全陆地时递归深度 = M×N，Java 默认栈可能撑不住。**坑**：被追问时主动提出「改 BFS Queue 避免栈溢出」或「迭代 DFS 显式栈」，体现对内存模型（Stack vs Heap）的理解。

### 建议刷的新题
- [ ] **DP**：House Robber（Easy）— 关联已掌握 LC53 Kadane、LC121/122 股票 DP。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，决策「偷当前 + 隔一个」vs 「不偷当前」。**坑**：只与前两个状态相关，可空间优化到 O(1)（两个变量滚动）。打基础后再推 Robber II 环形版。
- [ ] **DP**：Coin Change（Medium）— 关联已掌握 LC188 状态机思路。**核心**：`dp[i] = min(dp[i], dp[i - coin] + 1)` 凑金额 i 的最少硬币数；初始化 `dp[0]=0`，其余 `INF`。**坑**：`dp` 数组大小是 amount+1 不是 coins 长度；遍历顺序（外金额内硬币 = 组合数，反过来 = 排列数）——本题求最少硬币数不敏感均可用，但 [完全平方数] 类思路需注意。
- [ ] **DP**：Longest Increasing Subsequence（Medium）— 关联已掌握 LC53 最大子数组。**核心**：O(n²) DP `dp[i] = max(dp[j]+1) for j<i 且 nums[j]<nums[i]`；进阶 O(n log n) 二分贪心+`bisect` 维护单调尾数组 `tails`，`bisect_left(tails, x)` 替换。**坑**：DP 状态是「以 i 结尾的 LIS 长度」不是「前 i 个」，最终答案要 max(dp) 不是 dp[n]；O(n log n) 法 `tails` 数组长度是答案但元素未必是真实 LIS。
- [ ] **数组**：Container With Most Water（Medium）— 关联已掌握 LC1 Two Sum、LC19 双指针思路。**核心**：左右双指针向内收缩，每次移动较矮的那边（高度由短板决定，宽度只会变小）；面积 = `min(h[l], h[r]) * (r - l)`。**坑**：不能两边同时缩，必须只动较矮端；相等时两边都能动但答案不变。
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC53 数组遍历技巧。**核心**：不能用除法 → 左右前缀积两遍扫描：先从左累乘存 `out[i] = out[i-1]*nums[i-1]`，再从右用变量 `right` 累乘回乘 `out[i] *= right`。**坑**：第二轮从右扫描时 `right` 要先更新再相乘（或反过来），顺序错了会把本应排除的元素乘进去；O(1) 额外空间（不含输出数组）。
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 Number of Islands、LC207 BFS/DFS。**核心**：从两个大洋边界反向 DFS/BFS，标出「能流到 Pacific」和「能流到 Atlantic」的格子，求交集。**坑**：反向流的条件是「邻居高度 >= 当前」而不是 「<=」——正向水流从高到低，反向则从低回溯到高；每个大洋独立 visited 集合避免互相污染。

## 历史复习记录
- 2026-07-28：数组 & 二分查找、链表、图论 BFS/DFS
- 2026-07-27：树与递归、滑动窗口 & 字符串、间隔题 / 设计题（堆）
- 2026-07-26：链表、图论 BFS/DFS、动态规划（股票系列）
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
**总共 LeetCode 完成：32 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
