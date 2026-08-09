# 🎯 面试复习清单

## 📅 今日复习（2026-08-08）

### 需要回顾
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 迭代三指针 `prev → cur → next`，先存 `tmp = cur.next` 再改 `cur.next = prev`，三指针同步平移，返回 prev（新头）；递归版 `head.next.next = head; head.next = None`，注意返回新头。LC141 快慢指针——快指针每次走两步、慢指针一步，`while fast and fast.next` 判空，相遇即有环；进阶 Floyd 找环入口：相遇后 slow 回 head，两指针各走一步再相遇处即入口。LC21 合并两个有序链表——dummy 哨兵 + 双指针，`while l1 and l2` 比较取小，循环结束后把剩余链表直接接上（省逐节点搬运）。LC19 删除倒数第 N 个——快指针先走 N 步，快慢同步走，快指针到尾时慢指针恰在待删节点前驱；dummy 处理删除头节点。**面试口述**：链表题先问「能否修改原链表 / 是否需要 dummy 哨兵」；反转、环检测、找中点、找倒数第 N 个都是快慢指针家族的变体。**坑：LC206 必须先存 next 再改指针，顺序错直接断链；LC141 判空要 `fast and fast.next` 同时检查；LC19 必须用 dummy，否则删头节点时无前驱。**
- [ ] **树与递归**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102）、Construct Binary Tree（LC105）、Validate BST（LC98）、LCA（LC235/236） — **核心：LC104 递归 `1 + max(depth(l), depth(r))`；LC100 `p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)`，递归终止先判空（都空 True、一空一不空 False）；LC226 先交换左右孩子再递归翻转；LC102 层序 BFS——deque 队列，每层先记录 `size = len(q)` 再出队本层节点；LC105 前序第一个元素是根，inorder 用哈希表存「值→索引」O(1) 定位分割左右子树；LC98 递归传 `(low, high)` 边界，`low < val < high`；LC235 BST 版按值大小走向（`p < root < q` 则 root 即 LCA），LC236 二叉树版后序递归——左右子树都非空则当前节点是 LCA。**面试口述**：树题先判断「递归（天然适合树形）vs 迭代 BFS（层序/最短路径）」；凡是「判断整棵树是否满足 X」都要想清楚是传边界（min/max 范围）还是依赖子树返回值。**坑：LC98 只比较父子节点会漏掉右子树中的小值/左子树中的大值，必须传边界；LC105 递归时 preorder 指针要全局递增（或按长度切片），不能每层从头找。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating（LC3）、Minimum Window Substring（LC76）、Longest Common Prefix（LC14） — **核心：LC3 滑动窗口 + 哈希表记录字符最近位置，遇重复 `left = max(left, last_index[c] + 1)`，每次更新 `ans = max(ans, right - left + 1)`；LC76 `need` 字典记录 t 中字符需求，`formed` 计数「已满足需求的字符种类数」，`formed == len(need)` 时收缩左指针并更新最小窗口；LC14 横向比较（逐个字符串取公共前缀）或纵向按列扫描。**面试口述**：子串/子数组问题先想滑动窗口——「何时扩右边界、何时缩左边界、窗口满足什么条件」；区分固定窗口 vs 可变窗口两种模板。**坑：LC3 重复字符时 left 必须用 `max` 防止窗口回退；LC76 收缩左指针前先更新答案，字符计数从 need 跌破 need-1 时 `formed` 要 -1（判断用 `==` 触发而非 `>=`，否则重复减）。**

### 重点坑
- [ ] **LC206 反转链表「先存 next 再改指针」**：迭代三指针顺序必须为 `tmp = cur.next → cur.next = prev → prev = cur → cur = tmp`，少一步或顺序错就直接断链；递归版记住返回的是新头（原尾节点），`head.next` 要置 None 防环。
- [ ] **快慢指针「判空与 dummy」**：LC141 循环条件必须 `while fast and fast.next` 两个都查，否则 `fast.next.next` 抛 AttributeError；LC19 删除头节点时没有前驱，必须用 dummy 哨兵，快指针先走 N 步的写法天然依赖 dummy。
- [ ] **LC98 Validate BST「必须传 (low, high) 边界」**：只比较 `left.val < root.val < right.val` 会漏掉「右子树中存在小于根的值」这类错误；正确做法是递归传递区间并收窄，或中序遍历验证严格递增。
- [ ] **LC3 滑动窗口「left 跳转用 max 不用直接赋值」**：`left = max(left, last_index[c] + 1)`；直接 `left = last_index[c] + 1` 时若该字符上次出现位置在 left 之前，会把窗口左边界往回拉，导致 ans 虚大。
- [ ] **LC76 最小覆盖子串「formed 计数与更新顺序」**：每个字符计数达到 need 才 `formed += 1`（用 `==` 判断）；收缩左指针前先记录窗口长度，移动 left 后计数跌破 need 时 `formed -= 1`；顺序反了会漏掉最优解或重复减计数。

### 建议刷的新题
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 两两合并 + LC253 最小堆。**核心**：把 K 个头节点放进最小堆，每次 pop 最小接到 dummy 后，再 push 它的 next，O(n log k)。**坑**：堆里存 `(val, node)` 元组防止比较 node 时报错；不要用两两合并 O(nk) 除非面试官要求。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握 LC141 快慢指针找中点 + LC206 反转链表。**核心**：快慢指针找中点 → 反转后半段 → 交叉合并两段。**坑**：找中点时快指针判空（奇偶长度）；交叉合并时先存 next 再改指针，否则断链。
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree。**核心**：对每个节点调用 `isSameTree(root, subRoot)`，不等则递归 `isSubtree(root.left)` / `isSubtree(root.right)`；先判断当前节点是否相等。**坑**：subRoot 为空返回 True；区分「相等」与「包含」两种递归。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 中序遍历。**核心**：BST 中序遍历即升序，计数器数到第 k 个返回；迭代版用栈模拟中序。**坑**：递归版计数器要跨递归共享（Python 用 list 包裹或改迭代）；不要排序整个数组 O(n log n)。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3/LC76 滑动窗口模板。**核心**：维护窗口内出现次数最多的字符 `max_count`，`window_len - max_count <= k` 窗口合法，否则收缩左指针；答案 = 合法窗口最大长度。**坑**：`max_count` 只增不减（历史最大值）是常见优化，收缩后不精确也无妨；`right - left + 1 - max_count > k` 时才 left++。

## 历史复习记录
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
