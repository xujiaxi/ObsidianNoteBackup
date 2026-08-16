# 🎯 面试复习清单

## 📅 今日复习（2026-08-15）

### 需要回顾
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、II（LC122）、III（LC123）、IV（LC188）、Cooldown（LC309）、Transaction Fee（LC714） — **核心：LC121 一次交易——遍历时先更新 `minPrice` 再算 `profit = price - minPrice`，取最大。LC122 无限次交易——贪心：只要 `prices[i] > prices[i-1]` 就累加差价，无需找极值点。LC123/LC188 有限次交易——状态机 DP：`buy[k]`/`sell[k]` 双数组，先更新 buy 再更新 sell。LC309 冷冻期——三状态机（hold/sold/rest），卖出后必须隔一天才能再买。LC714 手续费——卖出时收益减 `fee`。**面试口述**：先确认「交易次数限制」，1 次 → 贪心维护 minPrice；无限次 → 累加正差价；有限 k 次 → 状态机。**坑：LC121 必须先更新 minPrice 再算 profit，顺序反了会算出负收益；LC188 当 k > n/2 时退化为无限次交易（直接贪心），否则维度爆炸/超时；LC309 冷冻期状态转移容易漏掉 rest 状态。**
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 按开始时间排序 + 最小堆存「最早结束时间」，堆顶 ≤ 当前会议 start 则复用房间（弹出堆顶），否则新开房间入堆，答案 = 堆大小。LC348 用玩家 +1/-1 计数，行/列/两条对角线绝对值达到 n 即获胜。LC362 时间戳数组 + 滑动窗口计数，hit 记录 timestamp，getHits 清理 300 秒前的过期记录。**面试口述**：间隔题先想「要不要排序、排序键是什么」；设计题先确认数据规模（并发量、读写比例）再选数据结构。**坑：LC253 忘记先排序直接遍历会错；堆里存的是结束时间不是会议本身；LC348 对角线判断 `i == j`（主对角）和 `i + j == n - 1`（副对角）。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 HashMap 存「值 → 下标」，一次遍历边查边存。LC53 Kadane——`curr = max(nums[i], curr + nums[i])`，`best = max(best, curr)`。LC153 与右边界 `nums[right]` 比较二分——`nums[mid] > nums[right]` 则最小值在右半，否则在左半（含 mid）。LC33 先判哪一半有序：`nums[mid] >= nums[left]` 则左半有序，再检查 target 是否落在有序半内，用 `<=` 处理边界。**面试口述**：二分先确认「单调性在哪、比较基准选左还是右」；LC153 选右边界是因为旋转点右侧一定小于左侧。**坑：LC1 必须先查 map 再存入当前元素，否则同一个元素会被用两次；LC53 忘记处理全负数数组（curr 初始化为 nums[0]）；LC33 判断 target 在有序半时边界条件 `<=` 写错会漏掉端点。**
- [ ] **Java 特定陷阱**：HashMap 的 value 是 `Integer` 时（如计数、下标），比较务必用 `.equals()` 而不是 `==` —— 超出 Integer Cache（-128~127）会缓存未命中导致比较失败；深递归（DFS）注意 Stack vs Heap，数据量不大也可能 `StackOverflowError`。

### 重点坑
- [ ] **LC121 股票顺序**：必须先更新 `minPrice` 再计算 `profit`；买卖顺序不能反（先买后卖），在同一个价格上先卖后买会算出错误收益；LC122 无限次交易直接累加所有正差价即可，不需要找局部极值点。
- [ ] **LC188 交易次数边界**：k 超过 `prices.length / 2` 时退化为无限次交易（用 LC122 贪心），否则状态机维度爆炸、容易超时；`buy`/`sell` 更新顺序必须 buy 在前 sell 在后，且 sell 依赖上一轮 buy。
- [ ] **LC253 Meeting Rooms II 排序**：必须先按开始时间排序再遍历，用最小堆维护最早结束时间；只有堆顶 `> interval.start` 才需要新开房间，`<=` 则复用（先弹出再入堆）。忘记排序是最大坑。
- [ ] **LC153/LC33 旋转数组二分基准**：LC153 与右边界比较（`nums[mid] > nums[right]` → 右半），LC33 先判断哪一半有序（`nums[mid] >= nums[left]` → 左半有序），再检查 target 是否在有序半内；边界比较统一用 `<=` 防漏端点。
- [ ] **LC1 Two Sum 查存顺序**：先查 HashMap 再存入当前元素，防止同一个元素被用两次；Java 中 `Integer` 用 `.equals()` 比较（超过 -128~127 的缓存范围 `==` 会失败）。

### 建议刷的新题
- [ ] **数组 / 双指针**：3Sum（LC15，Medium）— 关联已掌握 LC1 Two Sum + 排序。**核心**：排序后固定一个数 `nums[i]`，双指针 l/r 找两数之和 `= -nums[i]`；去重靠跳过相同元素。**坑**：固定数和双指针都要去重；`i` 循环到 `n-2` 即可。
- [ ] **数组 / 前缀积**：Product of Array Except Self（LC238，Medium）— 关联已掌握 Two Sum 的「空间换时间」思路。**核心**：左右两次遍历累积乘积，`answer[i] = 左前缀积 × 右后缀积`。**坑**：不能用整体乘积除法（数组含 0 会崩）；先算左再算右，一次遍历可完成。
- [ ] **间隔**：Merge Intervals（LC56，Medium）— 关联已掌握 LC253 Meeting Rooms II 的排序思想。**核心**：按 start 排序，`curr.end >= next.start` 则合并并更新 `end = max(end, next.end)`，否则把 curr 加入结果。**坑**：先排序；合并时 end 取两者较大值；最后别忘了把最后一个区间加入结果。
- [ ] **动态规划**：House Robber（LC198，Medium）— 关联已掌握股票系列状态机 DP。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，滚动变量优化 O(1) 空间。**坑**：`i` 从 2 开始，注意空数组和单元素边界。
- [ ] **动态规划**：Coin Change（LC322，Medium）— 关联已掌握股票系列 DP 最值思想。**核心**：完全背包——`dp[amount] = min(dp[amount], dp[amount - coin] + 1)`，外循环 coins、内循环 amount。**坑**：初始化为 `amount + 1` 作为无穷大；无解时返回 -1。

## 历史复习记录
- 2026-08-15：动态规划（股票系列）、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-08-14：链表、树与递归、滑动窗口 & 字符串
- 2026-08-13：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-12：动态规划（股票系列）、链表、树与递归
- 2026-08-11：数组 & 二分查找、图论 BFS/DFS、滑动窗口 & 字符串
- 2026-08-10：链表、树与递归、间隔 / 设计题（堆）
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
