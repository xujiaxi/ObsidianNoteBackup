# 🎯 面试复习清单

## 📅 今日复习（2026-08-10）

### 需要回顾
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针迭代 `prev/curr/next`——先保存 `next` 再改 `curr.next = prev`，最后整体右移；递归版 `head.next.next = head` 后置空 `head.next` 防环。LC141 快慢指针——快指针每次两步、慢指针一步，相遇即有环；要处理空链表/单节点。LC21 哨兵 dummy 节点 + 双指针比较，谁小接谁，收尾接剩余链表。LC19 快指针先走 n 步，再快慢同步走，慢指针停在待删节点**前一个**，配合 dummy 处理删头节点。**面试口述**：链表题先问「能否修改原链表」「是否允许额外空间」；删除类操作一律先挂 dummy。**坑：LC206 忘记保存 `next` 会丢链表；LC19 慢指针要停在待删前驱而不是待删节点本身。**
- [ ] **树与递归**：Invert Binary Tree（LC226）、Maximum Depth（LC104）、Level Order Traversal（LC102）、Construct Binary Tree from Preorder/Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235/236） — **核心：LC226 递归交换左右子树，先交换再递归或先递归再交换皆可；LC104 后序 `1 + max(depth(l), depth(r))`。LC102 BFS——队列 + 每层先记录 `size = q.size()` 再循环弹出，层与层不混。LC105 前序第一个元素是根，在 inorder 中定位根（哈希表存索引 O(1)），左子树长度 `k = idx - inLeft`，由此推出 preorder 左右边界。LC98 用上下界递归 `valid(node, lo, hi)` 而不是只比较左右孩子。LC235 利用 BST 性质：`root.val` 在 `p.val` 与 `q.val` 之间即为 LCA；LC236 一般二叉树后序递归——左右子树都找到则当前节点是 LCA。**面试口述**：树的题先明确「递归基（空节点返回什么）」；涉及 BST 优先想中序遍历有序性。**坑：LC98 只比较 node.left.val < node.val < node.right.val 会漏掉「右子树里出现比根小的值」；LC105 递归边界用「左子树长度」推导，别用绝对索引硬记。**
- [ ] **间隔 / 设计题（堆）**：Meeting Rooms II（LC253）、Design Tic-Tac-Toe（LC348）、Design Hit Counter（LC362） — **核心：LC253 排序 + 最小堆——先按开始时间排序，堆顶存「最早结束的会议」，新会议开始时间 >= 堆顶结束时间则弹出堆顶（复用会议室），否则直接入堆（新开一间），答案 = 堆的大小。LC362 滑动窗口计数——用队列存时间戳，`getHits` 时先把 `timestamp - 300` 之前的全部弹出再返回队列长度；或用环形数组按秒存。LC348 行/列/对角线计数器——`rows[i]`、`cols[j]`、正/反对角线，落子 +1（玩家1）/ -1（玩家2），绝对值达到 n 即获胜。**面试口述**：间隔题先排序再贪心是通用套路；堆的题先问「数据规模」决定用堆还是有序结构。**坑：LC253 忘记排序直接贪心会错；复用条件用 `>=`（前一场刚结束可以无缝衔接）。LC362 队列里时间戳必须单调递增，弹出过期元素要写在返回前。**

### 重点坑
- [ ] **LC98 验证 BST「上下界递归」**：必须传 `(lo, hi)` 区间约束整棵子树，只比较「父 vs 左右孩子」会漏判——典型反例：`[5,4,6,null,null,3,7]` 中右子树里的 3 小于根 5 却不小于其父 6。
- [ ] **链表「保存 next + dummy 哨兵」**：LC206 迭代反转必须先 `next = curr.next` 再改指向，否则断链；LC19 删除节点时慢指针要停在待删节点的**前驱**，并用 dummy 统一处理删除头节点的边界。
- [ ] **LC253「先排序 + 复用最早结束」**：间隔贪心第一步永远是按开始时间排序；判断能否复用会议室时比较的是**堆顶（最早结束）**，新会议开始时间 `>=` 堆顶结束时间才弹出复用，别拿当前会议和任意一间比。
- [ ] **LC105 重建二叉树「用长度推边界」**：inorder 中根的索引 `k` 决定左子树长度 `k - inLeft`，preorder 的右子树起点 = `preLeft + 1 + (k - inLeft)`；边界全靠长度推导，硬记绝对索引必错。

### 建议刷的新题
- [ ] **间隔**：Merge Intervals（Medium）— 关联已掌握 LC253 Meeting Rooms II 排序 + 扫描。**核心**：按开始时间排序后一次扫描，`cur.end >= next.start` 则合并（`end = max(end, next.end)`），否则把当前区间加入结果。**坑**：合并时右边界取两者较大值，不是后一个区间的 end；先排序是前提。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 合并两个有序链表 + LC253 堆思想。**核心**：把 k 个头节点放入最小堆，每次弹出最小节点接入结果，再将其 `next` 入堆；或分治两两合并。**坑**：堆中要处理 null；用 PriorityQueue 时节点比较器别写错（按 val 升序）。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握 LC206 反转链表 + LC141/LC19 快慢指针。**核心**：三步走——快慢指针找中点 → 反转后半段 → 交替合并两半。**坑**：找中点时偶数长度取「左中位」；反转后半段后要把前半段尾部置空，否则成环。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree。**核心**：对 s 每个节点调用 `isSameTree(s, t)`，递归 `s.left` / `s.right`；也可序列化后做子串匹配。**坑**：判子树是「s 的某个子树与 t 完全相同」，不能只比根值相等；注意空树边界。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 验证 BST（中序遍历有序）。**核心**：BST 中序遍历即升序，第 k 个访问的节点即答案；迭代版用栈 + 计数器，走到 k 就提前返回（O(H+k)）。**坑**：递归版要带返回值提前剪枝，别把整棵树遍历完；k 是 1-indexed，计数器从 1 开始。

## 历史复习记录
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
