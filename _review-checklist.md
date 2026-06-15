# 🎯 面试复习清单

## 📅 今日复习（2026-06-14）

### 需要回顾
- [ ] **链表综合**：LC206 反转链表、LC141 环检测、LC21 合并两个有序链表、LC19 删除倒数第N个节点 — **反转链表牢记「保存 next → 改 cur.next → 移动 prev/cur」三步走；环检测用快慢指针（都从 head 出发），相遇后 slow 重置 head 同速找入口；合并链表多用 Dummy 哨兵节点简化边界；删除倒数第N个节点用双指针保持 n+1 间距**。
- [ ] **树与递归**：LC104 最大深度、LC226 翻转二叉树、LC102 层序遍历、LC105 从前序/中序构造二叉树、LC235/236 最近公共祖先 — **后序遍历天然适合求深度/路径和；翻转树直接交换左右子树再递归；层序用队列 BFS；前序找根、中序分左右递归构造；LCA 递归条件：`p/q 分别在左右子树` 或 `当前节点就是 p/q`**。

### 重点坑
- [ ] **链表反转断链** — 反转前务必先保存 `next = cur.next`，再改 `cur.next = prev`，最后移动 `prev` 和 `cur`。顺序不可颠倒，否则丢失后续节点。
- [ ] **链表环检测快慢指针初始化** — fast 和 slow 都从 `head` 出发，不是 `head.next`。第一次相遇后，slow 重新指向 head，fast/slow 都以 1 步前进，再次相遇点即环入口。
- [ ] **构造二叉树时索引越界** — 前序第一个元素是根，在中序中找到根的位置 `idx`，递归时左右子树的区间边界要准确：`inorder [left, idx-1]` 和 `[idx+1, right]`，前序对应长度切分。
- [ ] **LCA 递归返回值处理** — 左右子树分别递归，如果两边都非 null 说明 p/q 分居两侧，当前节点就是 LCA；如果只有一边非 null 则返回那一边。注意短路判断，不要遗漏。
- [ ] **层序遍历忘记队列大小** — BFS 时每层要记录当前队列大小 `size`，用 for 循环处理完当前层再进入下一层，否则层级会错乱。

### 建议刷的新题
- [ ] **链表**：Reorder List（Medium）— 关联已掌握链表反转 + 快慢指针，**先拆成两半、反转后半、再交错合并**，考察链表操作的综合能力。
- [ ] **树**：Same Tree（Easy）— 关联已掌握树递归基础，**递归判断结构和值完全相同的条件**，是树类问题最核心的热身题。
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握滑动窗口框架，**维护窗口内最高频字符，`windowLen - maxFreq ≤ k` 则窗口有效，否则收缩左边界**。
- [ ] **图 / BFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 岛屿数量，**从四条边界逆流 DFS/BFS，标记能流向太平洋/大西洋的格子，取交集**。
- [ ] **树 / 路径**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握树的后序遍历，**递归返回单臂最大和（含负数要取 max(0, 子树和next))**，记录全局最大路径。

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

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：20 题**

## 待复习（按优先级）

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
