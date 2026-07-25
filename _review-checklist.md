# 🎯 面试复习清单

## 📅 今日复习（2026-07-24）

### 需要回顾
- [ ] **树与递归**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert/Flip Binary Tree（LC226）、Binary Tree Level Order Traversal（LC102）、Construct Binary Tree from Preorder and Inorder Traversal（LC105）、Validate Binary Search Tree（LC98）、Lowest Common Ancestor of BST（LC235）— **核心：LC104 DFS `return 1 + max(depth(left), depth(right))` 或 BFS 层序计数。LC100 递归 `isSameTree(p, q) = p.val == q.val && isSameTree(p.left, q.left) && isSameTree(p.right, q.right)`，base case 处理 null。LC226 递归交换 `swap(root.left, root.right)` 后递归左右子树。LC102 BFS 用 Queue 逐层 poll、记录 size 控制分层。LC105 preorder[0]=root，在 inorder 中定位 root 索引 split，左子树 preorder[1..idx+1]、inorder[0..idx]，右子树 preorder[idx+1..]、inorder[idx+1..]。LC98 中序遍历应严格递增——维护 `prev` 全局变量比较 `root.val > prev`，不能只比较 parent-child（局部有序≠全局 BST）。LC235 BST 的 LCA：利用 BST 性质，p、q 都小于 root 则递归左子树，都大于则递归右子树，分叉点即 LCA。**
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：LC133 HashMap<Node, NodeClone> 避免重复克隆+环，DFS 递归先 clone 邻居再 return；BFS 用 Queue 逐层克隆邻居。LC207 拓扑排序检测环——建邻接表 + 入度数组，BFS（Kahn's Algorithm）入度为 0 的先入队，队空时若遍历节点数 ≠ 总节点数则有环；或 DFS 三色标记法（white/gray/black，遇到 gray 即有环）。LC200 沉岛算法——遍历网格遇到 '1' 即 DFS/BFS 标记整个连通块为 '0'（直接改原矩阵避免 visited 数组开销），计数即可。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、Best Time to Buy and Sell Stock II（LC122）、Best Time to Buy and Sell Stock III（LC123）、Best Time to Buy and Sell Stock IV（LC188）、Best Time to Buy and Sell Stock with Cooldown（LC309）、Best Time to Buy and Sell Stock with Transaction Fee（LC714）— **核心：LC121 一次遍历维护 minPrice 和 maxProfit 贪心。LC122 可以无限次交易，每天只要 `prices[i] > prices[i-1]` 就累加收益（贪心）或 dp[i][hold] 状态机。LC123 最多 2 次交易——4 个状态变量 `buy1/sell1/buy2/sell2`，每次更新取 max。LC188 最多 k 次交易——通用化 LC123 到 k 维，注意 k ≥ n/2 时退化为 LC122。LC309 加 cooldown——卖出后第二天不能买入，状态机 `hold/sold/cooldown` 三态转移。LC714 加交易费——卖出时减 fee，dp[i][hold/sold] 状态机。**

