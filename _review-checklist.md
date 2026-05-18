# 🎯 面试复习清单

## 📅 今日复习（2026-05-17）

### 需要回顾
- [ ] **二分查找 — 旋转排序数组**：LC153 找最小值（与 `nums[right]` 比较，`mid < right` 舍弃右半，`mid > right` 舍弃左半）、LC33 搜索目标值（先判哪半有序，再判 target 是否在有序半内，注意 `<=` vs `<` 边界）、通用模板（`while left < right` 或 `while left <= right`，选对闭区间）— **二分查找是最高频考点之一，务必熟记两种变体**
- [ ] **滑动窗口 — 双指针模板**：LC3 无重复字符最长子串（`Set`/`Map` 维护窗口内字符，重复时左指针右移直到无重复）、LC76 最小覆盖子串（双哈希表 `need`/`have`，`required` 计数器 + `formed` 匹配数，右扩左缩）、通用模板（`for right in range(n):` 扩右 + `while` 条件满足时缩左，先处理左指针元素再 `left++`）

### 重点坑
- [ ] **二分查找右边界比较** — LC153 中与 `nums[right]` 比较而非 `nums[left]`；当 `nums[mid] < nums[right]` 时最小值在左半（含 mid），`nums[mid] > nums[right]` 时在右半（不含 mid）。注意不要混淆，写反会导致死循环或越界
- [ ] **滑动窗口左指针元素移除顺序** — 先移除/减计数，再 `left++`；顺序颠倒会导致计数错误。LC76 中特别要注意 `windowCounts[leftChar]--` 必须在 `left++` 之前
- [ ] **二分查找 mid 计算防溢出** — `mid = left + (right - left) // 2` 而非 `(left + right) // 2`；Java 中 `int` 大数相加可能溢出。Python 无此问题但建议养成好习惯

### 建议刷的新题
- [ ] **数组/哈希**：Two Sum（Easy）— HashMap 查表 O(1) 查找，面试第 1 高频题；关联已掌握的 HashMap 计数模式（LC76 最小覆盖子串），是哈希表应用的经典入门
- [ ] **数组/分治**：Maximum Subarray（Medium）— Kadane 算法 O(n) 扫描或分治 O(nlogn)；关联已掌握的分治递归思维（Tree 专题 LC104 最大深度），一题双解理解不同思路
- [ ] **数组/前缀**：Product of Array Except Self（Medium）— 前缀积 × 后缀积一次遍历；关联已掌握的数组 O(n) 扫描模式（LC3/LC76 滑动窗口），且面试极高频率
- [ ] **树/DFS**：Validate Binary Search Tree（Medium）— 中序遍历有序性 / 递归区间约束（`min`/`max` 传参）；直接拓展 Tree 专题，关联 LC235 BST 的 LCA 性质理解
- [ ] **数组/双指针**：Container With Most Water（Medium）— 双指针从两端向中间移动，每次移动较矮的边；关联已掌握的 two-pointer 模式（滑动窗口 + 链表快慢指针），面试常见变体

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
