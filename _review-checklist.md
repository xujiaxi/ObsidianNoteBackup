# 🎯 面试复习清单

## 📅 今日复习（2026-06-03）

### 需要回顾
- [ ] **树** — LC104 最大深度（**DFS 递归求高度，base case root==null 返回 0**）、LC226 翻转二叉树（**前/后序遍历 swap 左右子树，层序也能做**）、LC102 层序遍历（**BFS 队列模板，每层 for 循环按长度出队**）、LC105 构造二叉树（**前序找根、中序分左右，递归分治，注意偏移计算**）、LC235 BST 的 LCA（**利用 BST 性质，p<root<q 即 LCA，迭代比递归省栈空间**）
- [ ] **链表** — LC206 反转链表（**迭代三指针 prev/curr/next，递归从后往前理解**）、LC141 环检测（**快慢指针 Floyd 判环，fast 两步 slow 一步**）、LC21 合并两个有序链表（**Dummy Node 迭代 or 递归，注意剩余节点拼接**）、LC19 删除倒数第 N 个节点（**快指针先走 n 步，慢指针从 dummy 出发，差一步时删除**）

### 重点坑
- [ ] **树：LC105 构造索引偏移计算** — `int leftSize = index - inStart; root.left = build(preStart+1, inStart, leftSize); root.right = build(preStart+1+leftSize, index+1, inEnd)` 偏移计算极易忘加 1，建议手画例子验证
- [ ] **树：LC235 BST LCA 方向判断误区** — 条件是 `p.val < root.val && q.val < root.val` 往左，`p.val > root.val && q.val > root.val` 往右；不要用 while 循环时忘记比较另一侧；如果 p 或 q 就是 root 则直接返回 root
- [ ] **链表：Dummy Head 遗漏导致头节点特判** — LC19 删除头节点时如果没有 Dummy Head 需要额外 if 判断；LC21/LC206 用 Dummy Head 统一逻辑，最后返回 `dummy.next`
- [ ] **链表：快慢指针初始化与 null 检查** — LC141 快指针 `fast = head.next` 起步，while 循环条件必须先判 fast 再判 fast.next，防止 NPE；LC19 快指针走 n 步后要检查 null

### 建议刷的新题
- [ ] **树**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 关联已掌握树递归（LC104/LC226），**递归判断 `p.val == q.val && isSame(p.left, q.left) && isSame(p.right, q.right)`；迭代可用 BFS 双队列同步比较**
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握 BST 性质（LC235），**中序遍历递增序列 or 递归传递 `min/max` 边界；注意用 `long` 避免 `Integer.MIN_VALUE` 边界值，null 节点直接返回 true**
- [ ] **树**：[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)（Easy/Medium）— 关联 Same Tree 判断，**遍历每个节点 + isSameTree 判断子树是否相等；序列化 + KMP 可优化到 O(n)**
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握链表反转（LC206）和快慢指针（LC141），**三步法：快慢指针找中点 → 反转后半段 → 交错合并（注意切断前半段尾部）**
- [ ] **链表**：[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握合并两个有序链表（LC21），**分治归并（两两合并，O(N log k)）或 PriorityQueue min-heap 逐个取最小头节点（O(N log k)）；PriorityQueue 需自定义 Comparator 比较 ListNode.val**

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