### 重点坑
- [ ] **LC98 Validate BST 的中序遍历「全局 prev」陷阱**：不能只比较 `node.val > node.left.val && node.val < node.right.val`（这只能保证局部父子有序，不能保证整棵树满足 BST 性质——右子树的最小值必须大于根，而不仅是右孩子）。正确做法：中序遍历维护全局 `prev` 变量，每次访问节点检查 `node.val > prev`，更新 `prev = node.val`。用 `Long.MIN_VALUE` 初始化 prev 可以处理 `Integer.MIN_VALUE` 边界，或用 `Integer` 包装类 + null 判断。**易错**：把 prev 传入递归参数用值传递（Java int）不会回传更新，必须用实例变量或 `AtomicInteger`/`long[]` 数组。
- [ ] **LC105 Construct Binary Tree 的 preorder/inorder 索引边界**：preorder 第一个元素是 root，在 inorder 中找到 root 的索引 `idx` 后，**左子树元素个数 = idx**（不是 idx+1）。切分时 preorder 左 = `[1, 1+idx)`、preorder 右 = `[1+idx, end)`；inorder 左 = `[0, idx)`、inorder 右 = `[idx+1, end)`。**最易错**：把左右子树在 preorder 里的偏移量算错（左子树 preorder 长度应等于 inorder 左长度 idx），以及用 `indexOf` 在含重复元素时定位错误（题目保证无重复值，但面试时需口述这个前提）。
- [ ] **LC207 Course Schedule 的入度数组 vs 三色标记法混淆**：BFS 拓扑排序（Kahn's）——入度数组 `indegree[]`，每条边 `prereq → course` 时 `indegree[course]++`，初始把所有入度为 0 的节点入队，pop 时对邻居 `indegree--` 归零再入队，最终 `visitedCount == numCourses` 则无环。DFS 三色标记法——`0=white(未访问), 1=gray(访问中), 2=black(已完成)`，遇到 gray 节点说明回边即有环。**坑**：BFS 版本初始入队多个入度为 0 的节点时要全部入队（不能只入第一个），否则漏判；DFS 版本必须把已确认无环的节点标记为 black，避免被不同路径重复访问误判为环（gray≠black）。
- [ ] **LC309/LC714 股票状态机的 cooldown/fee 状态转移**：LC309 三态——`hold = max(hold, rest - price)`（今天买入，前一天必须是 rest 才能 buy）、`sold = hold + price`（今天卖出）、`rest = max(rest, sold)`（今天不操作，且刚卖完不能立刻买，所以 rest 来源是 sold）。**最易错**：cooldown 不是简单的「卖完跳过一天」，而是 hold 不能从 sold 直接转移（`hold` 只能从 `rest` 转移，不能从 `sold`）。LC714 的手续费——`sell` 状态加 `fee`（或 `buy` 状态减 fee），注意 fee 扣在买入还是卖出端看题目定义，通常扣在卖出 `sold = hold + price - fee`。
- [ ] **LC188 当 k ≥ n/2 时退化处理**：当 `k >= prices.length / 2` 时，交易次数不再是瓶颈，问题退化为 LC122（无限次交易），用贪心累加所有正差价即可，O(n) O(1)。不做这个判断直接用 3D DP（n×k×2）会导致内存和时间浪费甚至 TLE。**面试口述**：先判断 k 与 n/2 的关系选择最优解法，体现代码对不同规模的敏感度。

### 建议刷的新题
- [ ] **动态规划**：House Robber（Easy）— 关联已掌握 LC121/LC122 股票系列的状态机 DP 思路。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，抢当前房子则不能抢前一栋（dp[i-2]+nums[i]），不抢则继承 dp[i-1]。**坑**：空间可优化为 O(1) 用两个变量滚动；base case `dp[0]=nums[0], dp[1]=max(nums[0], nums[1])`。
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握股票 DP 的状态转移思想。**核心**：`dp[i] = dp[i-1] + dp[i-2]`（斐波那契变形），到第 n 阶只能从 n-1 或 n-2 跳上来。**坑**：n=1 和 n=2 单独处理；空间可优化为 O(1) 滚动两变量，面试时从 O(n) 空间讲到滚动优化体现递进思维。
- [ ] **树/Trie**：Implement Trie (Prefix Tree)（Medium）— 关联已掌握 LC105/LC226 树的递归结构 + LC3/LC76 字符串处理。**核心**：TrieNode 含 `children[26]` 和 `isEnd` 标志，insert 逐字符向下走不存在则新建，search 逐字符走到底检查 isEnd，startsWith 不检查 isEnd。**坑**：面试常 Follow-up 优化空间（HashMap 代替固定数组节省空节点），以及理解 Trie 适合前缀匹配的场景（搜索引擎自动补全、IP 路由）。
- [ ] **字符串/双指针**：Valid Palindrome（Easy）— 关联已掌握 LC3 字符串遍历 + LC141 双指针思路。**核心**：双指针从两端向中间走，跳过非字母数字字符（`Character.isLetterOrDigit`），比较小写化后的字符。**坑**：空串和纯符号串返回 true；Java 用 `Character.toLowerCase` 统一大小写；不能用 `reverse().equals()` 因为那要 O(n) 空间，双指针 O(1) 空间更优。
- [ ] **堆/优先队列**：Top K Frequent Elements（Medium）— 关联已掌握 LC1 HashMap 计数 + LC253 Meeting Rooms II 的优先队列使用。**核心**：先 HashMap 统计频次，再用最小堆维护 size=k 的堆（堆顶最小，Poll 超出 k 的），最后剩余即前 k 高频。**坑**：也可用桶排序（bucket[freq] = list of nums）O(n) 但空间取决于最大频次；PriorityQueue 的 Comparator 按 value（频次）排序而非 key；`O(n log k)` 堆解法 vs `O(n)` 桶排序解法，面试需口述两种空间的 trade-off。

## 历史复习记录
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
