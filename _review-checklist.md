# 🎯 面试复习清单

## 📅 今日复习（2026-05-18）

### 需要回顾
- [ ] **树 — 递归与 BFS**：LC104 最大深度（`max(left, right) + 1` 分治，`if not root: return 0` 防溢出）、LC102 层序遍历（`collections.deque` BFS 队列，`for _ in range(level_size)` 分层）、LC226 翻转二叉树（交换左右子节点后递归，`root.left, root.right = root.right, root.left`）、LC105 构造二叉树（前序首个元素为根，中序定位后分治递归，用 HashMap 缓存 `inorder` 索引 O(1) 查询）、LC235 BST 的 LCA（利用 BST 大小性质，`p.val < root.val < q.val` 时 root 即为 LCA）、LC236 二叉树的 LCA（后续遍历递归，`if left and right: return root`）— **树的递归模板是多道 DP 题的基石，务必吃透**
- [ ] **链表 — 指针操作**：LC206 反转（`prev, curr, next` 三指针迭代或 `head.next = None` 递归终止）、LC141 环检测（快慢指针 `slow = head, fast = head.next`，注意初始化避免环小死循环）、LC21 合并有序链表（哨兵 `dummy` 节点 + 双指针尾插，`l1.val < l2.val` 时接 l1 否则接 l2）、LC19 删除倒数第 N（快慢指针间隔 n 步 + `dummy` 节点统一处理头节点删除）— **链表题 90% 可以用 dummy node + 快慢指针框架解决**

### 重点坑
- [ ] **递归终止条件遗漏** — LC104 最大深度、LC226 翻转二叉树：忘记 `if not root: return ...` 会导致无限递归栈溢出。树的递归题第一步永远是写 base case
- [ ] **链表反转指针保存顺序** — LC206：`next = curr.next` 必须在 `curr.next = prev` 之前执行，否则断链后无法访问剩余节点。固定节奏：`next = curr.next → curr.next = prev → prev = curr → curr = next`
- [ ] **LC105 前序+中序构造的索引查找** — 用 `inorder.index(val)` 是 O(n²)，必须用 HashMap 缓存 `{val: index}`，否则 LeetCode 大数据集超时。同一模式也适用于后序+中序构造

### 建议刷的新题
- [ ] **字符串/哈希**：Group Anagrams（Medium）— 字符串排序后作为哈希键分桶，或用计数数组（26 长度）作为键；关联已掌握的 HashMap 模式（LC76 最小覆盖子串的双哈希表计数 + LC3 窗口去重），同一套"数据归类"思路
- [ ] **数组/双指针**：3Sum（Medium）— 排序 + 双指针遍历 + 去重跳过；关联已掌握的双指针模式（滑动窗口 + 链表快慢指针），从"两指针向中"扩展到"固定一值 + 双指针"，面试第二高频
- [ ] **DP 入门**：House Robber（Medium）— 一维 DP：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`；关联已掌握的递归分治思维（Tree 专题 LC104 的 `max(left, right) + 1` 结构与此一致），是 DP 专题的最佳突破口
- [ ] **树/DFS**：Binary Tree Maximum Path Sum（Hard）— 后序遍历 + 全局最大值，`max(0, left_gain) + max(0, right_gain) + node.val`；对 Tree 专题已有 6 题基础的你，这是自然进阶，且面经高频
- [ ] **数组/贪心**：Best Time to Buy and Sell Stock（Easy）— 一次遍历更新 `min_price` 和 `max_profit`；关联已掌握的 O(n) 扫描模式（滑动窗口 + Kadane 思想），是 Array 专题最简单的开始

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
