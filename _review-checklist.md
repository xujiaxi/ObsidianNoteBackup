# 🎯 面试复习清单

## 📅 今日复习（2026-07-29）

### 需要回顾
- [ ] **树与递归**：Validate Binary Search Tree（LC98）、Construct Binary Tree from Preorder and Inorder Traversal（LC105）、Binary Tree Level Order Traversal（LC102）、Lowest Common Ancestor of BST（LC235）、Same Tree（LC100） — **核心：LC98 中序遍历必须严格递增——不能只比父子，要传 `min/max` 上下界（左子树所有节点 < root，右子树所有节点 > root）。LC105 `preorder[0]` 是 root，在 `inorder` 中找到 root 索引 `idx` → 左子树 `inorder[0..idx)` + 右子树 `inorder[idx+1..)`，递归切片构造，注意偏移量计算。LC102 BFS queue 层序遍历——用 `queue.size()` 记录当前层节点数，内层循环取完一层；也可 DFS 递归按 `depth` 追加到对应子数组。LC235 BST 的 LCA 性质：**p、q 都在左子树则 LCA 在左，都在右则 LCA 在右，第一次「分叉」的就是 LCA**；迭代版比递归更简洁。LC100 递归三问：都空 → true；一空一非空 → false；值相等 → 递归 `isSame(left.left, right.left) && isSame(left.right, right.right)`。**面试口述**：树题先想「递归 or 迭代」「BST 性质能不能用（LCA/查找）」「base case 是不是 null」。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）、Longest Common Prefix（LC14） — **核心：LC3 无重复最长子串——`right` 右扩、遇到重复 `char` 就 `left` 缩直到去掉重复；用 `HashMap<Char, Index>` 记录上次出现位置，`left = max(left, map[char]+1)` 直接跳过而非一步步缩。LC76 最小覆盖子串——**模板**：`right` 右扩累计数直到满足、`left` 内层 while 收缩直到不满足，收缩时判断是否更新最短窗口；`need` 计数器 + `valid` 已匹配数，当 `valid == need.size()` 时收缩。LC14 最长公共前缀——**二分法**：取最短串长度 `minLen`，二分 `mid`，比较所有串前 `mid` 字符是否相等；或**纵向扫描**：按列比较，第一个不匹配的列返回前缀。**坑**：LC76 收缩时 `valid--` 的条件是「该字符原本是需要的（count 在 need 中 > 0）」才减，否则不减——防止 `s = "a"` 但 `t = "aa"` 的边界。**面试口述**：滑窗通用模板——外层 `right++` 扩、满足条件后内层 `left++` 收、更新答案；先问清楚「窗口内是什么」「何时收缩」。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock（LC121）、Best Time to Buy and Sell Stock IV（LC188）、Best Time to Buy and Sell Stock with Cooldown（LC309） — **核心：LC121 一次交易——`minPrice = min(minPrice, price)`、`profit = max(profit, price - minPrice)`，本质 DP 退化。LC188 k 次交易——状态机：`hold[i][j]` 第 j 次持有 / `sold[i][j]` 第 j 次不持有；转移 `hold = max(hold, sold[j-1] - price)`、`sold = max(sold, hold + price)`；空间优化滚动数组用 `hold[]` 和 `sold[]`，注意 `j-1` 要用上一轮的值（不能覆盖）。LC309 冷冻期——三状态：`hold`（持有）、`sold`（今天卖出）、`rest`（非持有且冷冻）；转移 `rest[i] = max(rest[i-1], sold[i-1])`（昨天卖或昨天就 rest）、`hold = max(hold, rest - price)`（只能从 rest 买不能从刚卖的 sold 买）、`sold = hold + price`。**坑**：LC188 当 `k >= n/2` 时退化为无限次交易（贪心），因为最多做 `n/2` 次完整买卖；否则 DP 否则 O(nk) 会 MLE。**面试口述**：股票系列万能框架——画状态机「持有/不持有」+ 每个约束（交易次数/冷冻期/手续费）多加一个状态或维度。**

