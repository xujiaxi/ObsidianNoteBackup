# 🎯 面试复习清单

## 📅 今日复习（2026-08-09）

### 需要回顾
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133） — **核心：LC200 沉岛算法——遍历每个格子，遇到 '1' 就 `count++` 并用 DFS/BFS 把整块岛屿改成 '0'（原地沉岛），避免重复计数；LC207 环检测——拓扑排序 Kahn's Algorithm：统计每个课程入度，入度为 0 的节点入队，逐个出队并减少后继入度，最后处理数 != 课程数则存在环（等价 DFS 三色标记 0/1/2，遇到「灰 = 在递归栈中」即环）；LC133 Clone Graph——BFS + 哈希表「原节点→克隆节点」，先创建克隆节点再补邻居。**面试口述**：图题先问「有向/无向、是否连通、是否需要拓扑序」；「统计数量/连通分量」优先 DFS 沉岛，「层级/最短路径/克隆」优先 BFS。**坑：LC200 必须原地改矩阵；LC207 DFS 版要用三色状态而不是 visited 布尔值，否则漏判环；LC133 BFS 出队时再建克隆会重复建节点。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 一遍哈希——先查 `target - num` 是否已在 map，再存当前值，避免同一元素用两次；LC53 Kadane——`cur = max(num, cur + num)`，`ans = max(ans, cur)`，和为负直接重置；LC153 与右边界比较 `nums[mid] > nums[right]` 则最小值在右半（含 mid+1），否则在左半（含 mid）；LC33 先判断哪半有序——`nums[left] <= nums[mid]` 则左半有序，先查目标是否在有序半内，再决定收缩方向。**面试口述**：二分先确认「单调性在哪个区间成立」；旋转数组题统一与右边界比较更可靠。**坑：`while left < right` 时 mid 取左中位数 `(left+right)//2` 防死循环；LC33 判断有序半用 `<=` 处理边界。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、III（LC123）、IV（LC188）、Cooldown（LC309）、Transaction Fee（LC714） — **核心：股票系列通用状态机——每天两个状态 `hold`（持有）与 `cash`（不持有）：`cash = max(cash, hold + price)`，`hold = max(hold, cash - price)`（用旧 cash 值，防止同日买卖）；LC121 特例只需 `min_price` + `max_profit` 一趟扫描；LC123/188 加交易次数维度 `dp[k][hold/cash]`；LC309 冷冻期需额外记录前一天的卖出状态（`sell_prev`）；LC714 手续费在卖出时扣 `fee`。**面试口述**：股票题先确认「交易次数限制（1 次 / 无限 / k 次）」「能否同日买卖」「有无冷冻期/手续费」，再决定状态维度。**坑：LC121 先更新 min_price 再算 profit；LC188 当 `k >= n//2` 时退化为无限次（贪心累加所有正差价），否则 k 维数组爆炸；LC309 转移用「前一天卖出」状态，别写成当天卖当天买。**重点回顾 LC121：`profit = max(profit, price - min_price)` 与 `min_price = min(min_price, price)` 的顺序。**

### 重点坑
- [ ] **LC200 沉岛「原地修改 + 边界检查顺序」**：DFS/BFS 每访问一个 '1' 立即改成 '0'，否则同一岛屿被重复计数；边界检查 `0 <= r < m and 0 <= c < n` 必须写在递归入口最前面，先取邻居再判界会越界。
- [ ] **二分「与右边界比较 + 左中位数」**：LC153/LC33 统一用 `nums[mid] > nums[right]` 判断旋转点所在半区；`while left < right` 必须用左中位数 `(left+right)//2`，区间长度为 2 时若用右中位数会死循环。
- [ ] **股票 DP「状态更新顺序」**：`cash = max(cash, hold + price)` 必须先于 `hold = max(hold, cash - price)` 执行（用上一轮的 cash），顺序反了等于允许同日买卖；LC121 同理，先更新 `min_price` 再计算 `profit`。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿 BFS/DFS。**核心**：反向思维——从四条边界向陆地 flood fill，太平洋（左上边界）与大西洋（右下边界）各自 BFS/DFS 标记可达集合，两集合交集即能同时流到的格子。**坑**：水流方向判断是「下一格高度 >= 当前格」（水往低处流）；必须从边界出发而不是对每个格子做 DFS，否则 O((mn)²) 超时。
- [ ] **数组**：3Sum（Medium）— 关联已掌握 LC1 Two Sum + 排序。**核心**：排序后固定 `nums[i]`，剩余两数用双指针 `left/right` 找和为 `-nums[i]`，整体 O(n²)。**坑**：去重三连——外层 `i` 跳过重复值、找到一组后 `left/right` 也要跳过重复值，否则结果集重复。
- [ ] **数组**：Container With Most Water（Medium）— 关联已掌握双指针思想（LC121/LC11 同族）。**核心**：左右指针 `l=0, r=n-1`，面积 = `min(h[l], h[r]) * (r-l)`，每次移动高度较矮的一侧。**坑**：移动较高一侧面积只会更小，理解「矮侧必被淘汰」的单调性证明是这题核心，别盲目移动。
- [ ] **数组**：Maximum Product Subarray（Medium）— 关联已掌握 LC53 Kadane 最大子数组。**核心**：维护 `cur_max` 与 `cur_min` 两个状态（负负得正），`cur_max = max(num, num*cur_max, num*cur_min)`，遇到 0 自动重置。**坑**：只维护一个最大值会漏掉「两个负数相乘变正」的情况，必须同时跟踪最小乘积。
- [ ] **动态规划**：House Robber（Medium）— 关联已掌握股票系列状态转移。**核心**：`rob[i] = max(rob[i-1], rob[i-2] + nums[i])`（不抢 vs 抢当前家），滚动两个变量 O(1) 空间。**坑**：初始条件 `rob[0] = nums[0]`、`rob[1] = max(nums[0], nums[1])`；`n = 1` 时要特判，否则越界。

## 历史复习记录
- 2026-08-09：图论 BFS/DFS、数组 & 二分查找、动态规划（股票系列）
- 2026-08-08：链表、树与递归、滑动窗口 & 字符串
- 2026-08-07：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-06：滑动窗口 & 字符串、动态规划（股票系列）、树与递归
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
