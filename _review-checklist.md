# 🎯 面试复习清单

## 📅 今日复习（2026-06-01）

### 需要回顾
- [ ] **树递归/构造** — LC104 最大深度（**max(left, right) + 1，null → 0**）、LC226 翻转二叉树（**root.left, root.right = root.right, root.left，递归/迭代都要会**）、LC102 层序遍历（**BFS 队列，每层先记 size 再 for 循环**）、LC105 前序中序构造（**前序第一个是根，中序 hash 定位根，分左右递归**）、LC235 BST 的 LCA（**p/q 在 root 两侧或等于 root 则返回 root，利用 BST 性质剪枝**）、LC236 BT 的 LCA（**后序遍历，左右子树分别返回 p/q 则 root 是 LCA**）
- [ ] **链表综合** — LC206 反转链表（**三指针 prev/curr/next 或递归，迭代更安全**）、LC141 环检测（**快慢指针，快走两步慢走一步，相遇即有环**）、LC21 合并有序链表（**哨兵 dummy 节点 + 双指针比较，别忘了处理剩余**）、LC19 删除倒数第 N（**快慢指针保持 N 步差距，一次遍历**）

### 重点坑
- [ ] **树：递归基忘记处理 null** — 所有树递归必须先判断 root == null 返回 0/None；BST 合法性验证用全局 prev 指针中序遍历，不要只比较 left < root < right（会漏掉层级约束）
- [ ] **链表：反转时丢失 next 引用** — 每次移动前务必保存 `next = curr.next`，顺序是 curr → next → prev；删除节点时注意 head 可能被删除，用 dummy 节点简化
- [ ] **树：LC105 构造时中序 hash 化** — 必须先建中序值→下标的 hash 映射，不然后续每次查找 O(n) 导致整体 O(n²)，面试必问优化

### 建议刷的新题
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握 BST（LC235），**中序遍历升序 + prev 指针比较；或用递归传递 (min, max) 范围约束；两个方法都要会，面试常考变体**
- [ ] **树**：[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)（Easy）— 关联已掌握树递归（LC104/LC226），**双重递归：isSubtree 遍历每个节点 + isSame 判断两树是否完全相同；可序列化成字符串用 KMP 优化**
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握链表反转（LC206）+ 快慢指针（LC141），**三步走：快慢找中点 → 反转后半 → 交错合并；易错：后半断开连接，最后节点指向 null**
- [ ] **链表/堆**：[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握合并两链表（LC21），**优先队列 O(n log k) 或分治归并 O(n log k)；分治空间 O(1)，面试更推荐；注意自定义比较器写法**
- [ ] **数组（拓展）**：[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)（Medium）— **前缀积 + 后缀积各一次遍历，O(n) 时间 O(1) 额外空间（输出数组不算）；与 sliding window 模式互补**

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

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：20 题**

## 待复习（按优先级）

- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
