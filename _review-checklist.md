# 🎯 面试复习清单

## 📅 今日复习（2026-06-17）

### 需要回顾
- [ ] **图 DFS/BFS**：克隆图（LC133）、岛屿数量（LC200）、课程表/拓扑排序（LC207） — **核心：克隆图用哈希表存原节点→新节点，DFS/BFS均可；岛屿数量用沉岛法（DFS/BFS将访问过的1标记为0）；课程表用三色标记法检测环（0未访问/1处理中/2已完成），Kahn算法用入度数组/BFS**。注意图的连通性问题别漏掉未visited的所有节点都要作为入口。
- [ ] **滑动窗口**：无重复字符最长子串（LC3）、最小覆盖子串（LC76） — **核心：模板为外层while右指针扩展，内层while满足条件时收缩左指针。LC3用HashMap/Set维护字符位置去重；LC76维护窗口内字符计数和已匹配字符种类数**。注意LC76中t可能有重复字符，要统计数量而非单纯存在性。
- [ ] **二分查找**：搜索旋转排序数组（LC33）、寻找旋转数组最小值（LC153） — **核心：与右边界`nums[right]`比较通常更可靠。LC153判断中点与右边界比较；LC33先判断有序区间再定位**。注意单元素数组、完全未旋转数组、全部相等元素的边界情况。

### 重点坑
- [ ] **图DFS递归栈溢出** — 数据量大时深度递归会导致StackOverflow，需了解迭代DFS（显式栈）或BFS（队列）替代方案。面试中提到复杂度要同时说时间O(V+E)和空间O(V)。
- [ ] **滑动窗口收缩条件搞混** — LC3窗口内无重复时扩大，有重复时收缩左指针；LC76窗口覆盖所有t字符后才收缩求最小。写之前先明确：什么条件下扩展？什么条件下收缩？
- [ ] **二分查找与右边界比较** — 旋转数组问题中`nums[mid] > nums[right]`说明最小值在右半部分，`nums[mid] < nums[right]`在左半部分。不要和左边界比较，容易出错。
- [ ] **拓扑排序入度初始化** — 建邻接表后必须同时维护每个节点的入度，BFS时只有入度为0的节点才能入队。有向图建边方向容易搞反。
- [ ] **HashMap / HashSet 判重 vs 计数** — LC3可用Set维护窗口内字符（去重），但LC76必须用Map维护字符计数（因为t中有重复字符）。根据题目选择合适的数据结构。

### 建议刷的新题
- [ ] **数组/双指针**：Two Sum（Easy）— 关联已掌握HashMap计数思想，**用HashMap存值→索引，遍历中target - nums[i]是否已存在即可O(n)**。注意返回的是索引而非值，数组中只有一个解这个条件。
- [ ] **数组/贪心**：Best Time to Buy and Sell Stock（Easy）— 关联已掌握数组遍历/维护最值思想，**遍历时维护历史最小buy价格，每天计算当天卖的最大利润**，一次遍历O(n)，空间O(1)。
- [ ] **字符串/滑动窗口**：Longest Repeating Character Replacement（Medium）— 关联已掌握滑动窗口核心模板，**窗口内维护字符最大频率，检查窗口长度-最大频率<=k则可行，否则收缩左边界**。注意这里不需要真的替换，而是判断条件。
- [ ] **树**：Same Tree（Easy） — 关联已掌握树递归思维，**递归比较两棵树的根值、左子树、右子树是否同时相等**。base case处理null节点的情况：两个都null返回true，一个null一个非null返回false。
- [ ] **图/并查集**：Longest Consecutive Sequence（Medium）— 关联已掌握图的连通性思想，**用Set去重后遍历，只从序列起点（num-1不存在）开始向后被查连续元素**。也可用哈希表/并查集，空间换时间O(n)。

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
**总共 LeetCode 完成：23 题**

## 待复习（按优先级）

- [ ] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [ ] **图 DFS/BFS** — LC133 克隆图 + LC200 岛屿 + LC207 拓扑排序
- [ ] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [ ] **树递归/构造** — LC104 最大深度 + LC226 翻转 + LC102 层序 + LC105 构造二叉树 + LC235 LCA BST + LC236 LCA BT
- [ ] **链表综合** — LC206 反转 + LC141 环检测 + LC21 合并 + LC19 删除倒数 N
