# 🎯 面试复习清单

## 📅 今日复习（2026-08-04）

### 需要回顾
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock I-IV（LC121/122/123/188）、Cooldown（LC309）、Transaction Fee（LC714） — **核心：一套状态机框架通吃——先问「几次交易 / 有无冷冻期 / 有无手续费」决定状态个数；LC121 只交易一次——维护历史最低价 min_price，每天尝试卖出取 max（状态机雏形 buy=max(buy,-price), sell=max(sell,buy+price)）；LC122 无限次——贪心累加所有 `price[i] > price[i-1]` 的正差价（分段交易等价于一次交易），或 2 状态 hold/not_hold；LC123 最多 2 次——4 状态 buy1/sell1/buy2/sell2，buy2 = max(buy2, sell1 - price)；LC188 最多 k 次——泛化为 buy[j]/sell[j] 数组，`k >= n//2` 时退化为 122 贪心（O(NK)→O(N)）；LC309 冷冻期——「空仓」拆成 sold（刚卖）/ rest（可买）两个状态 → 3 状态机；LC714 手续费——回到 2 状态，买入或卖出扣一次 fee。**面试口述**：股票题先报状态机框架「定义状态 → 转移方程 → 初始化 → 空间压缩」，再说每题的差异化限制；LC309/714 强调多元赋值是为了读旧值。**坑：LC309 依次赋值会覆盖旧值，必须 `hold, sold, rest = ...` 多元赋值；LC188 不做贪心特判会 O(NK) 超时；LC714 手续费只能扣一次（买或卖选一个）；LC123 初始化 buy2 = -prices[0] 而不是 0。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order（LC102）、Construct from Pre/Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235）、LCA of Binary Tree（LC236） — **核心：递归三件套——终止条件 → 递归调用 → 汇总返回；LC104 = `1 + max(depth(left), depth(right))`；LC98 上下界递归传 `(min_val, max_val)` 区间，或中序遍历序列严格递增；LC105 前序第一个元素必为根 + 中序以根为界切左右子树，哈希表存 inorder 索引避免 O(N) 查找；LC235 用 BST 值大小「指路」O(h) 下探；LC236 普通二叉树用后序汇总——左右子树各找到一边即当前节点是 LCA；LC102 BFS 队列按层处理。**面试口述**：先问「BST 还是一般二叉树」决定能否用值大小剪枝；递归先写终止条件；树的题大部分是「分治 + 后序汇总」。**坑：LC98 只比较父子节点会漏（必须传上下界），且判空用 `is not None`（节点值可能为 0，`if min_val:` 会误判）；LC105 preorder 指针全局自增、必须先递归左子树（preorder 顺序 [根,左,右]）；LC236 的 `return left or right` 上传逻辑别写反。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针 prev/curr/next_temp 推移反转，递归版 `head.next.next = head` 从后往前；LC141 快慢指针（Floyd）判环，有环快指针必套圈慢指针；LC21 Dummy Node 拉链式合并，`curr.next = l1 or l2` 接剩余；LC19 快指针先走 N+1 步保持间距，slow 停在待删节点的**前驱**。**面试口述**：链表题第一反应「要不要 Dummy Node 简化头节点处理」；快慢指针三用途——判环 / 找中点 / 找倒数第 N 个。**坑：LC206 迭代忘存 next_temp 会断链、递归版忘 `head.next = None` 会成环；LC141 必须 `while fast and fast.next` 防空指针；LC19 走 N+1 步而不是 N 步，否则 slow 会停在被删节点本身；LC21 注意用 `<=` 保证稳定。**

### 重点坑
- [ ] **LC98 验证 BST 必须传上下界**：只比较「父节点 vs 子节点」会漏——反例根 5、右子树左孩子 3（比 5 小但比右子树根 6 小，局部合法整体非法）；递归传 (min_val, max_val) 区间，或中序遍历严格递增；判空用 `is not None`，因为节点值可能为 0。
- [ ] **LC309 冷冻期三状态必须多元赋值**：`hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)` 一次赋值——day N 的 sold 依赖 day N-1 的 hold、hold 依赖旧 rest，依次更新会读到被覆盖的新值。**口诀**：状态之间有依赖就多元赋值。
- [ ] **LC105 重建二叉树先左后右**：preorder 指针是全局自增的，每建一个节点消耗一个元素；必须先递归左子树再递归右子树，顺序反了会建出错误结构；inorder 用哈希表存「值 → 索引」避免每次 index() 查找。
- [ ] **LC206 反转链表忘存 next 断链**：迭代版先 `next_temp = curr.next` 再改指向，三指针顺序不能乱；递归版反转后必须 `head.next = None` 断链，否则新链表尾部成环。

### 建议刷的新题
- [ ] **动态规划**：House Robber（Medium）— 关联已掌握 LC121/LC188 股票 DP 状态机。**核心**：一维 DP——`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`（偷当前则跳过前一家），可压缩为两个变量；本质是「选 / 不选」状态转移，与股票系列的 hold/not_hold 同构。**坑**：初始化注意 i=0、i=1 边界；别写成 `dp[i-1] + nums[i]`（相邻不能同时偷）。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握股票系列的状态转移思维。**核心**：斐波那契递推 `dp[i] = dp[i-1] + dp[i-2]`，可滚动变量 O(1) 空间；是面试 DP 入门必问，口述时讲清「为什么是加不是乘」。**坑**：n 小的时候别用递归（指数级重复计算），用迭代或记忆化。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree 递归比较。**核心**：对每个节点调用 isSameTree 判断子树是否相等，或先序遍历序列化后用 KMP/字符串匹配；是 LC100 的直接变体，练「树的遍历 + 分治」组合。**坑**：空树特判——subRoot 为空直接返回 true；别漏掉 root 自身相等的情况。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握 LC206 反转 + LC141 快慢指针 + LC19 找中点。**核心**：三步走——快慢指针找中点 → 反转后半段 → 交错合并两半；一道题串起链表三大基本功。**坑**：找中点时偶数长度要取「前半段最后一个」而不是后一半开头；合并时先存 next 再改指向，防止断链。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 中序遍历 + LC235 BST 性质。**核心**：BST 中序遍历即升序序列，中序递归/迭代计数到第 k 个即答案；或利用左子树大小做二分剪枝。**坑**：迭代版用栈模拟中序，注意 k 是 1-indexed（先 k-- 再判断）；递归版用全局计数器。

## 历史复习记录
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
