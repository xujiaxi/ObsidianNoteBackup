# 🎯 面试复习清单

## 📅 今日复习（2026-05-20）

### 需要回顾
- [ ] **树 — 分治/递归/构造**：LC104 最大深度（`max(left,right)+1` 分治递归，null 返回 0）、LC102 层序遍历（BFS 队列 → 每层 for-size 分批）、LC105 前序中序构造二叉树（前序定根、中序分左右、递归分治，**关键是 HashMap 缓存中序 index**）、LC226 翻转二叉树（`TreeNode tmp = left; left = invert(right); right = invert(tmp)`，**不是 swap(left, right)**，要用临时变量）、LC235 BST 最近公共祖先（利用 BST 性质 `p.val < root.val < q.val` 判断方向，**不要写成通用二叉树 LCA**）
- [ ] **链表 — 反转/快慢/哨兵**：LC206 反转链表（`prev→curr→next` 三指针迭代 + 递归实现，**关键**：迭代中 `next = curr.next; curr.next = prev;` 顺序不能乱）、LC141 环检测（快慢指针：`while (fast != null && fast.next != null)`、**初始化必须都从 head 出发**，否则少走一步漏判环）、LC21 合并有序链表（哨兵 dummy 统一处理头节点，`while(l1 != null && l2 != null)` 双指针比较）、LC19 删除倒数第 N 个（dummy + 快慢指针差 N 步，**slow 最终指向待删节点的前驱** → `slow.next = slow.next.next`）

### 重点坑
- [ ] **树递归边界 Null 处理** — 所有树递归函数（LC104 最大深度、LC226 翻转）必须先处理 `root == null` 的情况。LC104 空节点返回 0（不是 Integer.MIN_VALUE），LC226 空节点返回 null（不是 new TreeNode()），漏掉 → 头撞 NullPointerException
- [ ] **链表 Dummy Node 遗漏** — LC19 删除链表的倒数第 N 个节点、LC21 合并有序链表：**头节点可能被改动**的操作必须用 `ListNode dummy = new ListNode(0); dummy.next = head;`，最后返回 `dummy.next` 而不是 `head`，否则头节点作为边界情况需额外 if 判断
- [ ] **LC105 前序中序构造的 index 边界** — 递归构建左右子树时，左子树长度 = `inorderRootIndex - inStart`，右子树从 `preStart + 1 + leftLen` 取。**常见错**：直接在 `preStart + 1` 上硬编码 → 递归几层后 index 越界

### 建议刷的新题
- [ ] **树/BST**：Validate Binary Search Tree（Medium）— 中序遍历单调递增递增进阶；或用递归传递 (min, max) 区间约束每个节点值范围，关联已掌握的树递归框架（LC104 分治 + LC235 BST 性质），BST 类题目核心基础，面经必考
- [ ] **链表综合**：Reorder List（Medium）— 三步走：快慢指针找中点 → 反转后半段 → 交替合并；一题检验三项基本功，关联已掌握的 LC206 反转、LC141 快慢指针、LC21 合并，大厂综合题最爱的变体
- [ ] **树/Trie**：Implement Trie (Prefix Tree)（Medium）— 多叉树结构，每个节点含 `TrieNode[26]` + `isEnd` 标记；关联已掌握的树结构概念（LC105 构造）+ 字符串前缀匹配，系统设计面试也常问，为 Word Search II 打基础
- [ ] **数组/DP**：House Robber（Medium）— 一维 DP：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，空间可优化为 O(1) 滚动数组；关联已掌握的分治递归模式（LC104 `max(left, right) + 1` 结构与 max(取, 不取) 一脉相承），DP 专题最佳突破口
- [ ] **图/DFS**：Pacific Atlantic Water Flow（Medium）— 从太平洋和大西洋边界分别逆向 DFS 向内推进，标记各自能到达的格子，交集即为答案；关联已掌握的 LC200 沉岛算法坐标遍历 + DFS 框架，同一套「从边界出发逆向遍历」思想是高频变体

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

- [ ] **树分治/构造** — LC104 最大深度 + LC102 层序 + LC105 构造二叉树 + LC226 翻转 + LC235 LCA
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
