# 🎯 面试复习清单

## 📅 今日复习（2026-07-22）

### 需要回顾
- [ ] **树与递归**：Maximum Depth of Binary Tree（LC104）、Binary Tree Level Order Traversal（LC102）、Construct Binary Tree from Preorder and Inorder Traversal（LC105）、Validate Binary Search Tree（LC98）— **核心：LC104 递归 `max(depth(left), depth(right)) + 1`，迭代 BFS 用队列逐层计数。LC102 BFS 逐层入队，`size = queue.size()` 控制当前层节点数，内层 `for` 循环弹出 size 个节点收集到子列表，再扩展下一层。LC105 前序+中序重建——前序首元素是根，在中序里找到根的索引 `idx`，左子树 = `inorder[0:idx]`，右子树 = `inorder[idx+1:]`，递归构建。LC98 验证 BST——**中序遍历必严格递增**，用 `prev` 变量记录前驱节点值；或递归传递 `min/max` 范围（左子树上限 < root.val，右子树下限 > root.val）。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：LC3 通用模板——`left=0`，`right` 右扩，遇到重复字符（在 Set 中）则内层 `while` 收缩 `left` 直到无重复，更新 `result = max(result, right - left + 1)`。LC76 滑动窗口变形——先统计 `t` 的字符频次 `need` + `missing`（还需匹配的字符种类数），`right` 扩展时匹配到 `t` 中字符则减少 `missing`，当 `missing == 0`（窗口覆盖 t）时 `left` 收缩寻找最小窗口；收缩时若弹出的字符属于 `need` 则恢复 `missing`。**

### 重点坑
- [ ] **LC102 层次遍历的队列大小快照**：必须在外层循环开始时 `int size = queue.size()` 快照当前层节点数，再写内层 `for (int i = 0; i < size; i++)`。**常见错误**：直接在 `for` 里写 `queue.size()`——因为循环体内不断 `queue.offer()` 加入下一层节点，size 实时变化，会导致当前层混入下一层节点。快照变量切断这个耦合是关键。
- [ ] **LC98 验证 BST 的范围递归 vs 中序法**：**范围递归法坑**——初学者常写 `left.val < root.val && right.val > root.val` 只检查直接子节点，但 BST 要求整棵子树都满足范围。正确写法是递归传递 `min` 和 `max`（左子树必须 < root.val，右子树必须 > root.val，且这个约束沿树向下传播）。**中序法坑**——`prev` 必须用实例变量或数组引用（(`int[] prev`）在递归中保持可变状态，普通局部变量无法跨递归层传递。不少用例目标 `Long.MIN_VALUE` 会溢出，需求改为 `Long` 或先设标志位。
- [ ] **LC105 前序+中序重建的边界处理**：在中序里找根用 `HashMap` 预存 `val → index` 避免每层线性查找。递归构建左子树时，区间是 `[preStart+1, preStart+1+leftSize-1]` 和 `[inStart, idx-1]`，右子树区间是 `[preStart+leftSize+1, preEnd]` 和 `[idx+1, inEnd]`——`leftSize = idx - inStart`（中序中根左侧的节点数），下标计算极易写错。空节点判断：`inStart > inEnd` 时返回 `null`。
- [ ] **LC76 Minimum Window 的 `missing` 计数语义**：`missing` 表示「还缺多少个字符种类」而非「还缺多少个字符实例」。当 `missing == 0` 时窗口覆盖 t，开始收缩。**关键坑**：收缩 `left` 时，弹出的字符不在 `need` 中直接跳过；在 `need` 中则 `count[c]++`（剩余需求增加），若 `count[c] > 0` 说明这个字符从「刚好满足」变为「不足」，`missing++`。这个 `count[c] > 0` 判断是窗口能否合法收缩的关键。

### 建议刷的新题
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree（递归比价两棵树是否相同）+ LC104 树的递归思维。**核心**：对 `s` 的每个节点做「以该节点为根的子树是否与 `t` 相同」的判断，相当于 LC100 在每个节点上跑一次。递归双入口 `isSubtree(s, t)` + `isSame(s, t)`。**坑**：`s == null` 直接返回 false（空树不可能是 t 的父树，除非 t 也为空），`isSame` 用递归逐节点比较。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 Validate BST（中序遍历序列）+ LC102 层次遍历。**核心**：BST 的中序遍历是升序序列，第 k 小元素即中序遍历第 k 个访问的节点。迭代中序遍历（栈模拟），弹到第 k 个即返回。**坑**：递归中序需要提前终止（用计数器），迭代法更清晰。Follow-up：BST 经常修改如何优化——可在节点结构里维护子树大小。
- [ ] **滑动窗口/字符串**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3 无重复字符最长子串 + LC76 最小覆盖子串模板。**核心**：滑动窗口维护「窗口长度 - 出现最多字符的次数 ≤ k」的约束——`right` 扩展更新 `maxFreq`，当 `right - left + 1 - maxFreq > k` 时收缩 `left`。**坑**：`maxFreq` 不需要在收缩时减小——「窗口长度 - maxFreq > k」限制窗口扩张，maxFreq 保持历史最大值，窗口只增不减，最终 `result = longest valid right - left + 1` 恒成立。
- [ ] **字符串/Hash Table**：Valid Anagram（Easy）— 关联已掌握 LC3 的字符频次计数思路。**核心**：长度不同直接 false；长度相同用 26 大小的计数数组或 HashMap 统计 `s` 的每个字符 +1，`t` 的每个字符 -1，最终全为 0 即 true。**坑**：排序法（`s.sorted() == t.sorted()`）虽然简洁但 O(n log n)，面试首选 O(n) 计数法。Unicode 字符用 HashMap 更通用。
- [ ] **数组/双指针**：Container With Most Water（Medium）— 关联已掌握 LC1 Two Sum（双指针方向）+ LC53 一遍扫描思维。**核心**：双指针从两端向中间收敛，面积 = `min(height[left], height[right]) * (right - left)`，移动较小的一端（因为移动大端面积只会更小）。**坑**：贪心直觉是正确的（可数学证明），面试中需要说明「为何移动大端不可能获得更大面积」的论证逻辑——「短板效应」决定了面积受限于较小端，移动较小端才有机会找到更高的边。

## 历史复习记录
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
