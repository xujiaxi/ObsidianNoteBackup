# 🎯 面试复习清单

## 📅 今日复习（2026-06-20）

### 需要回顾
- [ ] **树**：翻转二叉树（LC226）、构造二叉树（LC105）、LCA I/II（LC235 / LC236） — **核心：递归时想清楚 base case（空节点返回 null）。翻转二叉树直接递归交换左右子树，类似于链表反转的逻辑。构造二叉树时，用 HashMap 缓存 inorder 索引，避免 O(n) 查找根节点位置。LCA 在 BST 中利用大小关系简化判断，普通二叉树则递归查找左右子树结果，两者都非 null 则当前节点为 LCA。**
- [ ] **链表**：List 反转（LC206）、快慢指针环检测（LC141）、合并有序链表（LC21）、删除倒数第 N 个节点（LC19） — **核心：反转=迭代改 next 的方向，三个指针（prev/curr/next）配合；环检测=快慢指针（fast 走 2 步，slow 走 1 步），相交则有环；删除第 N 个节点是快慢指针的经典变体（fast 先走 N 步）。多多使用 dummy head 规避空指针。**
- [ ] **层次遍历**：Binary Tree Level Order Traversal（LC102） — **核心：BFS 用队列，每轮外层 while 处理完一层，内层 for 循环处理当前层的所有节点。注意每层结束时收集结果。**

### 重点坑
- [ ] **翻转二叉树递归时搞混左右子树** — 递归回来后还要不要交换？记住：**先递归交换子树的内部，再交换当前节点的左右子树**，或者先交换再递归都可以，但一旦先返回了子节点再交换当前节点时，注意处理的是本节点的 left/right 指针，不是子树的结果。
- [ ] **构造二叉树时忘记用 HashMap 缓存 inorder 索引** — 每轮递归都扫描 inorder 数组找根节点是 O(n²) 的。预处理 HashMap<Value, Index> 把单次查找降到 O锅盖等多种容器；) 。
- [ ] **链表反转时指针更新顺序错误** — 务必在修改 `curr.next = prev` 之前保存好 `next = curr.next`，否则链表会断裂。画图：prev ← curr → next，改的时候先保存 next。
- [ ] **Java Integer 比较用 == 而不是 equals** — 特别是 HashMap/HashSet 中超出 - programmer's Cache (-128 ~ 127) 范围的 `Integer` 值用 == 会判定为 false，导致逻辑错误。牢记用 `.equals()` 或自动拆箱后用基本类型比较。

### 建议刷的新题
- [ ] **树**：Same Tree（Easy）— 关联已掌握的树递归思维，**递归比较根值 + 左右子树是否同时相等。base case 处理两个都 null 返回 true，一个 null 一个非 null 返回 false。**
- [ ] **树**：Validate Binary Search Tree（Medium）— 关联已掌握的树遍历思维，**中序遍历验证单调递增（或递归维护每个节点的上下界）。不能用单一节点的孩子大小判断，必须考虑祖先节点的约束。**
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握的排序 + 双指针思想，**排序后固定一个数，剩余部分用双指针找两数之和等于 -nums[i]。注意去重（固定值、左指针、右指针重复时都要跳过），返回的是值不是索引。**
- [ ] **链表/堆**：Merge K Sorted Lists（Hard）— 关联已掌握的链表合并和堆（会议室 II），**最小堆维护 k 个头节点，每次弹出最小节点加入结果链表，并将其 next 入堆。** Hard 级别，可作为进阶挑战。
- [ ] **哈希表/堆**：Top K Frequent Elements（Medium）— 关联已掌握的哈希表和堆，**先统计频次再用最小堆维护前 K 个高频元素。复杂度：统计 O(n)，堆操作 O(n log k)。**

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Design | 2 | `design/` |
| Array | 1 | `array/` |
| Heap | 1 | `heap/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Dynamic Programming | 0 | `dynamic-programming/` |
| Greedy | 0 | `greedy/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| String | 0 | `string/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：21 题**

## 待复习（按优先级）

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** —
- [x] **Intervals / 区间** — LC253 会议室 II
- [x] **树** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表** — LC206 + LC141 + LC21 + LC19
