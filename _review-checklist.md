# 🎯 面试复习清单

## 📅 今日复习（2026-08-20）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：沉岛算法——LC200 访问过的陆地直接标记为水（`grid[r][c]='0'`），省 visited 数组；LC133 用 HashMap 存 old→new 映射，DFS/BFS 边遍历边建节点，避免重复克隆死循环；LC207 环检测用三色标记法（0 未访问 / 1 访问中 / 2 已完成，遇到「访问中」即闭环）或 Kahn 拓扑排序（入度数组 + 队列）。**面试口述**：先判断题型——连通分量（DFS 沉岛）还是依赖关系（拓扑排序）；克隆图先讲 HashMap 映射防止死循环。**坑：LC200 忘记标记已访问会死循环/重复计数；全陆地时 DFS 递归深度 = 格子数 → StackOverflow，大数据换 BFS 或迭代 DFS；LC207 只有入度减到 0 才入队，最后要检查出队节点数 == 总节点数（否则有环）。**
- [ ] **链表**：Reverse a Linked List（LC206）、Detect Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：三指针反转（先存 `next_temp` 再改 `curr.next`）；快慢指针检测环（`while fast and fast.next`）；合并/删除用 Dummy 节点简化头节点边界。**面试口述**：反转先讲迭代 O(1) 空间再讲递归版；链表题先想「dummy 节点能否简化边界」再动手。**坑：反转时先保存 next 再断链，顺序反了丢失后续链表；快慢指针循环条件顺序 `fast and fast.next` 不能反；LC19 用 dummy 避免删除头节点的特判。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert（LC226）、Level Order（LC102）、Construct from Preorder/Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235/236） — **核心：递归模板——空节点 base case + 左右子树结果组合；层序用队列 BFS；LC105 前序定根 + 中序切分左右子树（HashMap 缓存中序索引 O(1) 查找）；LC98 验证 BST 必须传上下界区间 (min, max)；LC235 利用 BST 有序性质（都小于根走左、都大于根走右）。**面试口述**：树题先问「当前节点的答案能否由左右子树答案组合出来」；BST 题先想能否利用有序性质。**坑：LC98 只比较直接子节点会漏判（必须传上下界）；中序遍历验证用 `prev >= node.val`（严格递增，重复值非法）；LC105 区间边界（inLeft/inRight）易写错，写完用样例自测；Python 类变量陷阱——`self.prev` 必须在方法内初始化。**

### 重点坑
- [ ] **图论**：LC200 沉岛必须标记已访问，忘记会死循环/重复计数；全陆地时 DFS 栈深 = 格子数 → StackOverflow，改 BFS 或迭代 DFS；LC207 Kahn 拓扑排序只有入度减到 0 才入队，且出队节点数 < 总节点数说明有环。
- [ ] **链表**：反转链表必须先存 `next_temp` 再改 `curr.next`，顺序反了丢失后续链表；快慢指针循环条件 `while fast and fast.next`（fast.next 判断在前会空指针）；LC19 删除头节点用 dummy 节点避免特判。
- [ ] **树**：LC98 必须传上下界区间递归，只比较直接子节点会漏掉「右子树中的小值」；中序遍历验证用 `prev >= node.val` 而非 `>`；LC105 中序索引用 HashMap 缓存、区间边界写完自测。

### 建议刷的新题
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握知识点：LC98 中序遍历（今日树专题）。**核心**：BST 中序遍历第 k 个节点即答案；可提前剪枝（k 减到 0 即停）。**坑**：中序必须严格递增遍历；迭代栈版本注意入栈顺序。
- [ ] **树**：Serialize and Deserialize Binary Tree（LC297，Hard）— 关联已掌握知识点：LC102 层序遍历 + LC105 构造树。**核心**：BFS 层序序列化，null 占位保持结构；反序列化用队列逐层重建。**坑**：序列化分隔符与 null 标记统一；反序列化时队列里存的是节点而非值。
- [ ] **图**：Longest Consecutive Sequence（LC128，Medium）— 关联已掌握知识点：LC200 图连通思想 + LC1 HashMap。**核心**：HashSet 存所有数，只从「没有前驱的数」开始向后扩展，整体 O(n)。**坑**：判断前驱用 `set.contains(num-1)`，避免每个数都重复扩展。
- [ ] **图 / 回溯**：Word Search（LC79，Medium）— 关联已掌握知识点：LC200 沉岛 DFS 模板（今日图论专题）。**核心**：DFS 四方向 + visited 标记，回溯时恢复状态；先判边界再访问。**坑**：回溯后必须恢复 visited，否则影响其他分支；字符匹配失败要提前剪枝。
- [ ] **数组 / 双指针**：Container With Most Water（LC11，Medium）— 关联已掌握知识点：Two Sum（LC1）双指针。**核心**：左右指针向中间收缩，每次移动较矮的一侧，维护最大面积。**坑**：面积由较矮边决定，移动较高边不可能增大面积。

## 历史复习记录
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
