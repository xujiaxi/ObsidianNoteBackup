# 🎯 面试复习清单

## 📅 今日复习（2026-07-18）

### 需要回顾
- [ ] **树与递归**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Validate BST（LC98）— **核心：LC104 三种写法——递归 DFS（`max(depth(left), depth(right)) + 1`）、BFS（逐层遍历计数）、迭代 DFS（栈里存 `(node, depth)` 对）。LC100 递归判定结构一致：两空树 true、一边空一边非空 false、值相等且左右子树都相同。LC226 一行递归 `swap(left, right)` 后递归子树（前序位 swap）；也可迭代 deque 做 BFS 逐层 swap。LC98 中序遍历必须用 prev 全局/引用变量才比较，BST 不能只看 `node.left.val < node.val`——必须保证整个左子树的最大值 < root < 整个右子树的最小值，常见错误是只比较直接父子。**
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：LC133 克隆图——HashMap `oldToNew` 既做映射又做 visited，BFS 取邻居时 on-the-fly 创建克隆节点并入队，避免重复克隆。LC207 三色标记法（WHITE/GRAY/BLACK）检测环：GRAY 表示当前 DFS 栈中（回边出现即环），BLACK 表示已完成可缓存跳过；也可 Kahn's BFS（拓扑排序入度减一）。LC200 沉岛算法/BFS 或 DFS：访问过的 `'1'` 就地改 `'0'`（沉岛）省 visited 空间，每次从新 `'1'` 触发一次 BFS/DFS 即一个岛。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating（LC3）、Minimum Window Substring（LC76）— **核心：LC3 经典双指针滑动窗口——`right` 扩展，遇到重复 char 时 `left = max(left, charIndex[char] + 1)`（注意用最近出现位置而不是简单 left++）；HashMap 存 `char → 最近 index` 一遍扫完 O(n)。LC76 最小覆盖子串——`right` 扩展找满足，`left` 收缩找最优，maintain 一个 `formed` 计数表示「已满足的字符种类数」；满足时记录 `minLen, start`；window contract 后要把移出去字符放回 need 计数。LC76 与 LC3 模板一致但 need/dict 更复杂。**

### 重点坑
- [ ] **Validate BST 的局部比较陷阱**：`node.left.val < node.val < node.right.val` 不充分！反例：`[5,1,8,null,6]`（root=5，左子树含 6）—— `5 < 6 < 8` 本身成立，但 6 在 5 的左子树中违反 BST 性质。**正确做法**：中序遍历 + prev 指针，每次比较 `prev < curr`；或递归传递 `(minBound, maxBound)`，每进入左子树 `max = node.val`，每进入右子树 `min = node.val`，根节点用 `(−∞, +∞)`。
- [ ] **Clone Graph 的 HashMap 双重用途**：`oldToNew` map 起两个作用——①判 visited（key 存在表示已克隆）②查克隆目标。**常见坑**：BFS 时邻居是已克隆过的节点（map 命中）应直接用 map 取克隆，未克隆的才创建并入队；写代码时容易把「已克隆」和「未克隆」走同一个分支，导致重复克隆或漏切边。Python 中可用 `if neighbor not in oldToNew` 单条件区分；Java 中用 `containsKey`。
- [ ] **Longest Substring Without Repeating 的 `left` 更新方式**：错误写法 `if s[right] in seen: left = seen[s[right]] + 1`——会回退 left！比如 `abba` 在 right=3（a）时 seen[a]=0，`left = 1` 是错的。**必须 `left = max(left, seen[s[right]] + 1)`**，保证 left 永不后退（滑动窗口只前进不回退）。同时更新 `seen[s[right]] = right` 必须放在 left 更新之后，否则 left 算错。
- [ ] **Course Schedule 的三色标记顺序**：DFS 中先置 GRAY 再进递归，BLACK 置在所有邻居访问完之后。漏置 GRAY 会导致自环或交叉边误判为环。Kahn's BFS 用入度队列而非 visited，注意初始化时入度 0 的节点全部入队，每弹出一次出列的节点数若 < n 即存在环。

### 建议刷的新题
- [ ] **树**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握 LC104 / LC226（递归返回最大深度）+ LC98（递归传参边界）。**核心**：递归「从当前节点向下走最大单边路径」`gain = max(0, left + right) + node.val`（负贡献剪枝为 0），同时维护全局 `maxSum = max(maxSum, left + right + node.val)`（左右都向下的完整路径）。**坑**：节点值可为负，绕过负子树；返回给父节点的只能是一条单边路径，不能两条都返回。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree。**核心**：对 s 的每个节点做根调用 LC100 判定，匹配即真；可以预处理 s、t 各自 DFS 序列化字符串，再 KMP/字符串匹配 O(|s|+|t|)。**坑**：直接 `s == t` 判等没考虑子树本身，要靠遍历每个节点为候选根。
- [ ] **树**：Construct Binary Tree from Preorder and Inorder Traversal（Medium，已做但建议快默写一遍）— 关联已掌握 LC105（基础）；考试中高频变形题如「Preorder + Postorder」、「Inorder + Postorder」。**核心**：preorder 首元素即根，在 inorder 中找根位置切分左右子树，递归构造；HashMap 缓存 inorder 中值的位置 O(n)。**坑**：边界 `preStart > preEnd` 返 null，不要写越界；下标计算时 left 子树长度 = rootIndexInorder - inStart。
- [ ] **图论/BFS**：Rotting Oranges（Medium，非 Blind75 但与 LC200 同类型）— 关联已掌握 LC200 Number of Islands。**核心**：多源 BFS——所有初始腐烂橘子同时入队当 level 0，每次扩展一层算时间+1，最终感染全部新鲜橘子的最小分钟。**坑**：最后扫一遍 grid 看是否还有新鲜橘子，有则返回 -1；初始若无新鲜橘子直接返回 0 不必 BFS。
- [ ] **动态规划入门**：Climbing Stairs（Easy）— 关联已掌握 LC121 Best Time to Buy and Sell Stock（状态 DP 入门）。**核心**：`dp[i] = dp[i-1] + dp[i-2]`（斐波那契数列变体），两种状态转移——从第 i-1 阶一步跨上来或从第 i-2 阶跨两步，空间优化用两个变量滚动即可（O(1)）。**坑**：base case `dp[1]=1, dp[2]=2` 容易写反；用变量滚动时注意更新顺序——`prev2 → prev1 → cur`。

## 历史复习记录
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
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 2 | `array/` |
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
