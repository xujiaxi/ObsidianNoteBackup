# 🎯 面试复习清单

## 📅 今日复习（2026-07-30）

### 需要回顾
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End of List（LC19） — **核心：LC206 迭代三指针 `prev/curr/next_temp`——先存 `next_temp = curr.next`、再 `curr.next = prev` 反转、最后 `prev, curr = curr, next_temp` 整体移动；返回 `prev`（新头）。递归版 `head.next.next = head` 从后往前，`head.next = None` 断链。LC141 Floyd 快慢指针——`slow` 走 1 步、`fast` 走 2 步，`slow == fast` 即有环；`while (fast && fast.next)` 防空指针。LC21 拉链合并——Dummy Node 统一头节点逻辑，`while l1 and l2` 比较接小者，剩余 `curr.next = l1 or l2` 直接接上。LC19 快慢指针保持间距 N+1——`fast` 先走 N+1 步、再快慢同走，`slow` 停在被删节点**前驱**，`slow.next = slow.next.next` 删除。**面试口述**：链表题先想「迭代 or 递归」「是否需要 Dummy Node 简化头节点」「快慢指针能解决（找中点/检测环/保持间距）」。**坑：LC206 迭代时 `next_temp` 必须在反转前暂存，否则 `curr.next` 已被改写无法前进；LC141 `fast.next.next` 前必须 `while (fast && fast.next)` 防止尾节点越界；LC19 必须走 N+1 步而非 N 步，否则 `slow` 会停在待删节点本身而非前驱。**
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 双指针法——拆散 starts/ends 分别排序，`while s < len`：`starts[s] >= ends[e]` 则 `used -= 1; e += 1`（腾房），否则 `used += 1; s += 1`，`max_rooms = max(used)`；堆解法——按开始排序，堆存结束时间，`rooms[0] <= start` 则 pop 复用，push 当前 end，`len(rooms)` 即答案。LC348 计分法 O(1) move——放弃存棋盘，用 `rows/cols[2][n]` + `diag[2]` 累计分，玩家1 +1 玩家2 -1，`abs(score) == n` 即胜；主对角 `row == col`、副对角 `row + col == n-1`。LC362 deque 滑动窗口——`hit` 尾部追加 timestamp，`getHits` 用 `while q and q[0] <= timestamp - 300: popleft()` 清理过期，`len(q)` 为结果；进阶用 `[timestamp, count]` pair 合并同秒敲击并维护 `total` 变量。**面试口述**：设计题先问「操作频率」「时空要求」「数据范围」，先给朴素解保底再优化（LC348 O(N) → O(1)，LC362 deque → pair 或二分）。**坑：LC253 `starts[s] >= ends[e]` 用 `>=` 不是 `>`（前一个结束时间 ≤ 当前开始 → 不重叠）；LC348 二维数组必须用 `[[0]*n for _ in range(n)]` 不能 `[[0]*n]*n`（多行共享引用）；±1 计分法而非直接加 player 值（混合棋子会假阳性）；LC362 过期条件 `<=` 不是 `<`（第 301 秒时区间是 [2,301]，第 1 秒数据应清除）；tuple 不可修改，合并计数要用 list `[ts, count]`。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Best Time to Buy and Sell Stock（LC121）、Search in Rotated Sorted Array（LC33）、Find Minimum in Rotated Sorted Array（LC153） — **核心：LC1 一遍哈希——`complement = target - nums[i]`，先查 dict 再存入，天然防自匹配；O(n)/O(n)。LC53 Kadane 空间优化——`prev_max = max(prev_max + nums[i], nums[i])`（延续 vs 重新开始），`ans = max(ans, prev_max)` 用两个变量分开维护。LC121 一次交易——`minPrice = min(minPrice, price)`、`profit = max(profit, price - minPrice)`。LC33 旋转搜索——`while left <= right`，先判断哪半有序 `nums[left] <= nums[mid]`（左有序），再查 target 是否在有序区间，在→收 half，不在→去另一半。LC153 找最小——`while left < right`，与**右边界**比 `nums[mid] > nums[right]` 则最小在右 `left = mid + 1`，否则 `right = mid`（mid 可能就是最小值）；退出返回 `nums[left]`。**面试口述**：二分先确定「找特定值 vs 找极值」→ 前者 `<=` 后者 `<`；旋转数组先找有序半边、再判断 target 归属。**坑：LC53 Kadane 中 `prev_max`（以当前元素结尾的最大和）与 `ans`（全局最大）不能混用一个变量，否则会累加不相邻元素；LC33 `nums[left] <= nums[mid]` 用 `<=` 处理两元素情况（[3,1] 时 left==mid==0）；LC153 用右边界判断而非左边界（左边界有二义性），`right = mid` 不能写成 `mid - 1`（mid 可能就是最小值）。**

