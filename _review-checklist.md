# 🎯 面试复习清单

## 📅 今日复习（2026-08-13）

### 需要回顾
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 按开始时间排序 + 最小堆存「结束时间」，`start >= 堆顶` 则 pop 复用会议室、否则 push，堆大小即最大并发会议数。LC348 每行 / 每列 / 两对角线各维护计数器，玩家 1 记 +1、玩家 2 记 -1，某计数器绝对值 == n 即赢（O(1) 判定，无需遍历棋盘）。LC362 时间戳队列 / 环形数组，`getHits` 先清理 300 秒前的旧时间戳再返回长度。**面试口述**：先想「要不要排序」「堆里存什么」。**坑：LC253 不按 start 排序直接入堆必错；堆里存的是 end 不是 start；LC348 对角线条件 `row == col`、`row + col == n - 1` 别漏。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 哈希表存「值 → 下标」，一次遍历查 `target - nums[i]`，先查后存防自配。LC53 Kadane——`cur = max(nums[i], cur + nums[i])`、`best = max(best, cur)`，全负数数组也能正确。LC153 与右边界比较——`nums[mid] > nums[right]` 则 `left = mid + 1`，否则 `right = mid`。LC33 先判「哪半有序」，target 在有序半内就缩到该半、否则去另一半，`nums[mid] == target` 优先返回。**面试口述**：先确认「是否旋转」「找值还是找边界」，再选模板。**坑：LC1 先存再查会重复用同一个元素；LC153 与左边界比较在非旋转 / 偶数长度时会错；LC33 循环条件 `left <= right` 与 `left == right` 边界漏判。**
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛——遍历到未访问的 '1' 计数 +1，DFS/BFS 把整片相邻陆地置 '0'。LC207 拓扑排序——Kahn（入度表 + 队列，逐个弹出入度为 0 的节点）或 DFS 三色标记（0 未访问 / 1 访问中 / 2 已完成）检测环，有环返回 false。LC133 克隆——`HashMap<原节点, 新节点>`，DFS 先创建新节点再递归邻居，用 map 判重防死循环。**面试口述**：先定「BFS 还是 DFS」「是否需要 visited / 入度表」。**坑：LC200 每个 '1' 只触发一次 DFS，沉岛后别重复计数；LC207 邻接表方向（prereq → course）必须与入度表一致；LC133 必须先建节点再处理邻居，否则无限递归。**
### 重点坑
- [ ] **LC253 会议室 II 的排序与堆内容**：必须先按开始时间排序，堆里存「结束时间」——不排序直接入堆，堆顶不是最早结束的会议，复用判断全错；新会议 `start >= 堆顶 end` 才 pop 复用，否则 push 新结束时间。
- [ ] **二分查找边界比较**：LC153 与右边界比（`nums[mid] > nums[right]` 才向右缩），与左边界比在非旋转 / 偶数长度场景会错；LC33 先判哪半有序再二分；`mid = left + (right - left) / 2` 防溢出，循环退出条件想清楚再写。
- [ ] **LC207 建图方向与入度一致**：邻接表方向（prereq → course）和入度表必须对应，方向反了拓扑排序结果全错；DFS 三色标记法里「访问中再遇到该节点」才是环，已完成（2）不算环。
- [ ] **LC200 沉岛计数**：每遇到一个未访问的 '1' 才计数 +1 并整片沉掉；若 DFS 里重复计数、或忘记把相邻陆地置 '0'，岛屿数会多算。
- [ ] **Java Integer 比较用 `.equals()`**：HashMap 的 values 等 Integer 对象用 `==` 比较会踩 Integer Cache（-128 ~ 127）的坑——小值碰巧相等、大值必不等，面试写 Java 时务必用 `.equals()`。

### 建议刷的新题
- [ ] **间隔**：Merge Intervals（LC56，Medium）— 关联已掌握 LC253 间隔排序处理。**核心**：按 start 排序后线性扫描，`interval[0] <= prevEnd` 则合并（更新 end 取 max），否则开新区间。**坑**：不排序直接合并必错；合并时 end 要取两者较大值。
- [ ] **堆**：Top K Frequent Elements（LC347，Medium）— 关联已掌握 LC253 最小堆。**核心**：HashMap 计数 + 大小为 k 的最小堆（按频率比较），堆满且新频率更高时 pop 堆顶；也可用桶排序 O(n)。**坑**：堆比较的是频率不是元素值；最后堆内元素顺序任意，无需排序输出。
- [ ] **数组**：3Sum（LC15，Medium）— 关联已掌握 LC1 Two Sum。**核心**：排序 + 固定一个数 + 双指针找剩余两数，`sum < 0` 左移、`sum > 0` 右移。**坑**：固定数和双指针都要跳过重复值去重，否则结果重复。
- [ ] **数组 / 动态规划**：Maximum Product Subarray（LC152，Medium）— 关联已掌握 LC53 Kadane。**核心**：同时维护当前最大 / 最小乘积（负负得正），`curMax = max(nums[i], nums[i]*curMax, nums[i]*curMin)`，遇 0 自动重置。**坑**：只维护最大值会漏掉「两个负数相乘变正」的情况，必须成对维护。
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握 LC200 沉岛 DFS。**核心**：从四条边界反向 DFS / BFS，分别标记能流入太平洋 / 大西洋的格子，两个标记都有的格子即答案。**坑**：反向从边界出发（水往高处流），两个方向的 visited 要分开标记，最后取交集。

## 历史复习记录
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
