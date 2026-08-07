# 🎯 面试复习清单

## 📅 今日复习（2026-08-06）

### 需要回顾
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76） — **核心：LC3 双指针 + HashMap——`left = max(left, map.get(c) + 1)`（存字符最近下标+1，left 只增不减），每次 `ans = max(ans, right - left + 1)`，先查旧值再 put 新下标；LC76 通用模板——外层 while 扩右指针、用 `int[128]` 计数（比 HashMap 快），`required == 0` 时内层 while 收缩左指针并更新最小窗口，收缩时同步恢复计数与 required。**面试口述**：滑动窗口题先问「窗口收缩条件是什么」——LC3 是「出现重复字符」、LC76 是「已包含 t 全部字符」，再套模板；固定窗口 vs 可变窗口的收缩时机不同。**坑：LC3 left 必须取 max 不能直接赋 `map.get(c)+1`（可能回退）；LC76 收缩时漏恢复计数会导致后续窗口永远无效。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、II（LC122）、III（LC123）、IV（LC188）、Cooldown（LC309）、Transaction Fee（LC714） — **核心：LC121 一遍扫描维护 `min_price`，每天算 `profit = max(profit, price - min_price)`；LC122 无限次——贪心累加所有正差价 `prices[i] > prices[i-1]`；LC123/188 有限次——状态机 `buy[k]`/`sell[k]`，按 buy→sell→buy→sell 顺序更新；LC309 冷却——需要 rest 状态或记录前一天 sell，卖出后隔一天才能买；LC714 手续费——统一在买入或卖出时扣一次 fee。**面试口述**：股票题先确定「交易次数限制 + 是否冷却/手续费」，再选贪心 or 状态机；有限次 k 较大时降级为无限次。**坑：LC121 不是「全局最大减全局最小」（最大可能出现在最小之前，如 [3,2,6,5,0,3] 应得 4 不是 3）；LC188 k > n/2 必须降级否则超时；LC309 两状态会忽略冷却限制。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Tree（LC226）、Level Order（LC102）、Construct from Preorder+Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235）、LCA of Binary Tree（LC236） — **核心：递归三步——base case（null）、分解、合并；LC102 BFS 每层先记 `size = q.size()`；LC105 前序第一个是根、中序定位根切分左右，HashMap 存中序下标 O(1) 定位；LC98 必须传 min/max 上下界递归校验；LC236 后序遍历——左右都非空则当前节点即 LCA。**面试口述**：树题先问「递归 or 迭代」「是否需要父指针」；BST 题优先想中序遍历（有序）与上下界剪枝。**坑：LC98 只比较相邻节点会漏判 `[5,1,4,null,null,3,6]`；LC105 中序下标不用 HashMap 会 O(n²)，且切片边界易错；LC236 返回值语义（找到 p/q vs 找到 LCA）要分清。**

### 重点坑
- [ ] **LC3 滑动窗口「map 存 index+1、left 只增不减、先查后存」**：重复字符出现时 `left = max(left, map.get(c) + 1)`——直接赋值可能把 left 回退导致窗口内仍有重复；必须先取旧值更新 left 再 put 新下标，顺序反了会用新下标算 left。**坑**：用 HashSet + 删除法也能做但复杂度退化，HashMap 记录下标是标准解。
- [ ] **LC76 滑动窗口「required == 0 才收缩 + 收缩后必须恢复计数」**：`required = t.length()`，扩张时 `need[c]--` 后若 `>= 0`（说明这字符是 t 需要的）才 `required--`；收缩 left 时 `need[c]++` 后若 `> 0` 则 `required++`——漏掉恢复步骤，后续窗口将永远无法再次变有效。**坑**：`required` 只在「从不足跨过满足」时递减，别对每个字符都减。
- [ ] **LC121 股票「不是全局最大减全局最小」**：最高价可能出现在最低价之前（[3,2,6,5,0,3] 全局 max 3 - min 0 = 3，但正确答案是 2 买 6 卖 = 4）。**正确**：一遍扫描维护 `min_price`，每天 `profit = max(profit, price - min_price)`，保证「先买后卖」的顺序约束。
- [ ] **LC188/LC309 股票「k 过大降级 + 冷却需要第三状态」**：LC188 当 `k >= n/2` 时等价无限次交易，直接套 LC122 贪心，否则 k 维 DP 会 TLE/MLE；LC309 只有 hold/cash 两状态无法表达「卖出的第二天不能买」，要加 rest 状态或用变量记录前一天是否刚卖出。
- [ ] **LC98 验证 BST「必须传上下界，不能只比较相邻节点」**：`[5,1,4,null,null,3,6]` 中根 5 的右子树里有 3（小于 5）——只比较父节点会误判合法。**正确**：递归传 `(node.left, min, node.val)` / `(node.right, node.val, max)`，或用中序遍历检查严格递增。

### 建议刷的新题
- [ ] **滑动窗口 / 字符串**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：窗口内维护 `max_freq`，`window_len - max_freq <= k` 说明可全变成同一字符，否则收缩 left；`max_freq` 只增不减（历史最大值）不影响正确性且避免收缩时重新计算。**坑**：收缩时不要递减 max_freq；字符集固定（26 字母）时用数组计数。
- [ ] **DP**：House Robber（Medium）— 关联已掌握股票系列「选 or 不选」状态机思维。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`（不偷当前 vs 偷当前），滚动两个变量 O(1) 空间。**坑**：i=1 边界（`dp[i-2]` 越界）；与股票题一样都是「每个位置做决策 + 状态转移」的套路。
- [ ] **DP**：Climbing Stairs（Easy）— 关联已掌握股票 DP 递推基础。**核心**：`dp[i] = dp[i-1] + dp[i-2]`（最后一步跨 1 阶或 2 阶），斐波那契数列，滚动变量 O(1)。**坑**：n=1 时直接返回 1；从 n=2 开始递推，别把下标写乱。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree 精确递归比较。**核心**：双重递归——外层遍历 root 每个节点，内层 `isSameTree` 精确比较（含 null 结构）；`isSubtree = isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)`。**坑**：子树要求结构完全一致，isSameTree 的 null 处理要对称。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 Validate BST 中序遍历。**核心**：BST 中序遍历即升序序列，迭代栈模拟中序，k 递减到 0 时返回当前节点 O(H+k)；进阶用子树节点数 `left_size` 剪枝 O(H)。**坑**：迭代中序要「一路向左压栈，弹出后转向右子树」，别忘转向；k 是 1-indexed。

## 历史复习记录
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
