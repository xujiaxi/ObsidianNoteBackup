# 🎯 面试复习清单

## 📅 今日复习（2026-06-07）

### 需要回顾
- [ ] **树递归/构造** — LC104 最大深度（**后序遍历：左右子树最大深度 +1**）、LC226 翻转二叉树（**前序或后序交换左右子节点，注意不能中序交换**）、LC102 层序遍历（**BFS 用 Queue，每层先取 size 再逐一出队**）
- [ ] **链表综合** — LC206 反转链表（**`prev`→`curr`→`next` 三指针逐节点反转，注意先保存 `next`**）、LC141 环检测（**快慢指针：快指针一次两步、慢指针一次一步，相遇则有环**）、LC21 合并有序链表（**Dummy Node + 双指针逐个比大小，收尾处理剩余链表**）

### 重点坑
- [ ] **二叉树中序不能用来翻转** — 翻转二叉树用前序或后序，用中序（左→根→右）会先把左子树翻转到右子树，再处理右子树时又把原来的左子树又翻一遍，导致左右子树都被翻转两次最终恢复原状
- [ ] **层序遍历 BFS 每层 size 要提前存** — `int size = queue.size();` 必须在开始遍历该层之前存起来，否则入队子节点后 size 会变，导致每层节点错乱；正确写法：外层 `while(!queue.isEmpty())`，内层 `for(int i=0;i<size;i++)`
- [ ] **快慢指针判断环的起点** — LC141 只是检测是否有环，若要找环入口需在相遇后把慢指针移回头节点，两指针同速前进再次相遇点即为环入口

### 建议刷的新题
- [ ] **链表**：[Merge K Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)（Hard）— 关联已掌握 LC21 合并双链表，**用最小堆（PriorityQueue）每次取最小节点，或分治合并**，是大厂常考变体
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握 LC206 反转链表 + LC141 快慢指针，**三步法：快慢指针找中点 → 反转后半段 → 交替合并两段**，综合考察多个链表技巧
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握 BST 性质（LC235 LCA），**中序遍历应递增，或递归传递 `(min, max)` 区间**，边界值用 Long 防止溢出
- [ ] **树**：[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)（Hard）— 关联已掌握 LC102 层序 + LC105 前序构造，**BFS/DFS 序列化到字符串，反序列化按相同顺序重建**，面试高频
- [ ] **树**：[Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)（Medium）— 关联已掌握树结构（LC102），**`TrieNode` 含 `children[26]` 和 `isEnd` 标志，插入/搜索/前缀搜索均为 O(len)**，为后续 Word Search II 做铺垫

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