### 重点坑
- [ ] **LC206 链表反转「必须先存 next_temp 再做 curr.next = prev」**：顺序错了 `curr.next` 已被改写指向 `prev`，再取 `curr.next` 就回不去了。**正确**：`next_temp = curr.next` → `curr.next = prev` → `prev, curr = curr, next_temp`。迭代返回 `prev`（循环退出时 `curr = None`，`prev` 是新头）。**坑**：递归版 `head.next.next = head` 容易写成 `head.next = head`（自指死循环），且必须 `head.next = None` 断链否则形成环。
- [ ] **LC19 删除倒数第 N「快指针走 N+1 步而非 N 步」**：走 N 步则 `slow` 停在被删节点本身（无法删除，需要前驱）；走 N+1 步则 `slow` 停在被删节点前驱。**坑**：不用 Dummy Node 时删除头节点需单独处理；用 Dummy Node 后 `fast = slow = dummy` 统一逻辑，返回 `dummy.next`。
- [ ] **LC348 Tic-Tac-Toe「直接加 player 值会假阳性」**：如 n=5 第一行玩家2 下两步（+2+2=4）、玩家1 下一步（+1=5），检查 `score == 5*1` 会误判玩家1 胜利但实际只下 3 步没连满。**正确**：±1 计分法，混合棋子正负抵消，只有纯 +1 或纯 -1 累加到 ±n 才真胜。**坑**：二维数组 `[[0]*n]*n` 多行共享同一引用，改一行全变——必须 `[[0]*n for _ in range(n)]`。
- [ ] **LC362 Hit Counter「过期条件用 <= 不是 <」**：第 301 秒查 `getHits(301)` 窗口是 [2,301]，第 1 秒数据应被清除，`timestamp - 300 = 1`，须 `q[0] <= 1` 才触发清除。**坑**：合并同秒敲击时用 tuple `(...)` 会 TypeError（不可修改），必须用 list `[timestamp, count]` 才能 `+= 1`；`total` 变量出入队同步增减是「记账本」，不需要担心被 copy 影响历史。
- [ ] **LC53 Kadane「prev_max 与 ans 不能共用一个变量」**：`ans = max(ans + nums[i], nums[i])` 是错的——`ans` 存的是全局最大值（可能来自不相邻的最优子数组），累加会混合不同子数组。**正确**：`prev_max`（以当前元素结尾的连续和，做状态转移）+ `ans`（全局最大，只取 max）。**坑**：`prev_max + nums[i]` 为正才延续、为负就 `nums[i]` 重新开始，避免负前缀拖累。

### 建议刷的新题
- [ ] **间隔**：Merge Intervals（Medium）— 关联已掌握 LC253 Meeting Rooms II（排序+堆/双指针）。**核心**：按 `start` 排序后线性扫描——`curr.start <= result[-1].end` 则合并 `end = max(end, curr.end)`，否则追加新区间。**坑**：合并时取 `max(end, curr.end)` 而非直接用 `curr.end`（原区间可能更长）；排序用 `Integer.compare` 避免 `a[0]-b[0]` 整数溢出。
- [ ] **数组 & 双指针**：Container With Most Water（Medium）— 关联已掌握 LC19 双指针、LC1 数组遍历。**核心**：左右指针从两端向中间，面积 `= min(h[l], h[r]) * (r - l)`，移动较矮的一侧（保留较高的才有可能增大面积）。**坑**：移动指针后面积可能减小（宽度变窄），但这是必要的——高度受限才要放弃矮边；不能贪心只看宽度。
- [ ] **数组 & 三数之和**：3Sum（Medium）— 关联已掌握 LC1 Two Sum（哈希查 complement）、LC19 双指针。**核心**：排序 + 固定 `nums[i]` + 双指针 `[i+1, n-1]` 找 `= -nums[i]`，找到后左右都跳过 duplicates。**坑**：三层去重——`nums[i] == nums[i-1]` 跳固定数、左右指针各跳相同值；外层 `i` 只到 `n-2`。
- [ ] **堆 / 哈希**：Top K Frequent Elements（Medium）— 关联已掌握 LC253 堆（heapq）、LC1 HashMap。**核心**：Counter 统频次后用大小为 k 的最小堆（堆顶是频次最低的，超出 k 就 pop），最后堆里就是 top k；或桶排序 `bucket[freq] = [nums]` 从高频往低扫。**坑**：最小堆存的是频次最低的元素，`len(heap) > k` 时 `heappop` 弹出最小（也就是被淘汰的那个），保留的是高频。
- [ ] **矩阵**：Set Matrix Zeroes（Medium）— 关联已掌握 LC200 Number of Islands（矩阵遍历 + 原地标记）。**核心**：用第一行/第一列作为标记数组记录该行/列是否有 0，再二次遍历置零；要单独处理 `matrix[0][0]` 的「既是行标记也是列标记」双重身份。**坑**：不能边遍历边置零（会污染后续判断），必须先标记再统一处理；空间 O(1) 靠复用首行首列实现。

## 历史复习记录
- 2026-07-30：链表、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-07-29：树与递归、滑动窗口 & 字符串、动态规划（股票系列）
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
