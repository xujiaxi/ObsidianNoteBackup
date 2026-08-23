# 🎯 面试复习清单

## 📅 今日复习（2026-08-22）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——访问过的陆地标记为水避免重复访问；LC207 三色标记法（白/灰/黑）做环检测 + 拓扑排序（Kahn's BFS 与 DFS 两种实现）；LC133 用 HashMap 存「原节点 → 克隆节点」映射，BFS/DFS 逐层克隆。**面试口述：先讲清图用什么结构存（邻接表/邻接矩阵），再定遍历顺序——BFS 用队列保证层序、DFS 用递归或显式栈；环检测反问自己「节点有几种状态」。**坑：LC200 忘记把访问过的陆地标记为水会导致重复计数甚至死循环；LC207 只用 visited 布尔无法区分「访问中」和「访问完」，必须三色标记；LC133 没有映射表会无限递归或重复 new 节点；DFS 深递归注意 StackOverflowError。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针迭代（prev/curr/next）或递归，先保存 next 再改指向；LC141 快慢指针，快指针每次 2 步、慢指针 1 步，相遇即有环；LC21 用 dummy 哨兵节点 + 双指针比较；LC19 dummy 节点 + 快指针先走 N 步再同步移动。**面试口述：链表题先问「要不要 dummy 节点」——凡是可能动头节点（删除/插入头部）基本都要；再问「要不要快慢指针」——找中点、找环、找倒数第 N 个都用得上。**坑：LC206 反转顺序反了会断链（必须先存 next）；LC19 删除头节点必须靠 dummy，否则边界处理很痛苦；LC141 快慢指针步长必须不同才能相遇。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree from Preorder+Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235） — **核心：递归模板——先写 base case（空节点），再分治合并左右子树结果；LC102 层序遍历用队列，每层先取当前队列长度再出队；LC98 BST 性质 = 中序遍历有序，或递归传 (min, max) 范围；LC105 前序第一个是根，在中序定位根后递归切分左右子树；LC235 BST 的 LCA 用值比较——都小于根走左、都大于根走右。**面试口述：递归题先问「base case 是什么、返回值是什么」，再问「左右子树结果如何合并」；树的题先问「是 BST 吗、有 parent 指针吗」。**坑：LC98 只比较当前节点与直接子节点会漏掉「右子树中左子树小于根」的情况，必须传范围；LC105 中序里根的位置索引要用 preorder 起点偏移换算，左右子树长度别算错；LC102 每层必须固定 queue 大小再出队，否则把下一层混进来。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC153/33 与右边界 `nums[right]` 比较通常比左边界更可靠，区分「找目标值」与「找边界」两套模板；LC53 Kadane 算法 `cur = max(n, cur+n)`；LC1 HashMap 存「值 → 下标」一遍扫；LC121 维护 minPrice。**面试口述：二分先判断单调性/旋转点在哪一侧，再选模板。**坑：LC33 判断目标在左半还是右半时边界条件易错；LC153 用左边界比较在数组长度为 2 时会出错。**

### 重点坑
- [ ] **图论 BFS/DFS**：LC200 沉岛后必须标记访问过（改成 '0'），否则重复计数；LC207 环检测用三色标记（灰 = 访问中），只有 visited 布尔会误判；LC133 必须维护「原节点 → 克隆节点」映射，防止重复创建和无限递归；DFS 深递归可能 StackOverflowError。
- [ ] **链表**：LC206 反转先存 next 再改指针，否则断链；LC19 用 dummy 节点处理删除头节点，快指针先走 N 步再同步移动；LC141 快慢指针步长不同（2 vs 1）才能相遇判环。
- [ ] **树与递归**：LC98 验证 BST 必须传 (min, max) 区间而非只比直接子节点；LC105 重建树小心 inorder 索引偏移、子树长度计算易错；LC102 层序遍历每层先记 queue 大小再出队。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握知识点：LC200 岛屿 DFS/BFS（已完成）。**核心**：从四条边界反向遍历，两个 ocean 的可达集合取交集——比「正向找能同时到达两洋的点」简单得多。**坑**：反向遍历时比较条件是相邻格子 `>=` 当前高度；两条边界的 visited 要分开记。
- [ ] **链表 / 堆**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握知识点：LC21 合并两个有序链表 + LC253 最小堆（已完成）。**核心**：最小堆维护 k 个头节点，每次 pop 最小并 push 其 next；或分治两两合并。**坑**：Python 堆里存 `(值, 节点)` 避免直接比较节点报错；注意空链表输入。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握知识点：LC100 Same Tree（已完成）。**核心**：遍历主树每个节点，用 isSameTree 判断是否与子树相同。**坑**：空树是任何树的子树；必须用 isSameTree 整体比较而不是只比节点值。
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握知识点：LC98 Validate BST（已完成）。**核心**：BST 中序遍历即升序，第 k 个访问的节点就是答案；也可用左子树大小分治。**坑**：k 是 1-indexed，计数器先减再判断；递归可提前剪枝退出。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握知识点：LC206 反转链表 + LC141 快慢指针（已完成）。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两半。**坑**：找中点时奇偶长度边界；合并时先存 next 再改指针，否则断链。

## 历史复习记录
- 2026-08-22：图论 BFS/DFS、链表、树与递归
- 2026-08-21：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-20：图论 BFS/DFS、链表、树与递归
- 2026-08-19：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-18：图论 BFS/DFS、链表、树与递归
- 2026-08-17：滑动窗口 & 字符串、动态规划（股票系列）、数组 & 二分查找
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
