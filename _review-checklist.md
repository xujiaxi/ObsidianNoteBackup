# 🎯 面试复习清单

## 📅 今日复习（2026-07-16）

### 需要回顾
- [ ] **树与递归**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Binary Tree Level Order Traversal（LC102）、Validate BST（LC98）、Construct Binary Tree from Preorder+Inorder（LC105）、LCA of BST（LC235）、LCA of Binary Tree（LC236）— **核心：所有树题的根基是递归三步法（base case → 递归处理子树 → 合并结果）。LC102 层序遍历用 BFS + Queue 逐层处理；LC98 验证 BST 用中序遍历递增性（注意不能只比父子，要用 min/max 上下界传递）；LC105 构建树用 preorder[0] 定根、inorder 找根位置切分左右子树；LC236 LCA 用后序遍历——左右子树分别找到 p/q 则当前节点即为答案。**
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Clone Graph（LC133）、Course Schedule（LC207）— **核心：LC200 沉岛算法——DFS 遇到 '1' 就标记为 '0'（原地修改省空间），或用 visited Set。LC133 克隆图用 HashMap 记录 oldNode→newNode 映射，BFS/DFS 遍历邻居时递归克隆。LC207 拓扑排序检测环——Kahn's BFS（入度队列）或 DFS 三色标记法（0=未访问, 1=访问中, 2=已完成），遇到灰色节点说明有环。**

### 重点坑
- [ ] **Validate BST 中序遍历陷阱**：不能只比较 node.val 与 node.left.val / node.right.val！因为右子树的最左下角可能小于根。正确做法是用 `(min, max)` 上下界递归传递：`isValid(node, min, max)`，每次更新左子树上界=当前值、右子树下界=当前值。中序遍历法需维护全局 `prev` 变量，检查 `curr > prev`。
- [ ] **LCA of Binary Tree 的 null 返回值语义**：LC236 中后序遍历返回值有双重含义——找到目标节点返回该节点，未找到返回 null，两个子树都返回非 null 时当前节点就是 LCA。常见错误：找到一侧就提前返回，漏掉另一侧可能找到更深的 LCA。必须递归完左右子树再判断。
- [ ] **Course Schedule 邻接表建表方向**：`prerequisites[i] = [a, b]` 表示「要上 a 必须先上 b」，即 b→a 的边（b 是 a 的前驱）。建图时 `graph[b].add(a)` 并 `indegree[a]++`。方向搞反导致拓扑排序全部出错。

### 建议刷的新题
- [ ] **树/DFS**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握树的后序遍历递归（LC236 LCA）+ LC104 最大深度。核心：后序遍历计算「经过当前节点的最大路径和」= 当前节点值 + max(0, 左子树贡献) + max(0, 右子树贡献)，用全局变量追踪最大值。难点在于区分「全局路径」和「向上返回的单边贡献」。
- [ ] **图/DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 Number of Islands（LC200）DFS 沉岛思路。从四条边界向中间反向 DFS，分别标记能流入太平洋和大西洋的格子，最后取交集。核心思想：反向推导比正向模拟简单得多。
- [ ] **树/序列化**：Serialize and Deserialize Binary Tree（Hard）— 关联已掌握 LC105 构建树（preorder+inorder）+ LC102 层序遍历。用 BFS 层序序列化为字符串（null 用 # 占位），反序列化时用 Queue 逐层重建。面试高频设计题，考的是树的完整遍历与重建。
- [ ] **树/Trie**：Implement Trie (Prefix Tree)（Medium）— 关联已掌握树的递归结构与 DFS 遍历。Trie 本质是 N 叉树，每个节点含 children[26] + isEnd 标志。insert/search/startsWith 三方法，掌握后可拓展到 LC211 Add and Search Word（通配符 `.` 的 DFS）。
- [ ] **堆**：Top K Frequent Elements（Medium）— 关联已掌握 HashMap 计数（LC1 Two Sum）+ LC253 Meeting Rooms II 堆应用。先用 HashMap 频率统计，再用小顶堆（容量 K）或桶排序（按频率分桶）求 Top K。桶排序 O(N) 比堆 O(N log K) 更优，面试常考两种解法对比。

## 历史复习记录
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
