# 🎯 面试复习清单

## 📅 今日复习（2026-08-07）

### 需要回顾
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 两种解法——双指针时间线扫描（starts/ends 分别排序，`starts[s] >= ends[e]` 说明有会议室释放则 used--，max_rooms 记峰值）或最小堆（堆顶 = 最早结束的会议，`rooms[0] <= start` 就 pop 复用，堆大小即所需会议室数）；LC348 计分法 O(1)——玩家 1 加 +1、玩家 2 加 -1，`abs(score) == n` 判胜（±1 正负抵消，杜绝混合棋子假阳性），主对角线 `row == col`、副对角线 `row + col == n - 1`；LC362 deque 存时间戳，`q[0] <= timestamp - 300` 清理过期（均摊 O(1)），进阶用 `[timestamp, count]` Pair 合并同秒 + total 记账本。**面试口述**：间隔题先「按 start 排序 + 扫描」；设计题先问「数据规模 / 查询频率」再选 deque（滑动窗口）、heap（取最值）或二分（历史查询）。**坑：LC253 重叠/释放判断用 `<=`（前一会议刚好结束即可复用）；LC348 二维数组用 `[[0]*n for _ in range(n)]` 初始化，不能用 `[[0]*n]*n`（共享引用）；LC362 过期判断用 `<=` 不是 `<`，访问 q[0] 前先判空。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 一遍哈希表「先查 complement 再存自己」；LC53 Kadane——`dp[i] = max(dp[i-1] + nums[i], nums[i])`，当前连续和与全局最大用两个变量分开维护，空间 O(1)；LC153 找极值模板 `while (left < right)`，与右边界 `nums[right]` 比较（`nums[mid] > nums[right]` → `left = mid + 1`，否则 `right = mid`——mid 可能是最小值）；LC33 找目标模板 `while (left <= right)`，排除法——`nums[left] <= nums[mid]` 则左边有序，检查 target 是否在其中，不在就去另一半（含断层）。**面试口述**：二分先问「找特定值（`<=` 循环）还是找极值/边界（`<` 循环）」选模板；旋转数组统一和右边界比，消除二义性。**坑：LC1 先查后存防自匹配；LC53 混用一个变量会把不相邻元素加在一起；LC153 用左边界判断无法区分数组是否旋转过（二义性）；`right = mid` 时 mid 必须向下取整防死循环。**
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Clone Graph（LC133）、Course Schedule（LC207） — **核心：LC200 沉岛法——遇 '1' count++ 后 DFS 四方向全部标记 '0'，省 visited 数组；LC133 HashMap 备忘录（原始节点 → 克隆节点），先入表再递归防环；LC207 三色标记环检测——0 未访问 / 1 访问中（再遇到 = 有环）/ 2 已完成（再遇到 = 剪枝），或 BFS Kahn 拓扑排序——入度数组 + 队列，入度为 0 入队，出队后继入度 -1，最后 `count == n` 无环。**面试口述**：连通分量 → DFS（代码简洁）；最短路径 → BFS（逐层天然最短）；环检测/拓扑 → 三色 DFS 或 Kahn BFS；BFS 队列用 deque 不用 list.pop(0)（退化为 O(N²)）。**坑：LC133 先入表再递归，否则 A→B→A 环无限递归 StackOverflow；LC207 状态 2（已完成）是剪枝关键不能省；全陆地大矩阵 DFS 递归过深会爆栈，换 BFS 或迭代。**

### 重点坑
- [ ] **LC153 旋转数组二分「必须和右边界比较，不能用左边界」**：`nums[left]` 判断无法区分数组是否旋转过（二义性）；`nums[mid] > nums[right]` → 最小值在右半边 `left = mid + 1`，否则 `right = mid`（mid 自己可能就是最小值，不能 `mid - 1`）；`while (left < right)` 配 `right = mid` 时 mid 必须向下取整，否则死循环。
- [ ] **LC253 间隔「释放会议室的判断用 `<=` 不是 `<`」**：时间线扫描中 `starts[s] >= ends[e]`（即 `ends[e] <= starts[s]`）才说明有会议室腾出——前一会议刚好在此刻结束可复用；用 `<` 会把「刚好同时」误判为仍占用，多算会议室。最小堆版同理：`rooms[0] <= start` 才 pop。
- [ ] **LC348 设计题「±1 计分法 + 二维数组初始化」**：直接用 player 值（1/2）累加，混合棋子会假阳性（如 2+2+1=5 被误判玩家 1 获胜），必须 +1/-1 正负抵消、`abs(score) == n` 判胜；Python 初始化二维数组用 `[[0]*n for _ in range(n)]`，`[[0]*n]*n` 所有行共享同一引用，改一行全变。
- [ ] **LC133 图深拷贝「先入表再递归」**：HashMap 必须在处理邻居前 put 克隆节点——先递归再存表时 A→B→A 环会无限递归 StackOverflow；visited 备忘录是全局共享的，不能放在递归函数内部新建。
- [ ] **LC53 Kadane「当前连续和与全局最大分开维护」**：`ans = max(ans + nums[i], nums[i])` 会把不相邻的元素加在一起（ans 存的是全局最大，不是当前连续和）；正确写法是 `prev_max = max(prev_max + nums[i], nums[i])` 做状态转移，`ans = max(ans, prev_max)` 记全局。

### 建议刷的新题
- [ ] **间隔**：Merge Intervals（Medium）— 关联已掌握 LC253 排序 + 扫描思维。**核心**：按 start 排序后扫描，`cur.end >= next.start` 则合并（end 取 max），否则把 cur 加入结果并重置；O(n log n)。**坑**：必须按 start 排序；合并时 end 取两个区间的最大值，不能直接取 next.end。
- [ ] **间隔**：Insert Interval（Medium）— 关联已掌握 Merge Intervals 合并逻辑。**核心**：三段式——newInterval 左侧不重叠的区间直接加入、与 newInterval 重叠的区间合并（start 取 min、end 取 max）、右侧不重叠的区间直接加入。**坑**：合并时用更新后的 newInterval 继续向后比较；注意 newInterval 在开头/结尾的边界情况。
- [ ] **堆 / 设计**：Top K Frequent Elements（Medium）— 关联已掌握 LC1/LC3 的 HashMap 计数 + LC253 堆操作。**核心**：HashMap 统计频次后，用大小为 k 的**小顶堆**维护前 k 高频（堆顶是最小频次，新元素频次更大就替换），O(n log k)；进阶用桶排序 O(n)。**坑**：用大顶堆会退化为 O(n log n)；堆满 k 个后先比较堆顶再决定是否替换。
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC53 一遍扫描维护状态的思维。**核心**：两遍扫描——第一遍从左到右把前缀积存进输出数组，第二遍从右到左乘后缀积，O(1) 额外空间（不含输出数组）。**坑**：题目禁止用除法（数组含 0 会崩）；前缀积数组直接复用为输出数组。
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 的 DFS/BFS 遍历。**核心**：反向思维——从太平洋边界（上、左）和大西洋边界（下、右）分别向内 DFS/BFS 标记可达区域，最后取两个集合的交集。**坑**：从边界向内遍历时条件是「下一个格子高度 >= 当前」（水往高处流），方向与常规相反；visited 要分太平洋/大西洋两个布尔数组。

## 历史复习记录
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
