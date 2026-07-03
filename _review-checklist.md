# 🎯 面试复习清单

## 📅 今日复习（2026-07-02）

### 需要回顾
- [ ] **树（Tree）**：Maximum Depth of Binary Tree、Same Tree、Invert Binary Tree、Construct Binary Tree from Preorder and Inorder Traversal、Validate Binary Search Tree、Lowest Common Ancestor of BST — **核心：递归三要素（终止条件、返回值、递归逻辑）；前序+中序重建树时用 HashMap 缓存 inorder 索引；BST 验证用「区间法」（左开右闭）更严谨；LCA 利用 BST 特性判断 target 在哪个分支。**
- [ ] **链表（Linked List）**：Reverse a Linked List、Detect Cycle in a Linked List、Merge Two Sorted Lists、Remove Nth Node From End Of List — **核心：反转链表注意「三指针接力」（prev, curr, next）；环检测快慢指针，相遇后快指针回到 head 同步走找入口；Dummy Node 统一头节点处理；双指针求倒数第 n 个节点时，先让快指针走 n 步。**
- [ ] **滑动窗口（Sliding Window）**：Longest Substring Without Repeating Characters、Minimum Window Substring — **核心：外层 while bulge right 指针，内层 while 满足收缩条件时收缩 left；用 HashMap/数组记录字符频率；最小覆盖子串需要维护 valid 计数和 need 字典。**

### 重点坑
- [ ] **BST 验证时仅比较左右子节点容易出错**：区间法必须传递 min/max 上下界，不能只比较当前 node.val > left.val && node.val < right.val，否则孙子节点大于根节点会漏判。
- [ ] **链表反转时指针前进顺序**：先保存 next = curr.next，再执行 curr.next = prev，最后 prev = curr, curr = next；顺序颠倒会导致指针断链。
- [ ] **滑动窗口收缩时漏掉 valid 状态的同步更新**：Minimum Window Substring 中 shrink left 后，如果 window[c] == need[c] 则 valid--；忘记减会导致 valid 虚高，窗口不是最小。

### 建议刷的新题
- [ ] **树 / 递归**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握知识：树 DFS + 后序遍历。递归返回以当前节点为端点的最大路径和，全局维护 maxSum = max(maxSum, left + right + node.val)。注意「路径」不能分叉，所以递归返回值是 max(left, right, 0) + node.val。
- [ ] **链表 / 优先队列**：Merge K Sorted Lists（Hard）— 关联已掌握知识：Merge Two Sorted Lists。用小顶堆维护 K 个链表当前头节点，每次 pop 最小插入其 next；时间 O(N log K)。也可两两合并但慢于堆。
- [ ] **字符串 / 滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握知识：滑动窗口模板。窗口内最多允许替换 k 次使字符相同，维护 maxFreq，while (right - left + 1 - maxFreq > k) 时收缩 left。
- [ ] **数组 / Kadane 算法**：Maximum Subarray（Medium）— 关联已掌握知识：数组遍历 + 动态规划入门。dp[i] 表示以 i 结尾的最大子数组和，转移 dp[i] = max(nums[i], dp[i-1] + nums[i])；可优化 O(1) 空间。
- [ ] **二叉搜索树**：Kth Smallest Element in a BST（Medium）— 关联已掌握知识：BST 中序遍历有序。递归中序遍历到第 k 个节点即为答案；也可迭代用栈，时间 O(H + k)，空间 O(H)。

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

**Blind 75 完成：20 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
