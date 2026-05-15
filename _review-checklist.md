# 🎯 面试复习清单

## 📅 今日复习（2026-05-14）

### 需要回顾
- [ ] **链表 — 反转与环检测**：LC206 反转链表（pre/cur/next 三指针迭代，或递归到 base case 再反转连接）、LC141 环检测（快慢指针，快指针两步慢指针一步，相遇即有环）
- [ ] **链表 — 合并与删除**：LC21 合并两个有序链表（dummy 节点 + 双指针尾插）、LC19 删除链表倒数第 N 个节点（快慢指针拉开 N 步，一次遍历定位）
- [ ] **图 — DFS/BFS 模板**：LC133 克隆图（BFS 队列 + HashMap 映射原→克隆节点，避免重复拷贝）、LC200 岛屿数量（沉岛算法，DFS 四个方向标记为水）、LC207 课程表（拓扑排序 Kahn 算法，入度数组 + 队列处理）
- [ ] **树 — 深度与 LCA**：LC104 最大深度（分治递归，左子树和右子树最大深度 + 1）、LC235 BST 最近公共祖先（利用 BST 性质，一次遍历比较 root 与 p/q 大小）、LC105 前序中序构造二叉树（前序定根、中序分左右，递归构建）

### 重点坑
- [ ] **链表反转丢失引用** — 迭代反转时，先保存 `next = curr.next`，再断开 `curr.next = prev`，否则断链后找不到剩余结点
- [ ] **快慢指针步数差** — 环检测快指针走 2 步、慢指针走 1 步（步数差 1 确保必定相遇）；删除倒数第 N 个则快指针先走 N 步，慢指针再同步前进
- [ ] **图 DFS 递归过深** — LC200 岛屿 DFS 在超大网格上可能导致 StackOverflow，记住可以用 BFS 队列替代递归消除栈溢出风险
- [ ] **克隆图重复访问** — BFS/DFS 必须用 visited map 检查结点是否已被克隆，否则会重复创建结点导致死循环或引用错误

### 建议刷的新题
- [ ] **链表**：Reorder List（Medium）— 找中点（快慢指针）→ 反转后半段 → 交错合并，关联已完成 LC206 反转 + LC21 合并，一道题串起三个核心链表技能
- [ ] **链表/堆**：Merge K Sorted Lists（Hard）— 分治法两两合并（关联 LC21 Merge Two Sorted）或用最小堆 O(N log k)，链表进阶必考题
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— 从太平洋和大西洋边界分别 DFS/BFS，两个 boolean 矩阵记录可达性，关联 LC200 岛屿思维的延伸
- [ ] **数组**：Maximum Subarray（Medium）— Kadane 算法，一次遍历维护当前和与全局最大和，与已完成旋转数组二分同属数组类，面试极高频
- [ ] **树**：Serialize and Deserialize Binary Tree（Hard）— 前序/层序遍历序列化 + 递归反序列化，关联 LC105 构建二叉树，字符串编码思维考察全面

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）

## 待复习（按优先级）

- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **树分治** — LC104 最大深度 + LC235 LCA + LC105 构造二叉树

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
