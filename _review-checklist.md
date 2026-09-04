# 🎯 面试复习清单

## 📅 今日复习（2026-09-03）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Number of Islands（LC200）、Course Schedule（LC207） — **核心：LC133 深拷贝用 `HashMap<Node,Node> visited` 缓存，创建 clone 后「先入表再递归」克隆邻居，否则环 A→B→A 会无限递归 StackOverflow；LC200 沉岛算法——遍历矩阵遇 '1' 则岛屿数 +1，并从该格 DFS/BFS 把相连陆地全部淹成 '0'，递归前先做边界检查 `r<0 || c<0 || r>=rows || c>=cols || grid[r][c]=='0'` 直接 return；LC207 拓扑排序判环——Kahn BFS：邻接表 + 入度数组，入度为 0 的课程入队，出队 count++ 并把后继入度 -1、归 0 再入队，最后 `count == numCourses` 才可完成（有环则 count < n），无需 visited（入度天然防重）；DFS 三色标记（0 未访问 / 1 访问中 / 2 已完成）遇到状态 1 即发现环。**面试口述：连通分量计数用 DFS、拓扑/环检测用 Kahn BFS 迭代不爆栈；克隆图先确认用深拷贝，节点与邻居都要新建。**坑：LC133 忘记先 put 再递归必爆栈；LC207 有向图只加一条边并只给后继 +1 入度；LC200 面试确认是否允许修改原数组。**（本组为轮换复习，昨日已复习滑动窗口/股票DP/间隔设计，今日轮到图论/链表/树，距上次复习本组隔 1 天）**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针迭代 prev/curr/next——改 `curr.next` 前先存 next，逐个指回 prev；递归版先递到尾部，回溯时 `node.next.next = node` 再 `node.next = None` 断链；LC141 快慢指针——slow 走 1 步、fast 走 2 步，循环条件 `while fast and fast.next`，相遇即有环、走到 null 则无环；LC21 dummy 哨兵 + 双指针逐小接入，某条链耗尽后直接接另一条剩余部分；LC19 dummy + 快指针先走 n 步，再快慢同步走，快指针到尾部时 slow 正好停在待删节点**前驱**，`slow.next = slow.next.next` 完成删除。**面试口述：头节点可能被删/被换的题一律 dummy node 消除特判；链表题本质是改引用，画图比空想可靠。**坑：断链预警——修改 next 前先保存原 next；用 `.next.next` 前确保 fast 与 fast.next 都非空；LC19 慢指针必须停在被删节点前一个（快指针先走 n 步而非 n+1 时配合 while fast.next 判断）。**（本组为轮换复习，昨日已复习滑动窗口/股票DP/间隔设计，今日轮到图论/链表/树，距上次复习本组隔 1 天）**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree from Preorder and Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235） — **核心：LC104 后序递归 `depth = 1 + max(dfs(left), dfs(right))`，空节点返回 0；LC100 递归同构——两节点皆空 true、一空一非空 false、值不等 false，再递归比较左右子树；LC226 递归交换左右孩子，swap 用临时变量防引用覆盖；LC102 BFS 队列 + `for _ in range(len(q))` 固定当前层大小逐层收集；LC105 前序首元素为根，HashMap 存中序「值→下标」O(1) 定位根，按中序左右区间递归建树、前序下标递增；LC98 中序遍历必须严格递增——递归传 `(min, max)` 区间或维护 prev 指针，**不能只和直接左右孩子比较**；LC235 利用 BST 性质指路——p、q 都小于 root 走左、都大于走右，分叉点即 LCA（LC236 普通二叉树则后序递归：左右都非空返回当前节点）。**面试口述：树 80% 题 = 递归三要素（base case / 递归左右 / 向上汇总），先定「每个节点返回什么」再写代码。**坑：递归忘记判空；LC98 传区间用 long 的 ±inf 防 int 边界；LC105 中序下标不缓存会退化 O(N²)；链状深树递归可能栈溢出，可换迭代栈。**（本组为轮换复习，昨日已复习滑动窗口/股票DP/间隔设计，今日轮到图论/链表/树，距上次复习本组隔 1 天）**

