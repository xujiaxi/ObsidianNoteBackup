# 🎯 面试复习清单

## 📅 今日复习（2026-05-22）

### 需要回顾
- [ ] **树递归/分治**：LC104 最大深度（DFS 分治 `max(left,right)+1`，最简单的分治模板）、LC226 翻转二叉树（递归交换左右子树，**前序遍历位置操作**）、LC102 层序遍历（BFS 队列逐层收集，**`for i in range(size)` 分层写法**）、LC105 从前序与中序遍历构造二叉树（前序确定根 → 中序划分左右子树 → 递归构建，**HashMap 预存中序索引 O(1) 查找**）、LC235 BST 的 LCA（利用 BST 性质 `root.val` 在 p 和 q 之间即为 LCA，**无需递归遍历全部节点**）
- [ ] **链表**：LC206 反转链表（迭代：`prev → curr → nextTemp` 三指针逐个反转；递归：先反转后续、再让 `head.next.next = head`）、LC141 环检测（快慢指针，**`while (fast != null && fast.next != null)` 循环条件**）、LC21 合并两个有序链表（**哨兵节点 `dummy` + 尾插法**，递归写法更简洁）、LC19 删除链表倒数第 N 个节点（快慢指针法：快指针先走 N 步，然后同步移动，快指针到末尾时慢指针指向待删节点的前驱，**也要用 dummy 节点避免删除头节点时的边界问题**）
- [ ] **滑动窗口**：LC3 无重复字符最长子串（`HashMap<Character, Integer>` 记录字符最新索引，窗口收缩时 `left = Math.max(left, map.get(c) + 1)`，**left 不能回退**）、LC76 最小覆盖子串（`HashMap` 记录 t 中字符需求 → 扩展右指针满足需求 → 收缩左指针求最短，**`formed == required` 判断已全部覆盖**，此模板可解几乎所有子串问题）

### 重点坑
- [ ] **树递归返回值类型混淆** — LC104 用 `int` 返回深度，LC226 用 `TreeNode` 返回翻转后的根，LC105 用 `TreeNode` 返回构建的节点。**高频 Bug**：分治递归时混淆了「返回给父节点的值」和「当前层局部变量」—— LC105 中构建完左右子树后 `root.left = left; root.right = right;` 再 `return root`，三步顺序不能错
- [ ] **链表 dummy 节点遗忘** — 链表头可能被删除或修改时（LC19 删除头节点、LC21 合并的头不确定），**必须创建 `ListNode dummy = new ListNode(0); dummy.next = head;`** 并在最后 `return dummy.next`。面试中忘记 dummy 节点是常见扣分点
- [ ] **滑动窗口 left 移动逻辑** — LC3 中 `left = Math.max(left, map.get(c) + 1)` 用 max 防止 left 回退；LC76 中收缩时 `left++` 后要更新计数器和 `formed`。**两个模板的 left 收缩条件不同**：LC3 是无重复（窗口内字符频率 ≤1），LC76 是满足覆盖（`formed == required` 时收缩求最短）

### 建议刷的新题
- [ ] **数组/哈希**：[Two Sum](https://leetcode.com/problems/two-sum/)（Easy）— 哈希表存 `(value → index)`，遍历时检查 `target - nums[i]` 是否在表中。文件已存在可复用，哈希表查重模式关联已掌握的 LC3 滑动窗口 HashMap 写法，是「空间换时间」思维起点
- [ ] **链表综合**：[Reorder List](https://leetcode.com/problems/reorder-list/)（Medium）— 三步法：快慢指针找中点 → 反转后半段链表 → 交替合并前半和后半。关联已掌握的 LC206 反转链表 + LC141 快慢指针，链表多步操作综合题，面经高频
- [ ] **树/递归**：[Same Tree](https://leetcode.com/problems/same-tree/)（Easy）— 同时递归遍历两棵树：`if (p == null && q == null) return true;` 遇到不等立即返回 false。关联已掌握的树递归框架（LC104 分治 + LC226 递归翻转），强化「同时遍历两棵树」的比较模式
- [ ] **栈/字符串**：[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)（Easy）— 遇到开括号入栈，闭括号出栈并检查是否匹配，最后栈为空则有效。关联已掌握的拓扑排序入度概念（LC207 课程表），栈匹配是「后进先出」最经典应用
- [ ] **DP 入门**：[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)（Easy）— `dp[i] = dp[i-1] + dp[i-2]` 斐波那契递推，空间可优化为 O(1) 滚动数组。关联已掌握的 LC104 `max(left,right)+1` 分治递归模式（同一类「状态转移」思维），DP 专题零门槛突破口

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

- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
