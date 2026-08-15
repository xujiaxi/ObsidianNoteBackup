# 🎯 面试复习清单

## 📅 今日复习（2026-08-14）

### 需要回顾
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 迭代反转——`prev/curr/next` 三指针，先存 `next` 再改 `curr.next`，最后返回 `prev`（新头）。LC141 快慢指针——`slow` 每次 1 步、`fast` 每次 2 步，相遇即有环，循环条件 `fast != null && fast.next != null`。LC21 dummy 哨兵节点 + 双指针比较，谁小接谁，最后接上剩余部分。LC19 快指针先走 `n+1` 步，让 `slow` 停在待删节点**前一个**，dummy 节点统一处理删头节点。**面试口述**：先确认「能否用 dummy」「需要几个指针」，画图演示指针移动。**坑：LC206 先改指针再存 next 会断链；LC141 忘记判 `fast.next != null` 会 NPE；LC19 快指针只走 n 步时 slow 会停在待删节点本身，需 `slow.next = slow.next.next` 删除。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree from Preorder & Inorder（LC105）、Validate BST（LC98）、LCA of BST（LC235）/ LCA of Binary Tree（LC236） — **核心：递归模板——先写 base case 返回，再想左右子树递归结果如何合并。LC104 `1 + max(left, right)`。LC100 两树同步递归，值相等且左右都 Same。LC226 先交换左右子节点再递归。LC102 BFS 队列，每层先记录 `queue.size()` 再循环弹出。LC105 前序首元素定根，中序定位根 index，`leftLen = index - inStart`，按长度偏移递归。LC98 中序遍历递增，或递归传 `(min, max)` 边界。LC235 利用 BST 性质——`p.val < root.val < q.val` 则 root 即 LCA；LC236 二叉树 LCA 用后序递归，左右子树都有结果时当前节点即 LCA。**面试口述**：先想「递归返回值是什么」「base case 怎么写」。**坑：LC98 只比较左右子节点会漏掉祖先约束；LC105 递归传参用长度偏移别硬编码下标；LC102 循环内不重新取 size 会串层；LC226 交换后要递归处理子树。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76） — **核心：通用模板——外层 `while` 扩展右指针，内层 `while` 满足条件时收缩左指针。LC3 用 HashMap/Set 记录窗口内字符，出现重复时左指针收缩到重复字符后一位，答案取 `max(窗口长度)`。LC76 双 Map（need/window）+ `valid` 计数，`valid == need.size()` 时尝试收缩，**收缩前**先更新最小窗口答案。**面试口述**：先明确「窗口满足什么条件」「收缩时更新什么」。**坑：LC3 收缩条件写错会多收缩；LC76 忘记在收缩前记录答案、移出窗口字符时 `window` 计数和 `valid` 忘记同步更新。**

### 重点坑
- [ ] **LC206 反转链表指针顺序**：必须先 `next = curr.next` 保存后继，再 `curr.next = prev`，最后 `prev = curr; curr = next`——顺序错直接断链丢节点；最终返回 `prev` 不是 `curr`。
- [ ] **LC98 BST 验证的祖先约束**：只检查 `left < root < right` 会漏掉「右子树里出现比祖先小的节点」，必须递归传 `(min, max)` 边界或改中序遍历递增判断；LC235 是 BST 专用（值比较即可），LC236 通用二叉树要后序递归。
- [ ] **LC3/LC76 滑动窗口收缩时机**：LC3 只在出现重复时收缩，收缩到窗口内无重复为止；LC76 用 `valid == need.size()` 判断完全覆盖，更新答案要在收缩之前，移出字符时 `window` 计数和 `valid` 都要同步更新。
- [ ] **LC105 重建二叉树索引计算**：中序里定位根 index，`leftLen = index - inStart`，右子树起点是 `inStart + leftLen + 1`——用长度偏移而不是拍脑袋写死下标；前序指针每层 +1。
- [ ] **LC141 / LC19 快慢指针边界**：LC141 循环条件 `fast != null && fast.next != null` 缺一不可，否则 NPE；LC19 用 dummy 节点、快指针先走 `n+1` 步，保证 slow 停在待删节点前一个，删头节点也能统一处理。

### 建议刷的新题
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握 LC206 反转链表 + 快慢指针。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两半。**坑**：找中点注意奇偶长度；合并前先存 next 防止断链。
- [ ] **链表 / 堆**：Merge K Sorted Lists（LC23，Hard）— 关联已掌握 LC21 合并两个有序链表 + LC253 最小堆。**核心**：k 个头节点入最小堆，每次弹出最小节点接到结果链表，再将其 `next` 入堆。**坑**：比较器按节点值；堆空即结束；别重复入堆已弹出的节点。
- [ ] **树**：Subtree of Another Tree（LC572，Easy）— 关联已掌握 LC100 Same Tree。**核心**：对每个节点调用 `isSameTree(root, subRoot)`，或递归检查左右子树。**坑**：空树 / 空子树边界；要遍历所有节点而不是只比根。
- [ ] **树**：Kth Smallest Element in a BST（LC230，Medium）— 关联已掌握 LC98 BST 中序遍历。**核心**：中序遍历天然递增，计数到 k 返回；迭代栈实现可提前剪枝。**坑**：k 从 1 计数；递归用全局 / 引用计数，返回值传递易错。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（LC424，Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：维护窗口内最高频字符数 maxCount，`窗口长度 - maxCount <= k` 则窗口合法可扩展，否则左指针右移；经典 trick 是窗口长度只增不减。**坑**：收缩时记得同步更新字符频率和 maxCount。

## 历史复习记录
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
