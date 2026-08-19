# 🎯 面试复习清单

## 📅 今日复习（2026-08-18）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——访问过的陆地直接标记为水，BFS/DFS 皆可；LC207 拓扑排序（Kahn：入度为 0 的节点入队，入队节点数 != 总节点数即存在环）或三色标记 DFS；LC133 用 HashMap 存「原节点 → 克隆节点」映射，先建节点再处理邻居，避免重复创建。**面试口述**：先分清有向图/无向图、是否需要环检测，再选 BFS/DFS 还是拓扑排序。**坑：LC200 忘记沉岛会重复计数；LC207 用「访问数 == 节点数」判断无环；LC133 处理邻居时必须查 map，已存在就直接复用。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针 prev/curr/next 依次反转；LC141 快慢指针，快指针每次走两步；LC21 dummy 节点 + 双指针按值合并；LC19 快指针先走 n 步，慢指针再同步走，删除慢指针的下一个节点。**面试口述**：链表题先想「要不要 dummy 节点」，再想「反转 / 快慢指针 / 合并」哪种套路。**坑：LC206 先保存 next 再反转，否则断链；LC19 必须用 dummy 处理删除头节点；LC141 循环条件 `fast != null && fast.next != null`。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree from Preorder+Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235）、LCA of Binary Tree（LC236） — **核心：递归模板——先写 base case（null 处理），再递归左右子树；LC102 BFS 按层收集，每层先记录当前队列大小；LC105 前序第一个是根，中序用 HashMap 定位根来切分左右区间；LC98 递归传 (low, high) 上下界约束；LC235 按值二分，LC236 需递归找 p/q 分居两侧的情况。**面试口述**：树题先确认遍历方式（前/中/后序、BFS），想清楚「返回值是什么、要传给父节点什么」。**坑：LC98 只比较左右子节点会漏判（必须传上下界）；LC105 中序索引用 HashMap 缓存避免 O(n) 查找；LC236 注意 p/q 一个在子树、一个在根的情况。**（LC235 与 LC236 的区别：BST 按值判断走向，普通二叉树必须递归搜索。）**

### 重点坑
- [ ] **沉岛 & 环检测**：LC200 访问过的陆地必须标记为水（沉岛），否则死循环/重复计数；LC207 用三色标记（0 未访问 / 1 访问中 / 2 已访问）或 Kahn 拓扑排序检测环——DFS 遇到「访问中」节点即存在环，Kahn 判断「入队节点数 != 节点总数」。
- [ ] **链表指针操作**：反转链表先保存 next 再改指向（LC206）；删除节点用 dummy 头节点统一处理边界（LC19）；快慢指针循环条件 `fast != null && fast.next != null`（LC141），写错会 NPE 或漏判；合并链表后记得把尾部置 null。
- [ ] **树递归边界**：BST 校验必须传上下界 (low, high)，仅比较左右子节点会漏判（LC98）；递归先写 null base case；LC105 前序+中序构造树时中序索引用 HashMap 缓存，区间 [inLeft, inRight] 边界易写错——写完用单节点 / 斜树 / 空树三组用例自测。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握 LC200 Number of Islands 的 DFS/BFS。**核心**：反向思维——从四条边界向内 BFS/DFS，分别标记能流到太平洋/大西洋的格子，最后取交集。**坑**：别从每个格子出发做 DFS（会超时），从边界反向遍历；两个海洋用独立的 visited 标记。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握 LC206 反转链表 + 快慢指针。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两段。**坑**：找中点时奇偶长度的边界；合并时先保存 next 再改指针，防止断链；记得把前半段尾部置 null。
- [ ] **链表**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握 LC21 合并两个有序链表 + 最小堆。**核心**：优先队列（最小堆）每次弹出最小节点接上，或分治法两两合并。**坑**：堆比较器按 val 排序；处理空链表列表；K=1 的边界。
- [ ] **树**：Binary Tree Maximum Path Sum（LC124，Hard）— 关联已掌握树递归模板（LC104/LC226）。**核心**：后序遍历，每节点返回「单边最大路径和」（负数取 0），全局变量维护最大路径和。**坑**：路径可以拐弯经过根节点，答案不一定是根节点的返回值；负值分支直接丢弃。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握 LC100 Same Tree。**核心**：遍历主树每个节点，调用 Same Tree 判断是否匹配。**坑**：空树边界；Same Tree 中两个节点同时为 null 才算相等。

## 历史复习记录
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
