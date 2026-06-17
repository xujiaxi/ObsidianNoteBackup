# 🎯 面试复习清单

## 📅 今日复习（2026-06-16）

### 需要回顾
- [ ] **树深度/BST**：LC104 最大深度 + LC226 翻转二叉树 + LC235 BST 最低公共祖先 — **核心：递归函数的定义（返回什么）、base case（null 节点返回 0/空）。翻转二叉树递归交换左右子树；LCA BST 利用 BST 性质 `root.val > p.val && root.val > q.val` 则 LCA 在左子树**。注意递归终止条件和返回值不要遗漏。
- [ Terminal Node 构造 — LC105 从前序+中序构造二叉树 — **核心：前序首元素是根，在中序中找到根位置分左/右子树，递归构造**。注意构造时先构造根节点再递归，返回根。索引计算不要越界。
- [ ] **链表综合**：LC206 反转链表 + LC141 环检测（快慢指针）+ LC21 合并两个有序链表 + LC19 删除倒数 N — **核心：虚拟头节点（Dummy Node）处理边界；反转链表用三个指针 prev/curr/next 迭代；环检测用快慢指针，相遇即有环**。注意删除倒数 N 时用快指针先走 N 步。

### 重点坑
- [ ] **二叉树递归返回值类型不一致** — 有些题返回节点（构造/翻转），有些返回深度（最大深度），有些返回路径和。写之前先明确递归函数签名和返回值。
- [ ] **LCA BST 条件判断** — 不要写成 `root.val > p.val && root.val > q.val`，应该判断 `p.val < root.val && q.val < root.val` 则向左。面试时容易手误把 && 写成 ||。
- [ ] **前序+中序构造二叉树索引越界** — 中序中根的位置划分左右子树后，前序的范围要对应调整。建议画图辅助索引计算，或用 HashMap 缓存中序值→索引映射。
- [ ] **链表反转时指针丢失** — 反转前要先保存 `next = curr.next`，再改 `curr.next = prev`。顺序错一步就会断链。建议纸笔模拟一遍。
- [ ] **快慢指针初始位置** — 环检测时 slow/fast 都从头开始；删除倒数 N 时 fast 先走 N 步。不同题目快慢指针初始位置不同，不要想当然都从头开始。

### 建议刷的新题
- [ ] **动态规划**：Climbing Stairs（Easy）— 关联已掌握递归思维，**`dp[i] = dp[i-1] + dp[i-2]`**，是理解 DP 状态转移的最佳热身题。可进一步做 Coin Change 入门背包。
- [ ] **数组**：Maximum Subarray（Medium）— 关联已掌握滑动窗口/前缀和思想，**Kadane 算法：维护以当前元素结尾的最大子数组和**，`dp[i] = max(nums[i], dp[i-1] + nums[i])`，空间可优化到 O(1)。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 合并两个有序链表 + 堆/分治，**PriorityQueue 维护 k 个头节点不断 poll/offer，或归并分治合并**。是链表进阶必刷题。
- [ ] **树**：Validate Binary Search Tree（Medium）— 关联已掌握树递归，**递归时传入 min/max 区间约束当前节点值范围**，或者中序遍历验证严格递增。注意不是 `root.val > left && root.val < right`，而是整个子树都在区间内。
- [ ] **字符串**：Valid Anagram（Easy）— 关联已掌握 HashMap/数组计数，**用数组 26/128/256 统计字符频率，比较两个字符串频率是否一致**。是字符串 Hash 计数的基础题。

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Design | 2 | `design/` |
| Array | 1 | `array/` |
| Heap | 1 | `heap/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Dynamic Programming | 0 | `dynamic-programming/` |
| Greedy | 0 | `greedy/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| String | 0 | `string/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：23 题**

## 待复习（按优先级）

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
