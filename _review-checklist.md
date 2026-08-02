# 🎯 面试复习清单

## 📅 今日复习（2026-08-01）

### 需要回顾
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133） — **核心：LC200 沉岛算法——遍历网格遇 '1' → count++ → DFS/BFS 把整座岛标记为 '0'（直接改原数组省 visited 数组）；base case 是「越界 或 是水」。LC207 双解法——DFS 三色标记（0 未访问 / 1 访问中 → 撞见即环 / 2 已完成 → 剪枝，避免重复遍历已确认无环的子树）；BFS Kahn 拓扑排序（统计入度，入度为 0 入队，出队后后继入度 -1，最终 processed == numCourses 即无环）。LC133 HashMap 备忘录——key 原始节点、value 克隆节点，**先入表再递归邻居**，防止环 A→B→A 无限递归。**面试口述**：图题先问「有向/无向」「有无环」「连通分量还是最短路」——连通分量用 DFS 简洁、最短路/层级用 BFS；矩阵类图的邻居靠坐标计算（要查越界），图类邻居在 List 里（只有 null 风险）。**坑：LC200 全陆地时递归深度 = M×N 可能 StackOverflow（换 BFS 或迭代 DFS）；LC207 Kahn 不需要 visited（入度降为 0 才入队天然防重）、`int[]` 默认初始化为 0 不是 null；LC133 交换「入表」和「递归邻居」的顺序会死循环。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）、Longest Common Prefix（LC14） — **核心：LC3 找最长——right 扩张、出现重复时 left 收缩，`int[128]` 计数数组替代 HashMap；优化版用 HashMap 记录每个字符上次出现位置，重复时 `left = max(left, map[char] + 1)` 直接跳跃。LC76 找最短——need[]（t 的需求量）+ window[]（窗口计数）+ valid（已有多少种字符满足需求），`valid == totalNeeded` 时收缩 left 并更新最短窗口；「先扩张到合法、再收缩找最优」是滑动窗口通用模板。LC14 纵向逐列扫描——所有字符串第 i 位相同才继续，不匹配立即 `strs[0][:i]` 切片返回。**面试口述**：先分清「找最长」（窗口非法才收缩）还是「找最短」（窗口一合法就收缩试探）；字符类题优先 `int[128]` 数组。**坑：LC3 收缩时「先移出字符再 left++」，先 l++ 再 remove 会移错字符；r 每轮只加一次防死循环。LC76 收缩时只有 `window[d] == need[d]` 才 valid--（否则把已经不覆盖 t 的窗口当成覆盖）；Java 比较 Integer 用 .equals() 不用 ==（超出 -128~127 缓存是地址比较）。LC14 注意空数组返回 ""。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、Stock IV（LC188）、Stock with Cooldown（LC309） — **核心：系列本质是状态机 DP——LC121 一次交易：`minPrice` 与 `profit` 两变量滚动，O(1) 空间。LC188 k 次交易：把 4 状态泛化为 `buy[j]` / `sell[j]` 两个长度为 k 的数组，`buy[j] = max(buy[j], sell[j-1] - price)`、`sell[j] = max(sell[j], buy[j] + price)`；**k >= n//2 时限制失效，退化为 LC122 无限次贪心（累加所有正差价）**。LC309 冷冻期：把「空仓」拆成 sold（今天刚卖、明天不能买）和 rest（可买）两个状态，三状态转移 `hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)`，**必须多元赋值**（sold 依赖旧 hold、hold 依赖旧 rest，依次更新会覆盖旧值），答案取 max(sold, rest)。**面试口述**：股票题先数「交易次数上限 + 有无冷冻期/手续费」再定状态个数——1 次（2 变量）、无限次（贪心）、k 次（2 数组）、冷冻期（3 状态）、手续费（买入时扣 fee）。**坑：LC188 k=0 必须特判（`[-prices[0]] * 0` 是空列表会越界），k 很大还跑 O(NK) 会超时/MLE；LC309 漏掉 rest 状态会允许「今天卖、明天买」的非法转移；状态变量不要混用（类似 LC53 的 prev_max 与 ans 必须分开维护）。**