### 重点坑
- [ ] **图论**：LC133 克隆图必须先 `visited.put(node, clone)` 再递归邻居（先入表再递归），否则 A→B→A 环导致无限递归 StackOverflow；LC200 递归前先查越界/水体，沉岛（原地改 '0'）防重复访问，面试先确认可否修改原数组；BFS 队列用 `deque`，`list.pop(0)` 是 O(N) 会让整体退化 O(N²)。
- [ ] **链表**：改 `curr.next` 之前先保存原 next（断链预警）；快慢指针用 `fast.next.next` 前确认 fast 与 fast.next 均非空；反转/删除头节点的题一律 dummy node 免特判；LC19 快指针先走 n 步后快慢同步走，让 slow 停在待删节点**前驱**（`slow.next = slow.next.next`），而不是被删节点本身。
- [ ] **树**：LC98 校验 BST 必须传 min/max 区间或中序维护 prev，只和直接子节点比会漏「左子树的右孩子超大」类反例；LC105 中序值→下标用 HashMap 缓存，否则每次线性 find 整体 O(N²)；层序 BFS 用 `for _ in range(len(q))` 固定本层数量，别在循环体里动态取 len(q)（会串层）；极端深树递归 DFS 小心 StackOverflowError。
- [ ] **通用**：Java 比较 `Integer` 用 `.equals()` 而非 `==`（IntegerCache -128~127 之外失效）；Python 二维数组用列表推导式 `[[0]*n for _ in range(n)]`，`[[0]*n]*n` 各行共享同一引用；递归/队列优先 `deque`，避免 O(N) 头删。

### 建议刷的新题
- [ ] **图论/矩阵 DFS**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握知识点：LC200 Number of Islands 的网格 DFS/BFS（已完成）。**核心**：从每个格子正向判断能否到达两洋是 O(MN·MN) 会超时；反过来从四条边界「逆流而上」——只走向高度 ≥ 当前格的邻居，用两个 visited 布尔矩阵分别标记能流到太平洋 / 大西洋的格子，最后取交集。**坑**：方向别搞反（是水往低处流，反向则向高处走）；两个矩阵分别 DFS 后再合并，不要共用一个 visited。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握知识点：LC100 Same Tree 递归同构判断（已完成）。**核心**：`isSubtree(root, sub)` = 从当前节点起 `isSameTree(root, sub)` 为真，否则递归检查 `root.left` / `root.right`；isSameTree 即 LC100 原题。**坑**：子树要求结构完全一致（含空节点位置），isSameTree 里两空为 true、一空一非空为 false；递归三处都要判空。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握知识点：LC206 反转链表 + LC141 快慢指针（已完成）。**核心**：快慢指针找中点 → 反转后半段 → 前半与反转后的后半交替合并（L0→Ln→L1→Ln-1→…）。**坑**：找中点后要把前半段尾部断链（`mid_prev.next = None`），否则合并时成环死循环；反转后半段复用 LC206 模板。
- [ ] **链表 + 堆**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握知识点：LC21 合并两个有序链表 + LC253 最小堆用法（已完成）。**核心**：K 个头节点入最小堆（按节点值），每次弹出最小节点接入结果链，再把其 next 入堆，O(N log K)；另一思路分治两两合并（复用 LC21）。**坑**：Python 堆里直接存 ListNode 需要自定义 `__lt__`，稳妥做法存 `(val, i, node)` 三元组防值相等时比较节点报错；跳过空链表，K=0 时返回 None。
- [ ] **树/递归**：Binary Tree Maximum Path Sum（LC124，Hard）— 关联已掌握知识点：LC104 Maximum Depth 的后序递归（已完成）。**核心**：后序递归每个节点返回「向上延伸的最大单边贡献 `max(left_gain, right_gain, 0) + val`」，同时用全局变量更新「以该节点为拐点的完整路径和 `left_gain + right_gain + val`」。**坑**：单边贡献允许取 0（负数子树直接不选）；全局答案初始化为 `float('-inf')` 而非 0，否则全负数树会得 0 的错答案。

## 历史复习记录
- 2026-09-03：图论 BFS/DFS、链表、树与递归
- 2026-09-02：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-09-01：图论 BFS/DFS、链表、树与递归
- 2026-08-31：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-30：图论 BFS/DFS、链表、树与递归
- 2026-08-29：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-28：图论 BFS/DFS、链表、树与递归、数组 & 二分查找
- 2026-08-27：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-26：图论 BFS/DFS、链表、树与递归
- 2026-08-25：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-24：图论 BFS/DFS、链表、树与递归
- 2026-08-23：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-22：图论 BFS/DFS、链表、树与递归
- 2026-08-21：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-20：图论 BFS/DFS、链表、树与递归
- 2026-08-19：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-18：图论 BFS/DFS、链表、树与递归
- 2026-08-17：滑动窗口 & 字符串、动态规划（股票系列）、数组 & 二分查找
- 2026-08-16：图论 BFS/DFS、链表、树与递归
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
