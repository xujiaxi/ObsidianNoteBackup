# 🎯 面试复习清单

## 📅 今日复习（2026-08-05）

### 需要回顾
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 双指针法——starts/ends 分别排序，`starts[s] >= ends[e]` 则腾房 `used -= 1; e += 1`，否则 `used += 1; s += 1`，`max_used` 即答案；堆解法——按开始时间排序，最小堆存结束时间，`heap[0] <= start` 就 pop 复用，否则新开一间，堆大小即所需会议室数。LC348 计分法 O(1) move——不存棋盘，用 `rows/cols[2][n]` + `diag[2]` 累计分：玩家1 +1、玩家2 -1，`abs(score) == n` 即胜；主对角 `row == col`、副对角 `row + col == n - 1`。LC362 deque 滑动窗口——hit 尾部追加 timestamp，getHits 用 `while q and q[0] <= timestamp - 300: popleft()` 清理过期，`len(q)` 即结果；进阶用 `[ts, count]` 合并同秒并维护 total。**面试口述**：设计题先问「操作频率 / 数据范围 / 时空要求」，先给朴素解保底再优化（LC348 棋盘 O(N)→O(1) 计分、LC362 队列→合并计数）；LC253 先答排序+扫描线再提堆。**坑：LC253 `>=` 不是 `>`（结束 ≤ 开始即不重叠可复用）；LC348 二维数组必须 `[[0]*n for _ in range(n)]` 不能 `[[0]*n]*n`（共享引用）；LC362 过期条件 `<=` 不是 `<`（第 301 秒窗口是 [2,301]，第 1 秒数据要清）。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 一遍哈希——`complement = target - nums[i]` 先查 dict 再存入，天然防自匹配；LC53 Kadane——`prev_max = max(prev_max + nums[i], nums[i])`（延续 vs 重新开始），`ans` 单独记全局最大；LC153 与右边界比较——`nums[mid] > nums[right]` 最小值在右半边 `left = mid + 1`，否则 `right = mid`（mid 可能就是最小值），模板 `while left < right`；LC33 任一切口至少一半有序——`nums[left] <= nums[mid]` 判断左半有序、target 在不在其中，再排除另一半，模板 `while left <= right`。**面试口述**：二分先分清「找特定值」（`<=` + 排除）还是「找极值/边界」（`<` + 保留候选）；旋转数组优先与右边界比较，左边界有二义性。**坑：LC53 prev_max 与 ans 必须两个变量分开维护，混用会把不相邻元素加一起（[-2,1,-3,4] 算出 0 而非 4）；LC33 用 `<=`（两元素 [3,1] 时 left==mid）；LC153 `right = mid` 不能写成 `mid - 1`。**
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133） — **核心：LC200 沉岛算法——遇 '1' count++ 后 DFS/BFS 把整座岛置 '0'（原地修改省 visited），base case 先判越界再取值；LC207 双解法——DFS 三色标记（0 未访问 / 1 访问中 → 撞见即环 / 2 已完成 → 剪枝），BFS Kahn 拓扑排序（统计入度，入度 0 入队，出队后继入度 -1，processed == numCourses 即无环）；LC133 HashMap 备忘录——key 原始节点、value 克隆节点，**先入表再递归邻居**，防止环 A→B→A 无限递归。**面试口述**：图题先问「有向/无向」「有无环」「连通分量还是最短路」——连通分量 DFS 简洁、层级/最短路 BFS；矩阵类图邻居靠坐标计算（查越界），图类邻居在 List 里（只有 null 风险）。**坑：LC200 全陆地时 DFS 递归深度 = M×N 可能 StackOverflow（换 BFS）；LC207 Kahn 不需要 visited（入度归 0 才入队天然防重），`int[]` 默认 0 不是 null；LC133 交换「入表」和「递归邻居」的顺序会死循环。**

