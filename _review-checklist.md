# 🎯 面试复习清单

## 📅 今日复习（2026-08-28）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——遍历到陆地就 DFS/BFS 将其及相邻陆地全部置 '0'，触发次数即岛屿数；LC207 环检测——三色标记法（0 未访问 / 1 访问中 / 2 已完成）DFS，或 Kahn 拓扑排序 BFS 统计入度为 0 的节点，若入队数 < 课程总数则有环；LC133 克隆图——HashMap 记录「原节点 → 克隆节点」，已克隆则直接返回，避免重复创建与死循环。**面试口述：先确认是连通图还是森林、是否需要 visited，再选 BFS（层级/最短）还是 DFS（递归简洁）。**坑：LC200 忘记沉岛会重复计数；LC207 只记 visited 布尔会漏判环，必须区分「访问中」状态；LC133 漏掉 visited map 会无限递归。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针 prev/curr/next 原地反转（先存 next 再改指向），递归写法 `head.next.next = head` + 置空防环；LC141 快慢指针——slow 一步、fast 两步，相遇即有环；LC21 dummy 哨兵 + 双指针比较，谁小接谁，最后接剩余链表；LC19 dummy + 快慢指针，fast 先走 n+1 步再同步前进，slow 恰好停在待删节点的前一个。**面试口述：先问能否修改原链表、是否允许额外空间，再决定要不要 dummy 简化头节点边界。**坑：LC206 改指针前必须先存 next，否则断链；LC141 fast 每次走两步前判 `fast.next != null` 防空指针；LC19 fast 先走 n 还是 n+1 步搞混会删错节点。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree（LC105）、Validate BST（LC98）、LCA of BST（LC235） — **核心：递归三件套——base case（null 返回）、分解子问题、合并结果；LC104 `1 + max(depth(left), depth(right))`；LC100 两树同时 null 或值相等且左右子树都相等；LC226 先交换左右子树再递归；LC102 BFS 队列逐层处理，每层开始前先快照 `queue.size()`；LC105 前序第一个元素定根，HashMap 存中序索引快速切分左右子树；LC98 递归传 `(min, max)` 上下界约束，或中序遍历必须严格递增；LC235 利用 BST 性质——p、q 都小于 root 走左子树、都大于走右子树，否则 root 即为 LCA。**面试口述：先写 base case，再声明递归假设（子树已正确返回），最后讲如何合并。**坑：LC102 不先快照 size 会错层；LC98 只比较父节点不传上下界会漏判（右子树中出现小于根的值）；LC105 递归内线性找根索引会退化成 O(n²)，必须用 HashMap 预处理。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 HashMap 存「值 → 下标」，一次遍历查 `target - nums[i]`；LC53 Kadane——`cur = max(nums[i], cur + nums[i])`，`ans = max(ans, cur)`；LC153/LC33 旋转数组二分——与右边界 `nums[right]` 比较判断中点落在哪半段，找最小值用 `nums[mid] > nums[right]` 收缩左半，搜索目标值先判有序半段再决定走向。**面试口述：二分先确认单调性/有序性假设，再选左闭右闭还是左闭右开模板。**坑：LC1 先查 map 再放入当前元素，避免重复使用自身；LC53 cur 为负时重置而非累加；LC33 判断 `nums[mid] >= nums[left]` 的等号边界容易漏。**（注：本组为补充回顾，其余已完成专题按轮换复习）**

### 重点坑
- [ ] **图论**：LC133 Clone Graph 必须用 visited map 防重复克隆与死循环；LC207 环检测用三色标记（0/1/2），仅 visited 布尔会漏判「祖先回边」；LC200 沉岛后务必把当前格子置 '0'，否则重复计数。
- [ ] **链表**：LC206 先存 `next` 再改 `curr.next`，顺序反了直接断链；LC141 快指针每次走两步前判 `fast.next != null`；LC19 用 dummy 哨兵统一头节点删除场景，fast 先走 n+1 步再同步移动。
- [ ] **树**：LC102 每层开始前快照 `queue.size()`，循环内 size 变化会错层；LC98 验证 BST 必须传上下界（或中序遍历严格递增），只和父节点比较会漏判右子树中的较小值；LC105 用 HashMap 预处理 inorder 索引，避免递归内线性查找导致 O(n²)。
- [ ] **通用**：深度递归（DFS）可能 StackOverflowError，理解 Stack vs Heap 内存模型；Java 中比较 Integer 对象用 `.equals()` 而非 `==`（超出 -128~127 缓存时失效）。

### 建议刷的新题
- [ ] **图论**：Pacific Atlantic Water Flow（LC417，Medium）— 关联已掌握知识点：LC200 岛屿 DFS/BFS 遍历（已完成）。**核心**：反向思维——从四条海岸线向陆地 BFS/DFS，分别维护能流入太平洋/大西洋的两个 visited 集合，取交集。**坑**：正向模拟每个格子会超时，必须反向从边界出发；水流条件是 `next >= curr` 才能流动。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握知识点：LC206 反转链表 + LC141 快慢指针（已完成）。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两段。**坑**：找中点时奇偶长度的边界；合并时先保存 next 再改指向，防止断链。
- [ ] **链表**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握知识点：LC21 合并两个有序链表（已完成）。**核心**：优先队列（最小堆）每次弹出最小头节点接上，或分治两两合并；复杂度 O(N log k)。**坑**：比较器写反会变最大堆；处理空链表数组边界；堆中存节点而非值，注意节点排序依据。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握知识点：LC100 Same Tree 递归（已完成）。**核心**：双重递归——外层遍历 root 每个节点找候选，内层 isSameTree 精确比较。**坑**：空树边界（subRoot 为空返回 true）；区分「子树」与「子结构」，子树要求结构完全一致到叶子。
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握知识点：LC98 验证 BST 中序遍历（已完成）。**核心**：BST 中序遍历严格递增，第 k 个访问的节点即答案；用迭代栈可提前终止。**坑**：k 递减时机（访问节点时而非入栈时）；递归写法注意全局计数与提前返回。

## 历史复习记录
- 2026-08-28：图论 BFS/DFS、链表、树与递归、数组 & 二分查找
- 2026-08-27：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-26：图论 BFS/DFS、链表、树与递归
- 2026-08-25：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-24：图论 BFS/DFS、链表、树与递归
- 2026-08-23：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
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
