# 🎯 面试复习清单

## 📅 今日复习（2026-07-11）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200）— **核心：沉岛算法（将 visited 陆地标记为水）避免重复访问；三色标记法（0未访问/1访问中/2已访问）检测有向环；Kahn 算法拓扑排序（BFS 入度归零）。Clone Graph 用哈希表映射原节点→克隆节点，BFS/DFS 遍历时同步建立邻居连接。岛屿数量 DFS 每次遇到 '1' 就沉掉整块岛。**
- [ ] **二分查找**：Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33）— **核心：与右边界 `nums[right]` 比较决定中点在哪半边；旋转数组中 `mid > right` → 最小值在右半边，否则在左半边（含 mid）。搜索目标值时先判断 `mid` 在左有序段还是右有序段，再缩小范围。模板用 `while(left < right)` 收缩或 `while(left <= right)` 标准二分。**
- [ ] **数组基础**：Two Sum（LC1）、Best Time to Buy and Sell Stock（LC121）— **核心：Two Sum 哈希表一次遍历 O(N)；买卖股票维护 minPrice 和 maxProfit，每天检查「今天卖是否更赚」并更新最低买入价。两道题都体现了「遍历时维护历史状态」的数组思想。**

### 重点坑
- [ ] **二分查找边界条件与旋转数组死循环**：`while(left <= right)` vs `while(left < right)` 的选择决定返回值是 left 还是 right。旋转数组中 `mid` 计算注意整数溢出（`mid = left + (right - left) / 2`），且中点偏移一格可能导致死循环，务必手写模板验证。
- [ ] **图的克隆中遗漏双向连接**：Clone Graph DFS 遍历邻居时，不仅要 `clone.neighbors.add(map.get(neighbor))`，也要确保邻居节点本身已被创建并放入 map。BFS 同样要先 clone 当前节点再处理邻居，漏掉任一方向都会导致结构不完整。
- [ ] **图 DFS visited 标记时机**：在入栈/递归前就标记 visited（或沉岛），而不是在递归返回后标记。否则同一节点会被重复入队/入栈，导致栈溢出或无限循环。BFS 同样：入队时标记，不要出队才标记。
- [ ] **Two Sum 哈希表 vs 暴力**：牢记哈希表 O(N) 解法，面试中提完暴力法立刻给出哈希优化。注意题目是否要求返回索引（则不能先排序），若返回值则可排序 + 双指针。
- [ ] **买卖股票 minPrice 初始化**：`minPrice = prices[0]`，不要初始化为 0 或 MAX_VALUE 而不处理第一天。遍历从 `i=1` 开始，先算利润再更新最低价（先卖后买逻辑）。

### 建议刷的新题
- [ ] **数组 / 双指针**：3Sum（Medium）— 关联已掌握知识：Two Sum（LC1）哈希表思想 + 排序双指针。先排序，固定一个数后用双指针找剩余两数之和，注意去重（跳过重复元素），O(N²) 时间 O(1) 额外空间。
- [ ] **图 / 矩阵 DFS**：Pacific Atlantic Water Flow（Medium）— 关联已掌握知识：Number of Islands（LC200）矩阵 DFS。反向思维：从太平洋和大西洋边界分别做 DFS，标记能流到的格子，最后取交集。注意逆向水流（只能往高处或等高处流）。
- [ ] **数组 / DP（Kadane）**：Maximum Subarray（Medium）— 关联已掌握知识：买卖股票（LC121）一维遍历维护状态。Kadane 算法维护 `curMax = max(num, curMax + num)`，全局记录最大值。面试中分治法和贪心法都要能讲。
- [ ] **数组 / 双指针**：Container With Most Water（Medium）— 关联已掌握知识：双指针技术。左右指针向中间移动，每次移动较短的板，面积 = 距离 × 较短板高。证明移动短板不会漏掉最优解。
- [ ] **区间合并**：Merge Intervals（Medium）— 关联已掌握知识：Meeting Rooms II（LC253）区间排序思维。按 start 排序后遍历，合并重叠区间（当前 start ≤ 上一个 end），更新 end 为两者最大值。

## 历史复习记录
- 2026-07-11：图论 BFS/DFS、二分查找、数组基础
- 2026-07-07：滑动窗口、链表、树 DFS/BFS
- 2026-07-05：图论 BFS/DFS、二分查找、数组基础
- 2026-07-04：树与递归、链表、动态规划入门 — 股票系列
- 2026-07-03：数组 & 二分查找、图论 BFS/DFS、字符串 & 滑动窗口

## 📊 LeetCode 刷题进度

| 专题 | 已完成 | 目录 |
|------|--------|------|
| Tree | 8 | `tree/` |
| Dynamic Programming | 5 | `dynamic-programming/` |
| Linked List | 4 | `linked-list/` |
| Graph | 3 | `graph/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
| Array | 1 | `array/` |
| Greedy | 1 | `greedy/` |
| Heap | 1 | `heap/` |
| String | 1 | `string/` |
| Backtracking | 0 | `backtracking/` |
| Bit Manipulation | 0 | `bit-manipulation/` |
| Hash Table | 0 | `hash-table/` |
| Math | 0 | `math/` |
| Prefix Sum | 0 | `prefix-sum/` |
| Sorting | 0 | `sorting/` |
| Stack & Queue | 0 | `stack-queue/` |
| Sweep Line | 0 | `sweep-line/` |
| Trie | 0 | `trie/` |
| Two Pointers | 0 | `two-pointers/` |
| Union Find | 0 | `union-find/` |

**Blind 75 完成：21 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：30 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
