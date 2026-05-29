# 🎯 面试复习清单

## 📅 今日复习（2026-05-28）

### 需要回顾
- [ ] **树分治/遍历**：LC104 最大深度（**后序遍历 `max(left, right) + 1`，DFS 递归经典**）、LC102 层序遍历（**BFS 按层队列收集**）、LC105 构造二叉树（**前序确定根，中序分左右递归**）、LC226 翻转二叉树（**后序交换左右子节点**）、LC235 BST 的 LCA（**BST 性质：p < root < q 则 root 即为 LCA**）
- [ ] **链表综合**：LC206 反转链表（**三指针迭代或递归**）、LC141 环检测（**快慢指针相遇即环**）、LC21 合并两个有序链表（**dummy head + 双指针**）、LC19 删除倒数第 N 个节点（**快指针先走 N 步，慢指针跟随，dummy 处理边界**）

### 重点坑
- [ ] **链表 Dummy Node 遗忘** — 反转/合并/删除操作中，永远先设 `ListNode dummy = new ListNode(0); dummy.next = head;`，最后返回 `dummy.next`。尤其删除倒数 N：快指针先走 N 步后慢指针开始步进，需要 dummy 处理删除第一个节点的边界情况
- [ ] **递归栈溢出（StackOverflowError）** — 树深度递归时若树退化为链表（如斜树），递归深度过大爆栈。**面试中主动提：最坏 O(n) 栈空间，树很深可改为迭代（显式栈）**

### 建议刷的新题
- [ ] **链表**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 关联已掌握反转链表（LC206）和合并两个有序链表（LC21），**找中点 + 后半反转 + 交错合并，链表综合三合一题型**
- [ ] **树**：[Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)（Medium）— 关联已掌握中序遍历（LC102 延伸）和 BST 性质（LC235），**中序递归遍历检查严格递增，或传 min/max 上下界做前序判断**
- [ ] **数组**：[Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)（Medium）— 关联已掌握滑动窗口前缀思维（LC3/LC76），**左→右前缀积 + 右→左后缀积，O(n) 时间 O(1) 额外空间**
- [ ] **字符串**：[Group Anagrams](https://leetcode.com/problems/group-anagrams/)（Medium）— 关联已掌握哈希表 + 排序思维，**排序字符串作 key 或用字符计数数组作 key，O(n·klogk)**
- [ ] **DP**：[House Robber](https://leetcode.com/problems/house-robber/)（Medium）— 关联已掌握的分治子问题拆解 + 本周 DP 目标，**`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，空间可优化为 O(1)**

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |
| Design | 1 | `design/` |

**Blind 75 完成：16 / 75**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：18 题**

## 待复习（按优先级）

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
