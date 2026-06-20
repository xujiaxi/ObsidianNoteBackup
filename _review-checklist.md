# 🎯 面试复习清单

## 📅 今日复习（2026-06-19）

### 需要回顾
- [ ] **图 DFS/BFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：DFS 用递归 + visited 集合防重；BFS 用队列。沉岛算法直接改值为 '0' 避免额外空间；拓扑排序用 Kahn's Algorithm（入度表 + 队列）或 DFS 三色标记法。注意递归深度大时可能栈溢出。**
- [ ] **二分查找**：旋转数组最小值（LC153）、搜索旋转排序数组（LC33） — **核心：与右边界 `nums[right]` 比较更可靠。找最小值时，若 `nums[mid] > nums[right]` 说明最小值在右侧，否则在左侧（含 mid）。搜索时先判断哪半边有序，再在有序半区内决定是否继续搜索。**
- [ ] **滑动窗口**：无重复字符最长子串（LC3）、最小覆盖子串（LC76） — **核心：外层 `while` 扩展 right 指针，内层 `while` 在满足条件时收缩 left。LC3 用 HashSet 存窗口内字符去重；LC76 用 HashMap 计数 + 变量记录已满足条件字符数，达到目标才收缩。**

### 重点坑
- [ ] **图遍历忘记标记或回溯** — DFS 时若忘记将节点标记为已访问（或忘记回溯撤销标记），会导致死循环、重复访问或错误结果。克隆图时尤其注意原节点和克隆节点的映射关系用 HashMap 维护，避免重复克隆。
- [ ] **二分查找 mid 越界** — 写 `mid = (left + right) / 2` 在 `left + right` 溢出时会出错，务必写成 `mid = left + (right - left) / 2`；比较时最好与 `nums[right]` 而非 `nums[left]` 比较，避免旋转数组中存在重复值时判断失误。
- [ ] **滑动窗口过早收缩** — 在窗口还没覆盖全部目标字符时就开始移动 left，导致结果不完整。每次移动 right 加入新字符后，只有当 `formed == required`（即窗口内已包含所有目标字符且数量足够）时，才应该用 `while` 循环收缩 left 以寻找最短窗口。

### 建议刷的新题
- [ ] **树**：Same Tree（Easy）— 关联已掌握树递归思维，**递归比较根值 + 左右子树是否同时相等。base case 处理两个都 null 返回 true，一个 null 一个非 null 返回 false。**
- [ ] **树**：Validate Binary Search Tree（Medium）— 关联已掌握的树遍历思维，**中序遍历验证单调递增（或递归维护每个节点的上下界）。不能用单一节点的孩子大小判断，必须考虑祖先节点的约束。**
- [ ] **数组/双指针**：3Sum（Medium）— 关联已掌握的排序 + 双指针思想，**排序后固定一个数，剩余部分用双指针找两数之和等于 -nums[i]。注意去重（固定值、左指针、右指针重复时都要跳过），返回的是值不是索引。**
- [ ] **链表/堆**：Merge K Sorted Lists（Hard）— 关联已掌握的链表合并和堆（会议室 II），**最小堆维护 k 个头节点，每次弹出最小节点加入结果链表，并将其 next 入堆。** Hard 级别，可作为进阶挑战。
- [ ] **哈希表/堆**：Top K Frequent Elements（Medium）— 关联已掌握的哈希表和堆，**先统计频次再用最小堆维护前 K 个高频元素。复杂度：统计 O(n)，堆操作 O(n log k)。**

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

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **Intervals / 区间** — LC253 会议室 II