### 重点坑
- [ ] **LC253 间隔题「结束 ≤ 开始即可复用，用 >= 不是 >」**：双指针法 `starts[s] >= ends[e]` 才腾房——前一个会议恰好同时结束（end == start）不重叠，可以复用同一间；堆解法对应 `heap[0] <= start` 才 pop。**坑**：先按 start 排序是前提，忘记排序双指针法直接错。
- [ ] **LC348 Tic-Tac-Toe「±1 计分法 + 二维数组初始化」**：直接累加 player 值会假阳性——如 n=5 玩家2 走两步（+2+2=4）+ 玩家1 走一步（+1=5），`score == n` 会误判玩家1 胜利但实际没连成线。**正确**：玩家1 +1 / 玩家2 -1，混合棋子正负抵消，只有纯 ±1 累到 ±n 才真胜。**坑**：`[[0]*n]*n` 多行共享同一引用，改一行全变，必须 `[[0]*n for _ in range(n)]`；对角判定 `row == col`（主）、`row + col == n-1`（副）。
- [ ] **LC362 Hit Counter「过期条件 <= 不是 <」**：第 301 秒查询窗口是 [2, 301]，第 1 秒的数据应被清除，`timestamp - 300 = 1`，必须 `q[0] <= 1` 才 popleft。**坑**：合并同秒敲击用 tuple 会 TypeError（不可修改），要用 list `[ts, count]` 才能 `+= 1`；total 随出入队同步增减。
- [ ] **旋转数组二分「与右边界比较 + 两个模板别混」**：LC153 只凭 `nums[mid] > nums[right]` 才 `left = mid + 1`，否则 `right = mid`（mid 可能就是最小值）——「找极值」模板 `while left < right`；LC33 「找目标」模板 `while left <= right`，有序半区判断必须 `nums[left] <= nums[mid]`（`<=` 处理两元素情况）。**坑**：LC153 写 `right = mid - 1` 会把最小值跳过去；LC33 用左边界判断二义性大，右边界更稳。
- [ ] **LC207 三色标记「状态 1 撞见即环、状态 2 剪枝」+ LC133「先入表再递归」**：三色只到 0/1 能判环，但没有状态 2 会重复遍历已确认无环的子树（A→B→C 无环后 D→B 应直接跳过）；Clone Graph 必须 `visited.put(node, clone)` 在 `for (neighbor : node.neighbors)` 之前，顺序反了环 A→B→A 永远查不到备忘录 → 无限递归，HashMap 要做成员变量全局共享。

### 建议刷的新题
- [ ] **间隔**：Insert Interval（Medium）— 关联已掌握 LC253 Meeting Rooms II 区间排序 + 扫描线思维。**核心**：按 start 定位新区间插入点，分三段处理——前面的不重叠区间直接入结果、与新区间重叠的合并（`start = min`、`end = max`）、后面的直接追加；一遍扫描 O(n) 即可，不需要先插入再排序。**坑**：合并时更新 `end = max(end, interval[1])`，别只取新区间自己的 end；注意新区间完全在最前/最后（无重叠）的边界。
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC53 线性遍历 + LC1 空间换时间思维。**核心**：两遍扫描——第一遍从左到右累乘「前缀积」存入答案数组，第二遍从右到左乘「后缀积」；`ans[i] = left[i-1] * right[i+1]`，进阶用输出数组本身把空间压到 O(1)。**坑**：题目禁止用除法（含 0 会全盘出错），必须前缀 × 后缀；i=0 / i=n-1 边界的前后缀初始值为 1。
- [ ] **堆 / 设计**：Find Median from Data Stream（Hard）— 关联已掌握 LC253 最小堆 + LC348/362 设计题「先朴素后优化」的思维。**核心**：双堆法——大顶堆存较小一半、小顶堆存较大一半，保持大小差 ≤ 1，中位数 = 堆顶或两堆顶平均；addNum O(log n)、findMedian O(1)。**坑**：插入后要平衡两堆大小（差超过 1 转移堆顶）；Java 大顶堆用 `Collections.reverseOrder()`，Python 用负数模拟大顶堆。
- [ ] **图论 / 哈希**：Longest Consecutive Sequence（Medium）— 关联已掌握 LC200 连通分量思想 + LC1 Two Sum 哈希表。**核心**：全部数字入 HashSet 后，只从「序列起点」（`num - 1` 不在集合）向后累加计数，保证每个数字最多被访问一次 → O(n)/O(n)。**坑**：必须跳过非起点，否则每个元素都被当起点重复扫描退化成 O(n²)；去重靠 HashSet 天然完成。
- [ ] **数组 / DP**：Maximum Product Subarray（Medium）— 关联已掌握 LC53 Kadane 最大子数组。**核心**：Kadane 变体——负数乘负数变正，要同时维护 `max_so_far` 和 `min_so_far`（当前结尾的最大/最小乘积），`max = max(nums[i], max*nums[i], min*nums[i])`、`min = min(...)`，ans 记全局最大。**坑**：必须双变量——只记最大乘积遇到负号就废（如 [2,3,-2,4]）；更新时要用上一轮的旧值，先存临时变量再赋值。

## 历史复习记录
- 2026-08-05：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-04：动态规划（股票系列）、树与递归、链表
- 2026-08-03：图论 BFS/DFS、间隔 / 设计题（堆）、滑动窗口 & 字符串
- 2026-08-02：树与递归、链表、数组 & 二分查找
- 2026-08-01：图论 BFS/DFS、滑动窗口 & 字符串、动态规划（股票系列）
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
**总共 LeetCode 完成：31 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
