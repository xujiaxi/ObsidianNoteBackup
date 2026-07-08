# 🎯 面试复习清单

## 📅 今日复习（2026-07-07）

### 需要回顾
- [ ] **滑动窗口**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：外层 while 扩展右指针，内层 while 在条件满足时收缩左指针。窗口用 `window[c]` 计数，当 `window[c] == need[c]` 时 `valid++`；收缩后 `window[c]` 减少，若 `window[c] < need[c]` 必须 `valid--`。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19）— **核心：反转用三指针 prev/curr/next；环检测快慢指针；合并用 dummy 哨兵节点遍历；删除倒数第 N 个用快慢指针先让 fast 走 N 步。dummy 哨兵简化头节点删除。**
- [ ] **树 DFS/BFS 遍历**：Max Depth（LC104）、Invert（LC226）、Level Order（LC102）、Validate BST（LC98）、LCA of BST（LC235）— **核心：DFS 递归与栈、BFS 层序队列。BST 中序遍历有序；LCA 利用 BST 大小比较；Invert 交换左右子树递归。**

### 重点坑
- [ ] **滑动窗口收缩后忘记同步更新**：收缩左指针后 `window[c]` 减少，若 `window[c] < need[c]` 必须 `valid--`。漏掉 `valid--` 会导致 valid 虚高，窗口实际不满足条件但被判为满足。
- [ ] **链表反转指针顺序**：`next = curr.next; curr.next = prev; prev = curr; curr = next` — 顺序不能乱，尤其要先保存 `curr.next` 再修改 `curr.next` 指向，否则丢失后续节点。
- [ ] **二分查找边界条件**：`while(left <= right)` vs `while(left < right)`？返回 `left` 还是 `right`？旋转数组中点偏移一格导致死循环，务必手写模板并测试。
- [ ] **图的克隆中遗漏邻居**：Clone Graph 遍历邻居时既要创建邻居节点也要建立双向连接，别忘了双向处理。
- [ ] **Java Integer 比较**：务必用 `.equals()`，而非 `==`，因为超过 Integer Cache (-128~127) 会缓存未命中导致错误。

### 建议刷的新题
- [ ] **数组 / 前缀积**：Product of Array Except Self（Medium）— 关联已掌握知识：数组遍历。左遍历求前缀乘积，右遍历乘入后缀乘积，O(N)时间 O(1)额外空间（输出数组不计入）。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握知识：链表反转（LC206）+ 快慢指针（LC141）。三步走：快慢指针找中点 → 反转后半段 → 交叉合并前后半段。
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板（LC3, LC76）。窗口内维护 maxFreq，当 `窗口长度 - maxFreq > k` 时收缩 left 指针。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握知识：BST 性质（LC98）+ 中序遍历。BST 中序遍历即升序序列，第 k 个即为答案，可用递归或迭代栈实现。
- [ ] **堆**：Top K Frequent Elements（Medium）— 关联已掌握知识：哈希表 + 堆操作。HashMap 统计频率后，用最小堆（size=k）维护 Top K，堆满时弹出最小频率元素，O(N log K)。

## 历史复习记录
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
| Array | 1 | `array/` |
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

**Blind 75 完成：21 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **数组基础** — LC1 + LC121
