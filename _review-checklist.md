# 🎯 面试复习清单

## 📅 今日复习（2026-07-12）

### 需要回顾
- [ ] **滑动窗口**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：通用模板 — 外层 while 扩展右指针 `right++`，内层 while 满足条件时收缩左指针 `left++`；窗口内用 HashMap/数组维护字符计数；LC76 需要有效计数 `formed` 跟踪当前窗口是否覆盖所有目标字符。收缩窗口时先更新结果再移动左指针。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19）— **核心：反转链表用 `prev→curr→next` 三指针模板，保存 next 再改指向；快慢指针检测环，`slow = head, fast = head`，fast 每次两步 slow 一步，相遇即有环；哨兵节点（Dummy Node）简化头结点删除/合并边界；删除倒数第 N 个用快指针先走 N 步。**

### 重点坑
- [ ] **滑动窗口 valid-- 漏更新**：收缩窗口移动左指针时，必须同步更新窗口内计数（`windowCount[s[left]]--`）和有效计数（`formed--` 或 `count--`），漏掉任一个会导致后续窗口判断错误。尤其注意 char 类型转换后减少计数到 0 以下。
- [ ] **链表反转指针顺序错误**：`next = curr.next; curr.next = prev; prev = curr; curr = next` — 先保存 `next` 再改指向，顺序不可弄反。养成写完后手推一次的习惯（1→2→3→null）。
- [ ] **链表快慢指针环检测初始化**：两者都从 `head` 开始，但循环条件必须是 `while fast and fast.next`（检查 fast 和 fast.next 非空），不是 `while fast.next`。如果 `head` 为 null 或只有一个节点，`fast.next` 会抛 NPE。
- [ ] **滑动窗口的最小覆盖子串 left 收缩时机**：LC76 中，当窗口满足覆盖条件（`formed == required`）后才开始收缩左指针。收缩过程中可能再次变为不满足，此时退出内层 while。注意收缩后结果更新应在收缩开始前记录（先记录再收缩），以免丢失最优解。

### 建议刷的新题
- [ ] **链表**：Reorder List（Medium）— 关联已掌握知识：链表反转（LC206）+ 快慢指针找中点（LC141）+ 合并链表（LC21）。三步法：快慢指针找到中点→反转后半段→交替合并前后段。O(N) 时间 O(1) 空间，注意奇偶长度的中点选择。
- [ ] **数组 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板（LC3, LC76）。维护窗口内最高频字符出现次数 `maxFreq`，当 `windowLen - maxFreq > k` 时收缩左指针。面试高频，需理解为什么不需要每次更新 maxFreq。
- [ ] **数组 / 双指针**：3Sum（Medium）— 关联已掌握知识：Two Sum（LC1）哈希表思想 + 排序双指针。先排序，固定一个数后用双指针找剩余两数之和，注意去重（跳过重复元素），O(N²) 时间 O(1) 额外空间。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握知识：合并两个有序链表（LC21）。可用分治法（两两合并 O(N log K)）或小顶堆（PriorityQueue O(N log K)）。面试中分治实现更简洁且不依赖堆，两种方案都要能讲。

## 历史复习记录
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

- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
