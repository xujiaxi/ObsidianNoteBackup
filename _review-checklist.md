# 🎯 面试复习清单

## 📅 今日复习（2026-05-13）

### 需要回顾
- [ ] **数组 — 旋转数组二分搜索**：Find Minimum in Rotated Sorted 的 `nums[mid] vs nums[right]` 判断有序半边、Search in Rotated Sorted 先找最小再二分 vs 直接二分判断目标所在区间
- [ ] **滑动窗口 — 经典双指针模板**：LC3 最长无重复子串（Set 记录窗口内字符 + left 收缩）、LC76 最小覆盖子串（need/have 计数器 + valid 条件判断）

### 重点坑
- [ ] **旋转数组二分** — 比较 `nums[mid]` 和 `nums[right]`（而不是 left）更可靠；边界条件用 `<=` 或 `<` 容易混淆导致死循环
- [ ] **滑动窗口收缩** — LC76 中移动 left 时需要同步更新窗口计数器（`window[c].count--`），否则 valid 状态不会正确变化
- [ ] **BST 验证** — 不能只检查左右子节点值，必须用 `(min, max)` 范围参数传递到递归中
- [ ] **链表反转递归** — `head.next.next = head` 不是同时赋值，面试时迭代版（三指针分步）更不易出错

### 建议刷的新题
- [ ] **数组**：Maximum Subarray（Medium）— Kadane 算法（局部最优 + 全局最优），与已掌握的二分搜索形成数组专题互补
- [ ] **字符串**：Longest Repeating Character Replacement（Medium）— 滑动窗口变体（窗口内最多替换 k 个字符），与已完成 LC3/LC76 同 pattern 延伸
- [ ] **树**：Validate Binary Search Tree（Medium）— (min, max) 范围递归验证 BST 性质，从已完成 LCA of BST 延伸
- [ ] **图**：Pacific Atlantic Water Flow（Medium）— 从边界向内 DFS/BFS 逆向思维，与已完成 Number of Islands 互补
- [ ] **链表**：Reorder List（Medium）— 找中点 → 反转后半 → 交替合并，综合三大链表操作

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 6 | `tree/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |

**Blind 75 完成：13 / 75**（见 `knowledge/blind-75-overview.md`）

## 待复习（按优先级）

- [ ] **旋转数组二分** — `nums[mid] vs nums[right]` 判断有序半边
- [ ] **滑动窗口通用模板** — 外层扩展右指针，内层收缩左指针

## 本周目标

- [ ] 完成 DP 专题（Climbing Stairs, Coin Change, House Robber）
- [ ] 完成 Interval 专题（Merge Intervals, Insert Interval）
