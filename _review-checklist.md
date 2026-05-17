# 🎯 面试复习清单

## 📅 今日复习（2026-05-16）

### 需要回顾
- [ ] **链表 — 反转 & 环检测**：LC206 反转链表（迭代 pre/cur/next 三指针，递归后序反转）、LC141 环检测（快慢指针，相遇即存在环）、LC21 合并两个有序链表（哨兵节点 + 递归/迭代）、LC19 删除倒数第 N 个节点（快慢指针 + dummy head 避免头节点边界处理）
- [ ] **图 — DFS/BFS & 拓扑排序**：LC133 克隆图（DFS/BFS + HashMap<原节点, 新节点> 映射）、LC200 岛屿数量（沉岛算法：访问过的 '1' 变 '0' 避免重复）、LC207 课程表（Kahn BFS 入度表 / DFS 三色标记环检测，0=未访问 1=访问中 2=已完成）
- [ ] **树 — 递归 & 遍历**：LC104 最大深度（分治 `max(left,right)+1`）、LC226 翻转二叉树（前序交换左右子树）、LC102 层序遍历（BFS 队列逐层输出 `size` 层内循环）、LC105 构造二叉树（Preorder 找根，Inorder 分左右子树）、LC235 BST 的 LCA（利用 BST 性质，`root.val` 在 `p.val` 和 `q.val` 之间即为答案）

### 重点坑
- [ ] **链表 Dummy Head 遗漏** — 删除倒数第 N 个节点（LC19）或合并有序链表（LC21），用 dummy node 做哨兵，避免单独处理头节点删除/插入的边界情况，返回 `dummy.next`
- [ ] **图 DFS 栈溢出风险** — 岛屿数量（LC200）DFS 递归在岛屿极大时可能 StackOverflowError，可用 BFS 或显式栈替代；Course Schedule 三色标记法注意在递归返回后及时标记为 2（已完成）
- [ ] **树索引偏移计算** — 构造二叉树（LC105）中，`leftSize = inorderRootIdx - inStart`，根在 preorder 的偏移是 `preStart + 1` 到 `preStart + leftSize`，inorder 区间是 `inStart` 到 `inorderRootIdx - 1`；左子树大小容易算错导致数组越界

### 建议刷的新题
- [ ] **链表**：Reorder List（Medium）— 快慢指针找中点 + 反转后半段链表 + 交替合并；综合了已掌握的链表反转（LC206）和双指针（LC141）技巧，高频考点
- [ ] **字符串/双指针**：Valid Palindrome（Easy）— 双指针从两端向中间扫描，跳过非字母数字字符；关联已掌握的 two-pointer 模式（LC3/LC76 滑动窗口），面试常问
- [ ] **字符串/哈希**：Group Anagrams（Medium）— 排序字符串作为 HashMap key 分组，O(n·klogk)；关联已掌握的 HashMap 计数表（LC76）和哈希映射思维（LC133 克隆图）
- [ ] **堆/哈希**：Top K Frequent Elements（Medium）— HashMap 统计频率 + 小顶堆维护 Top K，O(nlogk)；拓展已掌握的哈希表应用，面试极高频率
- [ ] **DP 入门**：Climbing Stairs（Easy）— 斐波那契递推 `dp[i] = dp[i-1] + dp[i-2]`，可优化 O(1) 空间；关联已掌握的树递归分治思维（LC104 最大深度），是 DP 专题的最佳入门题

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
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
