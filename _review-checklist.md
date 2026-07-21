# 🎯 面试复习清单

## 📅 今日复习（2026-07-20）

### 需要回顾
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133）— **核心：LC200 沉岛算法——遍历到 '1' 即 DFS/BFS 标记所有连通的 '1' 为 '0'（原地修改避免 visited 数组）。LC207 拓扑排序 + 环检测——三色标记法（white/gray/black），gray 表示在当前 DFS 栈中（发现 gray 即有环）；或 Kahn 算法（BFS）记录入度，入度为 0 入队，每出队一个节点削减邻居入度。LC133 克隆图——HashMap `oldNode → newNode` 避免重复克隆，DFS/BFS 遍历邻居时递归克隆并连接。**时间复杂度**：均为 O(V+E)。
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End Of List（LC19）— **核心：LC206 反转——三指针 `prev/curr/next`，迭代写法更稳；递归写法 `reverseList(head.next)` 后接 `head.next.next = head`。LC141 快慢指针——`slow = slow.next, fast = fast.next.next`，相遇则有环；注意 `fast != null && fast.next != null` 的循环条件顺序。LC21 dummy 哑节点——`dummy.next` 锚定结果头，逐节点比较 `l1.val` 与 `l2.val` 拼接。LC19 双指针间距法——`fast` 先走 n 步，再 `slow/fast` 同步走至 `fast == null`，`slow` 即停在待删节点前一位，`slow.next = slow.next.next`。**

### 重点坑
- [ ] **LC141 快慢指针循环条件顺序**：必须写成 `while fast != null && fast.next != null`（先 fast 后 fast.next），如果反过来写会 NPE（空指针），因为先访问 `fast.next` 时 fast 可能为 null。另外空链表 `head == null` 时进循环体前应直接返回 false。误以为「快指针走到尾部 = 无环」要相当小心：fast 遇到 null 即终止，**相遇才说明有环**——`slow == fast` 返回 true 必须在快慢指针都走至少一步之后判断（否则同步起跑会直接相等）。
- [ ] **LC19 删除倒数第 N 个节点的边界**：当 `n == 链表长度` 时（即删除头节点），`fast` 先走 n 步后已经为 null，`slow` 没动——若不用 dummy 节点，需要单独处理「返回 head.next」。**正确写法**：套一个 dummy 节点指向 head，slow 从 dummy 开始，这样所有删除场景统一为 `slow.next = slow.next.next`，无需特殊处理头节点。此外 n 的合法性（1 ≤ n ≤ 长度）一般题目已保证，但面试时要明确假设。
- [ ] **LC207 三色标记法的颜色含义**：white=未访问，gray=在当前 DFS 路径上（栈中），black=已完成。**关键坑**：发现 gray 节点不一定是环——必须确认这是「当前 DFS 栈」中的 gray。如果遍历结束后才标记 black，但是中途遇到 gray，那才是回边（back edge）。常见错误：用 2 色（visited/unvisited）做 DFS 检测环会误判——例如 A→B, A→C, B→C 中，从 A 出发访问 C 后标记 visited，再从 B 访问 C 看到 visited 误以为有环，其实没有。**3 色是必须的**。
- [ ] **LC200 沉岛 vs visited 数组的边界**：原地修改 grid 把 '1' 标记为 '0' 可省空间，但**会破坏输入**——面试中要先问面试官「能否修改输入」。如果不能修改，必须用 `visited` 二维数组或 `Set<String>` 记录坐标。DFS 递归深度可能导致 StackOverflow（大网格 300×300），可改用 BFS + 队列避免栈溢出。另外「岛屿」连通性是 4 连通（上下左右），不是 8 连通，写邻居时方向数组 `[(1,0),(-1,0),(0,1),(0,-1)]`。

### 建议刷的新题
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC1/LC53（一遍扫描 O(n) 模式）。**核心**：先从左到右扫一遍构建 left 前缀积数组，再从右到左同步乘上 right 后缀积，空间可优化到 O(1)（输出数组不算额外空间）。**坑**：题目要求不能用除法，需纯乘法构造。边界：`prefix[i] = prefix[i-1] * nums[i-1]`，`prefix[0] = 1`。
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握 LC1 Two Sum（HashMap 对）。**核心**：排序 + 固定第一个数，双指针找 `target = -nums[i]`。去重关键——外层 `i > 0 && nums[i] == nums[i-1]` 跳过，内层 `while left < right && nums[left] == nums[left+1] left++`。**坑**：不排序无法做双指针去重；去重逻辑写错会导致漏解或多解。
- [ ] **数组/Hash Table**：Contains Duplicate（Easy）— 关联已掌握 LC1（HashMap 用法）。**核心**：HashSet 一遍扫，遇到 `num in set` 返回 true，否则加入 set。O(n) 时间，O(n) 空间。**坑**：常见误区是先排序再判相邻（O(n log n)），实际 HashSet 更优。如果要求 O(1) 空间，可排序后比较相邻元素 `nums[i] == nums[i-1]`。
- [ ] **动态规划**：House Robber（Medium）— 关联已掌握股票系列状态机（选/不选的二维状态）。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`——不抢当前（继承 i-1）或抢（i-2 + 当前）。空间优化到两个滚动变量。**坑**：base case `dp[0] = nums[0]`，`dp[1] = max(nums[0], nums[1])`，注意处理好长度为 1 的边缘情况。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握股票系列 DP 思维。**核心**：斐波那契 `dp[i] = dp[i-1] + dp[i-2]`，O(1) 空间滚动变量。**坑**：base case `dp[1]=1, dp[2]=2` 容易写反；面试中注意不能用递归（栈溢出），用迭代。

## 历史复习记录
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
