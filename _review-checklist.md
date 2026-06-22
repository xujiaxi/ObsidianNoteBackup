# 🎯 面试复习清单

## 📅 今日复习（2026-06-21）

### 需要回顾
- [ ] **图**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：Clone Graph 用 HashMap 作为新旧节点映射，先入表再递归处理邻居，防止环导致死循环；Course Schedule 三色标记法检测环（0未访问、1访问中、2已完成），状态1再次碰到说明有环，也可改用 Kahn 算法（BFS拓扑排序）用入度判断；Number of Islands 用沉岛策略直接改原数组 '1'→'0'，DFS/BFS 都可，选一个顺手的模板记住。注意矩阵访问先检查越界再检查值。**
- [ ] **二分查找**：Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：旋转排序数组的最小值用右边界判断更可靠（`nums[mid] > nums[right]` → 最小值在右边），`while (left < right)` 找极值；搜索目标值则用 `while (left <= right)`，核心是“找到有序的那一半，看 target 在不在里面”—— 左半边有序就检查 `[left, mid)`，否则检查右半边。**

### 重点坑
- [ ] **Clone Graph 中 HashMap 先入表再递归** — 如果先递归再 put，A→B→A 时 A 还没进表 → 无限递归。切记创建新节点后**立刻入表**，再处理邻居。
- [ ] **旋转排序数组二分查找与左边界比较会出错** — `nums[left]` 可能处于大段升序的任意位置，判断哪半有序时优先用 `nums[left] <= nums[mid]` 确认左半边有序，或者用右边界 `nums[right]` 判断更可靠（LC153）。
- [ ] **混淆 `while (left < right)` 和 `while (left <= right)`** — LC153 找极值用 `<`（左右相遇时退出），LC33 找目标值用 `<=`（还有元素时继续），选错模板会导致死循环或漏判。
- [ ] **Java Integer 比较用 == 而不是 equals** — 特别是 HashMap/HashSet 中超出 Integer Cache (-128 ~ 127) 范围的 `Integer` 值用 == 会判定为 false，导致逻辑错误。牢记用 `.equals()` 或自动拆箱后用基本类型比较。

### 建议刷的新题
- [ ] **图 / 多源 BFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握的 BFS/DFS（LC200 Number of Islands），**从四周海洋反向淹没，找同时能到达两个海洋的单元格90594331。是 LC200 的多源扩展。**
- [ ] **区间 / 排序**：Merge Intervals（Medium）— 关联已掌握的排序思想和 Meeting Rooms II（LC253），**先按起始位置排序，然后逐个合并重叠区间。关键是排序后只用比较当前区间的 start 和上一个 merged 区间的 end。**
- [ ] **滑动窗口 / 哈希表**：Longest Repeating Character Replacement（Medium）— 关联已掌握的滑动窗口（LC3, LC76），**可变窗口：维护频率最高的字符，看窗口减去最大频数是否在 k 范围内，不在则收缩左指针。**
- [ ] **数组 / 双指针**：Two Sum（Easy）— 关联哈希表基础用法，**一遍哈希表遍历：遍历当前数时检查 target - nums[i] 是否已在 map 中。** Hard 级别的变体（3Sum、4Sum ）都是在此基础上扩展。
- [ ] **树 / 递归**：Same Tree（Easy）— 关联已掌握的树递归思维，**同时递归比较两棵树的根值、左子树、右子树。base case：都 null 返回 true，一个 null 一个非 null 返回 false。**

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
| Heap | 1 | `heap/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Dynamic Programming | 0 | `dynamic-programming/` |
| Greedy | 0 | `greedy/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| String | 0 | `string/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：17 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：21 题**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **滑动窗口** —
- [x] **Intervals / 区间** — LC253 会议室 II
- [x] **树** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104
- [x] **链表** — LC206 + LC141 + LC21 + LC19
