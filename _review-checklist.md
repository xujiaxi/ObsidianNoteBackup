# 🎯 面试复习清单

## 📅 今日复习（2026-07-13）

### 需要回顾
- [ ] **树与递归**：Invert Binary Tree（LC226）、Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Validate Binary Search Tree（LC98）、Lowest Common Ancestor of BST（LC235）、Construct Binary Tree from Preorder and Inorder（LC105）、Binary Tree Level Order Traversal（LC102）、LCA of Binary Tree（LC236）— **核心：递归套路三部曲（终止条件→递归调用→合并结果）；BST 验证必须传递 `min/max` 边界或利用中序遍历递增性；树构造题以 preorder 第一个元素切分 inorder 数组，递归构建左右子树；层序遍历 BFS 用 queue 模板。**
- [ ] **动态规划**：Best Time to Buy and Sell Stock III（LC123）、Maximum Subarray（LC53）-style Kadane — **核心：DP 三步法 — 定义状态 → 递推公式 → base case；股票系列在 Limited Transactions 场景下用 `dp[k][i] = max(dp[k][i-1], prices[i] - prices[j] + dp[k-1][j-1])`；Kadane 算法 `cur = max(num, cur + num), maxSum = max(maxSum, cur)` 本质上就是压缩到 O(1) 空间的 DP。**

### 重点坑
- [ ] **树递归栈溢出（StackOverflowError）**：当二叉树退化为链表（如只有左子树）时，递归 DFS 深度 = 节点数，可能栈溢出。解决：掌握迭代遍历（显式 Stack）、Morris Traversal（O(1) 空间）、或调大栈空间。面试时先问「树是否平衡」，再决定用递归还是迭代。
- [ ] **BST 验证只检查当前节点 vs 左右子节点**：错误写法 `if root.val <= left.val or root.val >= right.val`。必须传递 `(min, max)` 边界到递归函数，确保整个左子树所有值都 < root.val，整个右子树所有值都 > root.val。中序遍历解法只检查相邻递增，更简洁但无法处理重复值。
- [ ] **DP 状态定义不清晰**：最常见的错误是拿到题就开始想递推公式，没有先明确定义 `dp[i]` 代表什么。经验法则：先想清楚「以 i 结尾」还是「前 i 个元素」，状态定义不同直接决定递推方向。写出状态定义后用 small example 手推验证。

### 建议刷的新题
- [ ] **数组 / DP**：Maximum Subarray（Medium）— 关联已掌握知识：股票最佳买卖时机的一遍扫描思想（LC121）。Kadane 算法本质是「到当前位置为止的最大子数组和」的 DP，`dp[i] = max(nums[i], dp[i-1] + nums[i])`。面试最高频题之一，O(N) 时间 O(1) 空间，必须能秒。
- [ ] **DP**：House Robber（Medium）— 关联已掌握知识：动态规划基础（已做 5 道 DP）。一维 DP 入门模板：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，再压缩到 O(1) 空间。House Robber II（环形）是自然延伸，一题吃透两种变体。
- [ ] **图 / DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握知识：Number of Islands 的 DFS 沉岛（LC200）+ Clone Graph 的 BFS/DFS 遍历（LC133）。反向从边界向中间 DFS，分别标记能流入太平洋和大西洋的格子，取交集。面试高频图题。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口通用模板（LC3, LC76）。核心难点：维护窗口内最高频字符 `maxFreq`，当 `windowLen - maxFreq > k` 时收缩左指针。注意无需每次更新 maxFreq（只会变小，不会影响结果）。字节/TikTok 高频题。

## 历史复习记录
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
| Array | 1 | `array/` |
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

**Blind 75 完成：21 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
