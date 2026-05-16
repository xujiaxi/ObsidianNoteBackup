# 🎯 面试复习清单

## 📅 今日复习（2026-05-15）

### 需要回顾
- [ ] **二分查找 — 旋转数组**：LC153 旋转数组最小值（与右边界 `nums[right]` 比较，`mid < right → right = mid`，`mid > right → left = mid + 1`）、LC33 搜索旋转排序数组（先定位有序半区，再判断 target 是否在其中决定收缩方向）
- [ ] **滑动窗口 — 通用模板**：LC3 无重复字符最长子串（`Set/Map` 记录窗口内字符，右指针扩张，遇到重复则左指针收缩）、LC76 最小覆盖子串（`needMap` + `windowMap`，满足条件后尝试收缩左指针找最短窗口）

### 重点坑
- [ ] **二分查找边界选择** — 旋转数组找最小值，用 `nums[mid]` 与 `nums[right]` 比较而非 `nums[left]`，因为右边界在旋转后更可靠；搜索目标值时，先判断 `mid` 落在左有序区还是右有序区，再决定 target 范围
- [ ] **滑动窗口收缩时机** — 通用模板中外层 `while right < n` 扩展右指针、内层 `while` 满足条件时收缩左指针，注意内层循环结束后要移除当前字符/减少计数，否则死循环
- [ ] **Integer 对象比较** — 若窗口字符计数存在 `HashMap<Character, Integer>` 中，比较时用 `.equals(int)` 而不是 `==`，避免 Integer Cache 范围外的对象引用不同

### 建议刷的新题
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 双指针维护窗口，用 `maxFreq` 记录窗口内最高频率字符，窗口长度 - `maxFreq` > `k` 时收缩；关联已完成 LC3/LC76 滑动窗口模板
- [ ] **数组**：Maximum Subarray（Medium）— Kadane 算法，一次遍历维护 `currentSum` 和 `maxSum`，看到负数及时重置思路；与已完成旋转数组同属数组专题，面试极高频
- [ ] **数组**：Best Time to Buy and Sell Stock（Easy）— 一次遍历维护历史最低价，每日计算当前利润取最大；考察简单的一次遍历思维，贴合学过的基础模板
- [ ] **数组/哈希**：Two Sum（Easy）— HashMap 记录补数，一次遍历 O(n) 解决；面试必考第一题，可作为进入哈希表专题的桥梁
- [ ] **数组**：Product of Array Except Self（Medium）— 左前缀积 + 右后缀积两次扫描，O(1) 额外空间（输出数组不计）；关联已完成数组二分查找的空间复杂度意识

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