### 重点坑
- [ ] **LC207 三色标记法「状态 1 撞见即环、状态 2 剪枝」**：只用 0/1 能检测环，但没有状态 2 会重复遍历已确认无环的子树（如 A→B→C 确认无环后 D→B 再次遇到 B 应直接跳过）。**坑**：BFS Kahn 必须「入度降为 0 才入队」，天然防重、不需要 visited 数组；`int[]` 默认初始化为 0 不是 null；若要求输出修课顺序（Course Schedule II），直接把 poll() 的顺序记录下来。
- [ ] **LC133 Clone Graph「必须先入表再递归邻居」**：顺序反了，环 A→B→A 时 A 永远查不到备忘录 → 无限递归 StackOverflow。**正确**：`visited.put(node, cloneNode)` 必须在 `for (neighbor : node.neighbors)` 之前。**坑**：HashMap 要设为成员变量全局共享，不能每次递归新建；`if (node == null)` 同时处理初始 null 输入和邻居列表中的 null，双重作用。
- [ ] **LC200 沉岛「全陆地时 DFS 递归深度 = M×N」**：内存模型上每个 dfs 调用占一个栈帧，最坏情况（全 '1'）栈深等于格子数 → StackOverflow。**正确**：数据量大换 BFS（Queue）或迭代 DFS；小数据 DFS 代码更简洁。**坑**：直接改原数组 `grid[r][c] = '0'` 省 visited，但面试要说明「修改输入」的前提；base case 先判越界再取 `grid[r][c]`，顺序反了会数组越界。
- [ ] **LC76「收缩时只有 window[d] == need[d] 才 valid--」**：窗口 left 移出的字符若是「需求量恰好被满足」的那种，valid 才减 1，否则会把已经不覆盖 t 的窗口当成覆盖，漏掉正确答案（边界如 s="a"、t="aa"）。**坑**：Java 比较 HashMap 的 Integer 值必须 .equals() 不能 ==（-128~127 之外是地址比较）——这是 blind-75 总览里点名的 Java 陷阱。
- [ ] **股票 DP「LC309 漏 rest 状态 / LC188 忘退化特判」**：冷冻期必须把空仓拆成 sold 与 rest 两个状态，否则「今天卖、明天买」的非法转移会被允许；三状态转移必须多元赋值（读旧值），依次赋值会互相覆盖。**坑**：LC188 当 k >= n//2 时退化为 LC122 贪心（累加正差价），不退化则 O(NK) 超时；k=0 不特判会因空列表越界；初始化已处理 prices[0]，循环应从 prices[1:] 开始。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 Number of Islands（矩阵 BFS/DFS 遍历）。**核心**：反向思维——不从每个格子正向搜索，而从四条海岸线边界反向 DFS/BFS，分别标记能流到太平洋/大西洋的格子，两个标记的交集即答案；用 visited 二维数组防重。**坑**：方向数组 `dirs = [(1,0),(-1,0),(0,1),(0,-1)]` 统一四方向；反向搜索时高度比较用 `>=`（水往低处流，反向是往高处爬）。
- [ ] **图论 / 哈希**：Longest Consecutive Sequence（Medium）— 关联已掌握 LC200 连通分量思想 + LC1 Two Sum 哈希表。**核心**：数字放入 HashSet 后，只从「序列起点」（`num - 1` 不存在于集合）开始向后累加计数，保证每个数字最多访问一次，O(n)/O(n)。**坑**：必须跳过非起点（`num-1 in set` 时 continue），否则每个元素都被当起点重复扫描，退化为 O(n²)。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3/LC76 滑动窗口通用模板。**核心**：窗口合法条件是「窗口长度 - 窗口内最高频字符数 ≤ k」（可替换 k 个字符），维护 maxCount，超了就收缩 left；找最长 → 窗口非法才收缩。**坑**：maxCount 在收缩时不必回退（经典优化：只增不减不影响答案正确性），别为「精确 maxCount」写多余代码。
- [ ] **字符串 / 双指针**：Longest Palindromic Substring（Medium）— 关联已掌握 LC3 字符串处理、LC14 逐列扫描思维。**核心**：中心扩展法——以每个字符（奇数长度）和每两个字符间隙（偶数长度）为中心向两边扩展，O(n²)/O(1)；也可 DP `dp[i][j] = (s[i]==s[j] && dp[i+1][j-1])`。**坑**：中心共有 2n-1 个（含字符间隙），别只遍历字符本身，否则漏掉偶数长度回文（如 "bb"）。
- [ ] **动态规划 / 贪心**：Jump Game（Medium）— 关联已掌握 LC122 贪心思想、股票系列状态转移。**核心**：维护最远可达位置 `maxReach = max(maxReach, i + nums[i])`，遍历中若 `i > maxReach` 直接返回 false；O(n)/O(1)。**坑**：看的是「累积最远能到哪」而非「下一步能跳多远」；当 `nums[i] == 0` 且 `maxReach == i` 时被卡死，要能识别这种无法前进的情况。

## 历史复习记录
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
