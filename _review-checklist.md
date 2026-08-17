# 🎯 面试复习清单

## 📅 今日复习（2026-08-16）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——遍历每个格子，遇到 `'1'` 就 DFS/BFS 把它及相邻的 `'1'` 全部置 `'0'`，计数 +1。LC207 三色标记环检测——0 未访问 / 1 访问中 / 2 已完成，DFS 中再次遇到「访问中」的节点说明有环；或用 Kahn 拓扑排序（indegree 数组 + 队列）。LC133 克隆图——HashMap 存「原节点 → 新节点」，DFS/BFS 遍历时先复制再连边，避免重复克隆。**面试口述**：先确认有向还是无向、是否需要判环；图遍历模板 = visited 标记 + 邻接表。**坑：LC200 忘记沉岛会无限递归/重复计数，越界要先判断；LC207 只用 boolean visited 无法区分「当前路径」和「已完成」会误判；LC133 不先建节点就递归会死循环。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 反转——prev/curr/next 三指针，先存 next 再改 `curr.next = prev`，最后 prev 即新头。LC141 快慢指针判环——快指针每次走两步、慢指针走一步，相遇即有环。LC21 合并——dummy 哨兵 + 双指针比较，谁小接谁。LC19 删倒数第 n 个——dummy + 快指针先走 n 步，再快慢同速走，慢指针停在待删节点的前一个。**面试口述**：涉及头节点可能变化的操作（删除、反转、合并）一律先建 dummy 哨兵简化边界。**坑：反转时先存 next 再改指针，顺序反了会断链；LC19 快指针要先走 n 步（不是 n-1）；合并链表最后别忘了接上剩余部分。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree（LC105）、Validate BST（LC98）、LCA of BST（LC235） — **核心：递归三件套——base case（`root == null`）、子问题、合并结果。LC104 深度 = `1 + max(左深, 右深)`；LC100 两树同 null 为 true，一 null 一非 null 为 false，再递归比较左右；LC226 交换左右子树后递归；LC102 层序 = BFS 队列，按层 size 循环；LC105 重建——前序第一个元素是根，在中序里定位根后分左右递归；LC98 验证 BST 传上下界（min/max）递归，或用中序遍历检查递增；LC235 利用 BST 性质，若 p、q 都小于 root 走左，都大于走右，否则 root 即 LCA。**面试口述**：先想清楚递归函数的「返回值」和「子问题划分」。**坑：所有递归先写空节点判断；LC98 不能只比较左右孩子，必须传上下界；LC105 用 HashMap 存中序「值 → 下标」加速查找。**（LC235 与 LC236 的区别：LC235 是 BST 可利用大小关系定向搜索，LC236 是普通二叉树需后序遍历回溯。）**

### 重点坑
- [ ] **LC200 沉岛顺序**：先置 `'0'` 再递归四个方向，而不是先递归再标记——否则重复访问/栈溢出；四个方向都要做越界检查（row/col 出界直接 return）。
- [ ] **LC207 环检测三色标记**：0/1/2 三色（未访问/访问中/已完成），DFS 遇到「访问中」(1) 才是环；只用一个 boolean visited 无法区分「当前路径」和「已完成」，会误判；Kahn 算法记得维护 indegree 数组，最后检查入队节点数 == 节点总数，否则说明有环。
- [ ] **链表 Dummy + 快慢指针**：头节点可能被删除/修改的操作（LC19 删倒数第 n 个）务必用 dummy 哨兵；LC141 快指针每次走两步，注意 `fast.next` 空指针；LC206 反转三指针顺序：先存 next 再改 `curr.next`，否则断链。
- [ ] **树递归 base case + BST 验证**：所有递归先写 `root == null` 返回；LC98 验证 BST 必须传上下界（`min < node.val < max`）——只比较左右孩子会漏掉「右子树的左子树小于根」这类情况；LC105 前序第一个元素定位根，中序按根的位置分左右，边界下标（inLeft/inRight）容易算错。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握 LC200 Number of Islands 的 DFS/BFS 遍历。**核心**：反向思维——不从每个格子出发找海，而从四条边界「水往高处流」反向 DFS/BFS，两个 boolean 矩阵分别标记能到达太平洋/大西洋的格子，最后取交集。**坑**：比较方向是 `next >= curr`（等高也能流），别写成 `>`；边界出发的遍历不需要沉岛标记。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握 LC206 反转链表 + LC141 快慢指针。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两段。**坑**：找中点时快指针从 head 出发一次走两步；合并前先断开两段（`mid.next = null`），否则会成环。
- [ ] **链表**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握 LC21 Merge Two Sorted Lists + 堆。**核心**：最小堆存 K 个链表头，每次弹出最小节点并推入其 `next`；或分治两两合并（归并思想）。**坑**：堆里存的是 ListNode 不是值；注意 K=0、空链表边界；比较器写错会导致堆序混乱。
- [ ] **树**：Binary Tree Maximum Path Sum（LC124，Hard）— 关联已掌握树递归模板（LC104 最大深度）。**核心**：后序遍历，每个节点返回「单边最大路径和」= `node.val + max(0, max(左增益, 右增益))`；全局答案 = `node.val + max(0, 左增益) + max(0, 右增益)`。**坑**：返回值只能取单边（路径不能分叉），全局值可以经过根连接左右；负数贡献用 `max(0, ...)` 丢弃。
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握 LC98 Validate BST 的中序遍历性质。**核心**：BST 中序遍历 = 递增序列，中序遍历计数到第 k 个即答案。**坑**：k 是 1-indexed（先减后用）；递归版注意提前剪枝返回；迭代版用显式栈先一路压左。

## 历史复习记录
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
