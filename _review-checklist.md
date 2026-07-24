# 🎯 面试复习清单

## 📅 今日复习（2026-07-23）

### 需要回顾
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）、Search in Rotated Sorted Array（LC33）、Find Minimum in Rotated Sorted Array（LC153）— **核心：LC1 暴力 O(n²) → HashMap 一遍扫描 O(n)，`map.get(target - nums[i])` 命中即返回；坑——put 操作必须在 lookup 之后执行，避免同元素自引用（target = 2x 时误把本元素当另一半）。LC121 一次遍历维护 `minPrice` 和 `maxProfit = Math.max(maxProfit, price - minPrice)`，贪心思想。LC33/153 旋转排序数组——与右边界 `nums[right]` 比较比左边界更可靠；LC153 求最小值用 `nums[mid] vs nums[right]` 判断左/右半有序，收缩 `right = mid`（非 `mid - 1`，因为 mid 可能是答案）；LC33 求目标值先判断哪半有序再二分。**
- [ ] **链表**：Reverse a Linked List（LC206）、Detect Cycle in a Linked List（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End Of List（LC19）— **核心：LC206 三指针迭代法 `prev=null, cur=head`，循环 `nxt = cur.next; cur.next = prev; prev = cur; cur = nxt`，递归法 `reverseList(head.next)` 后 `head.next.next = head; head.next = null`。LC141 快慢指针 Floyd 判圈——`slow` 走一步 `fast` 走两步，相遇则有环，`fast` 到 null 则无环。LC21 dummy 哨兵节点 + 双指针比较合并，`dummy.next` 返回头。LC19 双指针——`fast` 先走 n 步，再 `slow` 和 `fast` 同步走直到 `fast.next == null`，`slow.next` 即待删节点；dummy 哨兵解决删头节点边界。**

### 重点坑
- [ ] **LC1 Two Sum 的 HashMap 写入顺序**：必须先 `get` 再 `put`。若先 `put` 再 `get`，当 `target = nums[i] * 2`（如 target=6, nums[i]=3）时会把自己当成另一半匹配成功，返回错误结果。正确顺序：先查 `map.containsKey(target - nums[i])`，命中返回；未命中才 `map.put(nums[i], i)`。
- [ ] **LC33/LC153 旋转数组的 `right = mid` vs `right = mid - 1`**：求最小值（LC153）时 `nums[mid] < nums[right]` 说明右半有序，最小值在左半含 mid，必须 `right = mid`（不是 `mid - 1`，mid 本身可能就是最小值）。求目标值（LC33）时找到有序半段后，再判断 target 是否落在该半段来决定 `left = mid + 1` 还是 `right = mid - 1`。**最易错点**：混淆两种 `right` 更新方式——「找边界留 mid」vs「找目标排除 mid」。
- [ ] **LC206 递归反转的指针回接**：递归法 `head.next.next = head` 这一步是关键——`head.next`（反转后的新尾节点）的 next 回指向自己，再 `head.next = null` 断开原链以避免环。漏写 `head.next = null` 会导致链表尾部成环。基本情形：`head == null || head.next == null` 直接返回 head。
- [ ] **LC19 双指针的 n 步前置与 dummy 哨兵**：删倒数第 n 个节点时，如果 n 等于链表长度（删头节点），不设 dummy 会导致 `slow` 指向 head 本身而无法删除。正确做法：`dummy.next = head`，`fast = dummy` 先走 n+1 步（让 slow 停在被删节点的前驱），再同步推进。`slow.next = slow.next.next` 跳过待删节点。

### 建议刷的新题
- [ ] **数组**：Contains Duplicate（Easy）— 关联已掌握 LC1 Two Sum 的 HashMap/HashSet 思路。**核心**：遍历数组用 HashSet 记录已见元素，遇到已存在元素即返回 true。**坑**：HashSet `add()` 返回值可直接判断（`if (!set.add(num)) return true`），一行搞定；Follow-up 可练习排序后相邻比较的 O(n log n) 解法。
- [ ] **数组**：Product of Array Except Self（Medium）— 关联已掌握 LC53 一遍扫描 + LC121 贪心的前后缀思路。**核心**：不能用除法，用「左前缀积」和「右后缀积」两次遍历——第一遍 `output[i] = output[i-1] * nums[i-1]`（左积累计），第二遍反向 `right *= nums[i]; output[i] *= right`。**坑**：`output[0]` 初始为 1（无左侧元素），`right` 初始也为 1，第二遍从右往左遍历。
- [ ] **数组/双指针**：Container With Most Water（Medium）— 关联已掌握 LC1 双指针方向 + LC121 一遍扫描思维。**核心**：双指针从两端向中间收敛，面积 = `min(height[left], height[right]) * (right - left)`，移动较小的一端（因为移动大端面积只会更小）。**坑**：「短板效应」决定面积受限于较小端，移动较小端才有机会找到更高边——面试需口述为何移动大端不可能获得更大面积的论证。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 合并两个有序链表 + LC206 链表操作 + 哨兵节点技巧。**核心**：法一——分治两两合并（`mergeKLists(lists, l, r)` 对半递归，`mergeTwo(left, right)` 复用 LC21）；法二——最小堆（PriorityQueue 按 `ListNode.val` 排序）每次弹出最小节点拼到结果链表。**坑**：堆解法注意 `Comparator` 用 `a.val - b.val` 比较而非 `a - b`（对象引用）；空链表 `lists` 数组过滤；分治法复杂度 O(N log K) 比顺序两两合并 O(NK) 更优。
- [ ] **字符串/Hash Table**：Valid Anagram（Easy）— 关联已掌握 LC3 字符频次计数 + LC1 HashMap 计数思路。**核心**：长度不同直接 false；长度相同用 26 大小计数数组或 HashMap 统计 `s` 字符 +1、`t` 字符 -1，最终全 0 即 true。**坑**：排序法（`s.sorted() == t.sorted()`）虽然简洁但 O(n log n)，面试首选 O(n) 计数法；Unicode 字符场景用 HashMap 更通用。

## 历史复习记录
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
