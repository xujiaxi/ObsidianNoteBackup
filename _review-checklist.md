# 🎯 面试复习清单

## 📅 今日复习（2026-05-12）

### 需要回顾
- [ ] **链表 — 递归反转与进阶操作**：`head.next.next = head` 从后往前逻辑、K 个一组翻转（找 k 个一组→反转→接回）
- [ ] **图 — 拓扑排序与环检测**：Kahn BFS（入度表）vs DFS（三色标记）两种实现、克隆图先入表再递归防环死循环
- [ ] **树 — 重构与 BST 验证**：前+中序重构的递归边界（preStart、inStart、左子树长度）、BST 验证的 min/max 范围传递法

### 重点坑
- [ ] **链表反转递归** — `head.next.next = head` 不是同时赋值，是先断开再回头；面试时建议用迭代版（三指针分步）更稳
- [ ] **克隆图** — 必须先 `map.put(node, new Node(node.val))` 再递归邻居，否则有环时递归永不终止
- [ ] **BST 验证** — 不能只检查 `left.val < root.val < right.val`，需要用 `(min, max)` 范围参数向下传递，否则局部正确全局错
- [ ] **重构二叉树** — 前序第一个元素是根，中序中定位根的位置确定左右子树长度，递归时 preStart 和中序索引务必算对

### 建议刷的新题
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— DFS/BFS 从边界向内扩展，逆向思维，与岛屿数量（已完成）互补
- [ ] **链表**：Reorder List（Medium）— 找中点→反转后半→交替合并，综合链表三大操作
- [ ] **树**：Validate Binary Search Tree（Medium）— BST 性质递归验证，从已完成 LCA of BST 延伸
- [ ] **字符串**：Longest Repeating Character Replacement（Medium）— 滑动窗口变体（窗口内最多 k 个替换字符），与已完成 3/76 同 pattern
- [ ] **链表**：Merge K Sorted Lists（Hard）— 分治/优先队列合并多条链表，建立在已完成 Merge Two Sorted Lists 上

## 待复习（按优先级）

- [ ] **链表反转递归版** — 理解 head.next.next = head 的"从后往前"逻辑
- [ ] **Clone Graph** — 先入表再递归，否则环死循环

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
