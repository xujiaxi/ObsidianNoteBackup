# 🎯 面试复习清单

## 📅 今日复习（2026-05-30）

### 需要回顾
- [ ] **树：递归遍历 & 构造** — LC104 最大深度（**DFS 递归取左右子树 max + 1**）、LC226 翻转二叉树（**前序交换左右子树，后序也可**）、LC102 层序遍历（**BFS 队列，每层先取 size 再出队**）、LC105 从前序中序构造二叉树（**前序定根，中序分左右，递归构造**）、LC235 BST 的 LCA（**利用 BST 大小关系二分查找，O(h)**）、LC236 二叉树 LCA（**后序遍历，左右子树含 p/q 则返回当前节点**）
- [ ] **链表：反转 & 双指针** — LC206 反转链表（**三指针 prev→curr→next 迭代，或递归到尾再回溯**）、LC141 环检测（**快慢指针，相遇则有环**）、LC21 合并有序链表（**Dummy 节点 + 双指针比较尾插**）、LC19 删除倒数第 N（**快指针先走 N 步，然后快慢同步，慢指针停在被删节点的前驱**）

### 重点坑
- [ ] **树：递归的 base case 遗漏** — 二叉树递归必须先检查 `root == null` 再访问左右子树；层序 BFS 每轮必须先取 `queue.size()` 作为该层节点数，不要在循环中动态取 size（会变）
- [ ] **链表：Dummy 节点未正确使用** — 头节点可能被修改时（删除、反转、合并），必须用 `dummy.next = head`，最终返回 `dummy.next`；**反转链表时 prev 初始化为 null 而不是 dummy**
- [ ] **链表：快慢指针终止条件** — 环检测 while 循环条件应为 `fast != null && fast.next != null`；找中点时 fast 走 2 步 slow 走 1 步，fast 到 null 时 slow 在中点

### 建议刷的新题
- [ ] **树**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 关联已掌握递归遍历（LC104/LC226），**同时遍历两棵树比较节点值，递归终止条件：都为 null → true，一个 null → false，值不同 → false**，树专题最佳 warmup 题
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握 LCA 的 BST 性质（LC235），**中序遍历升序 或 递归传递 (min, max) 区间约束；易错：只比较左右子节点与根是不够的，必须维护全局上下界**
- [ ] **树**：[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)（Easy）— 关联 Same Tree 和树遍历，**对主树每个节点调用 isSameTree(subRoot)，前序遍历即可；可用序列化 + KMP 优化到 O(n+m)**
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握反转链表（LC206）和快慢指针（LC141），**三步走：快慢找中点 → 反转后半 → 交叉合并；面试高频，融合 3 个链表核心技巧的综合题**
- [ ] **链表**：[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握合并两有序链表（LC21），**最小堆 O(n log k) 或分治合并；面试 follow-up 常考、考察对优先队列的理解**

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