### 重点坑
- [ ] **LC98 BST 验证「只比父子不够，要传 min/max 范围」**：写 `isValid(root.left, root.val)` 漏了上界限制——左子树的右孩子也必须 < root.val，右子树的左孩子也必须 > root.val。**正确写法**：`isValid(node, min, max)` → 左子递归 `isValid(left, min, node.val)`、右子递归 `isValid(right, node.val, max)`，任一节点超出 `(min, max)` 开区间即非法。**坑**：若用 Integer 范围做初始值 `min=-∞, max=+∞`，用 `Long` 或 `null + 单独判断` 避免 `Integer.MIN_VALUE` 本身就是合法节点值但被边界误杀。
- [ ] **LC105 重建树「偏移量计算」与「找 root 索引效率」**：`preorder` 的 root 在 `preStart + k`（k 是左子树大小），`inorder` 切分后递归要用相对偏移而非全局索引。**坑**：每次在 `inorder` 中遍历找 `rootVal` 是 O(n)，总复杂度 O(n²)——用 `HashMap<val, idx>` 预建索引降到 O(n)。递归终止条件 `preStart > preEnd` 不能写成 `>=`（会漏掉单节点子树）。
- [ ] **LC76 最小窗口子串「valid 计数器增减条件」**：`valid` 只在「窗口中该字符数 <= 需要数」时才 `++`，超出后再加不算 match。收缩时要把 `need[c]` 加回来判断是否「从刚好够变成不够」才 `valid--`。**坑**：`need` 是固定需求（来自 t），`window` 是动态窗口计数——`valid == need.size()`（去重后不同字符数）不是 `need.length()`（含重复字符）；忽略这层关系会导致永远不收缩或过早收缩。
- [ ] **LC309 冷冻期「sold 不能直接到 hold，必须经过 rest」**：写成 `hold = max(hold, sold - price)` 是错的——刚卖出的当天不能买回（冷冻期约束）。**正确**：`hold` 只能从 `rest` 买入，`sold` 先变成 `rest`（隔一天）才能再买入。**坑**：三状态 DP 容易漏掉 `rest` 状态，把 `sold` 和 `rest` 合并会导致「今天卖、明天买」的非法转移；初始化 `hold = -prices[0]`、`sold = 0`、`rest = 0`，不能只用一维数组滚动（同一天会互相依赖，要先计算依赖少的）。
- [ ] **LC188「k >= n/2 退化贪心」与「sold[j-1] 必须用上一轮」**：当 k 足够大（2k ≥ n）时，状态机 DP 退化为无限次交易——此时做 `sum(max(0, prices[i]-prices[i-1]))` 贪心即可，否则 O(nk) 会 Memory Limit Exceeded。**坑**：滚动数组优化时 `sold[j]` 依赖 `sold[j]`（不卖）和 `hold[j] + price`（卖），`hold[j]` 依赖 `hold[j]` 和 `sold[j-1] - price`——`sold[j-1]` 是「上一次交易」的卖出收益，必须用上一轮迭代结果，顺序遍历 `j` 时如果先更新 `sold[j-1]` 再更新 `hold[j]` 会错用当前轮的值。

### 建议刷的新题
- [ ] **DP**：House Robber（Easy）— 关联已掌握 LC53 Kadane、LC121/122 股票 DP。**核心**：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，决策「偷当前 + 隔一个」vs 「不偷当前」。**坑**：只与前两个状态相关，可空间优化到 O(1)（两个变量滚动）；打基础后再推 Robber II 环形版（首尾不相邻需分类讨论「偷首 vs 偷尾」）。
- [ ] **DP**：Decode Ways（Medium）— 关联已掌握 LC309 多状态 DP、LC14 字符串处理。**核心**：`dp[i] = dp[i-1] * (s[i] != '0') + dp[i-2] * (1 <= s[i-1..i] <= 26)`；当前字符单独成码（非 0）+ 与前一个字符组合成 1-26 两种情况相加。**坑**：前导 0 是非法编码，`s[0]=='0'` 直接返回 0；`dp[0] = 1`（空串）但要从 `dp[i-2]` 初始化时小心下标越界；`10` 和 `20` 这种 `s[i]=='0'` 必须与前字符组合，不能单独算 `dp[i-1]` 分支。
- [ ] **字符串**：Valid Palindrome（Easy）— 关联已掌握 LC3 双指针、LC14 字符串遍历。**核心**：左右双指针从两端向中间扫，跳过非字母数字字符，小写化后比较；`Character.isLetterOrDigit()` 预过滤。**坑**：`Character.toLowerCase()` 调用前必须先 `isLetterOrDigit` 判断（对非字母数字调 `toLowerCase` 无害但浪费）；空串和纯符号串都是合法回文。
- [ ] **数组 & 间隔**：Merge Intervals（Medium）— 关联已掌握 LC253 Meeting Rooms II（堆/排序）、LC188 股票状态机思路。**核心**：按 `start` 排序后线性扫描——若 `curr.start <= result[-1].end` 则合并（`end = max(end, curr.end)`），否则追加新区间。**坑**：合并时取 `max(end, curr.end)` 而非直接用 `curr.end`（原区间可能更长）；排序比较器要稳定（`a[0] - b[0]` 在 Integer 范围内安全但负数溢出风险，用 `Integer.compare` 更稳）。
- [ ] **数组 & 双指针**：3Sum（Medium）— 关联已掌握 LC1 Two Sum、LC19 双指针、LC53 数组遍历。**核心**：排序 + 固定一个数 `nums[i]` + 双指针 `[i+1, n-1]` 找两数之和 = `-nums[i]`；找到一组后左右指针都要跳过 duplicates。**坑**：三层去重——`nums[i] == nums[i-1]` 跳过固定数、左指针跳过相同值、右指针跳过相同值；时间 O(n²)，外层 `i` 只到 `n-2`（后面双指针不够用就停）。

## 历史复习记录
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
**总共 LeetCode 完成：32 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
