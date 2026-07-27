# 🎯 面试复习清单

## 📅 今日复习（2026-07-26）

### 需要回顾
- [ ] **链表**：Reverse a Linked List（LC206）、Remove Nth Node From End of List（LC19）、Detect Cycle in a Linked List（LC141）、Merge Two Sorted Lists（LC21）— **核心：LC206 经典三指针迭代反转 `prev=null, cur=head`，每步存 `next=cur.next` 再 `cur.next=prev`，往前挪 `prev=cur, cur=next`，最后 `prev` 是新头。LC19 一次遍历删除倒数第 N 个——快慢指针间距 N+1：快指针先走 N+1 步，然后快慢同步，fast 到底时 slow 恰在被删节点的前驱位置 `slow.next = slow.next.next`，必须用 `dummy` 哨兵节点处理删除头节点的边界。LC141 环检测——快慢指针若相遇则有环，fast 走 2 步 slow 走 1 步，**相遇条件要在 while 内 `fast != null && fast.next != null` 后再移动**，且 fast/slow 同起点或慢一格起步皆可。LC21 合并两有序链表——Dummy Head + 双指针比较 `l1.val vs l2.val`，尾插法维护 `tail.next = smaller`，**最后把剩余链直接挂到 `tail.next`**。**
- [ ] **图论 BFS/DFS**：Number of Islands（LC200）、Course Schedule（LC207）、Clone Graph（LC133）— **核心：LC200 沉岛算法（Sinking Island）——遍历 grid，遇 '1' 计数 + DFS/BFS 把相连陆地标记为 '0'（原地修改避免 visited 矩阵的 O(mn) 额外空间），**坑**:原地修改破坏输入，面试时需主动确认是否允许；不确认时应改用 `boolean[][] visited` 或先复制。LC207 三色标记法环检测——0 未访问/1 访问中（再遇=环）/2 已完成（再遇=剪枝，避免重复遍历），DFS 外层对每个未访问节点调用，**关键**：return 前必须把 `visited[curr]=2` 标记完成。LC133 克隆图——HashMap `oldNode→newNode` 存新旧节点映射，DFS/BFS 先建节点再递归/迭代处理邻居；**坑**：建邻居时先查 map 看邻居是否已 clone，已 clone 直接连边，未 clone 则递归建并连边。**
- [ ] **动态规划（股票系列）**：Best Time to Buy and Sell Stock III（LC123）、Best Time to Buy and Sell Stock with Cooldown（LC309）— **核心：LC123 状态机 DP 至多 2 次交易——4 个状态变量 `buy1/sell1/buy2/sell2`，转移方程 `sell1=max(sell1, buy1+price)`、`buy2=max(buy2, sell1-price)`、`sell2=max(sell2, buy2+price)`，**初始化**：`buy1 = buy2 = -prices[0]`、`sell1 = sell2 = 0`（可在第一日做 0 利润虚拟交易）。LC309 冷冻期 DP——每天有 3 个状态（持有/冷冻后可买/冷冻中），`s0=今天不持有非冷冻（可买）`、`s1=今天持有`、`s2=今天冷冻（刚卖出）`，转移 `s0=max(s0, s2)`、`s1=max(s1, s0-price)`、`s2=s1+price`，答案 `max(s0, s2)`。**

### 重点坑
- [ ] **LC19 快慢指针走「N+1 步」而非 N 步**：要走 N+1 步才能让 `slow` 停在被删节点的**前驱**，走 N 步则 `slow` 指向被删节点本身（无法删除）。**坑**：删头节点时若不用 `dummy = ListNode(0, head)`，外层会直接 `head = head.next`，循环终止条件和返回值都需要特判。**面试口述**：`fast, slow = dummy, dummy` 同时从 dummy 出发能统一覆盖「删头节点」特殊情形，回答里**强调使用哨兵节点是关键**。
- [ ] **LC206 反转链表「先存 next 再改指针」的顺序**：迭代法每步顺序必须是 `① next = cur.next` → `② cur.next = prev`（反转指针）→ `③ prev = cur` → `④ cur = next`。**坑**：若先改 `cur.next = prev` 再取 `next = cur.next`，`next` 就丢了原后继。递归写法（`head.next.next = head; head.next = null`）更易记但需注意 `null` 断尾，否则成环。**面试口述**：怕错的训练——在白板上画 3 个节点走一遍 4 步就清楚。
- [ ] **LC200 沉岛算法的「原地修改破坏输入」问题**：DFS/BFS 把访问过的 `'1'` 改为 `'0'` 可省 visited 空间（O(1) 额外 vs O(mn) visited 矩阵）。**坑**：若面试官不允许破坏原 grid，需要单独维护 `boolean[][] visited` 或先 O(mn) 复制 grid；也可改用 BFS 队列带 visited 数组。此外沉岛必须确保每次 **扩大搜索时 4 个方向都判越界**（`dirs = [(0,1),(0,-1),(1,0),(-1,0)]`），漏方向会出现「孤岛计数」错误。
- [ ] **LC207 三色标记法状态「2=已完成」漏标导致死循环或重复遍历**：DFS 退出前必须 `visited[curr] = 2`，否则同一节点会被多次重复 DFS 递归（指数退化），而且健壮性差。**坑**：判断环用的是 `state==1`（访问中再遇=环）而非 `state==2`；先 push 一个节点时 `visited[curr]=1` 应在「进入循环前」设，循环回来验证时再 push。**面试口述**：熟练口述三色标记的「2 不必再次遍历，省下递归调用」是剪枝核心。

### 建议刷的新题
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 Merge Two Sorted Lists、LC19 快慢指针。**核心**：分治两两归并 O(N log K)，或最小堆 PriorityQueue O(N log K)（堆顶取当前最小节点，连接后 next 入堆）。**坑**：PriorityQueue 的 Comparator 按 `val` 排；分治递归 `merge(0, n-1)` base case 区间为空返回 null。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握 LC206 反转、LC141 快慢指针。**核心**：① 快慢指针找中点 ② 反转后半段 ③ 交错拼接前后两半。**坑**：快慢指针停在「前半段最后一个」（`slow` 停在中点偏左），断尾后才能独立反转；拼接时同时推进两个指针，`next` 备份顺序别乱。
- [ ] **图论**：Pacific Atlantic Water Flow（Medium）— 关联已掌握 LC200 DFS 岛屿、LC133 图遍历。**核心**：从两个海洋分别逆向 DFS/BFS 找能流入各自海洋的格子集合，取交集即为答案。**坑**：逆向 BFS 从沿海边界出发，需两个 `boolean[][]` 分别记录 Pacific/Atlantic 可达；交集后顺序输出。
- [ ] **图论**：Number of Connected Components in an Undirected Graph（Medium，Premium）— 关联已掌握 LC207 邻接表建图、LC200 遍历。**核心**：Union-Find 或 DFS 遍历，统计连通分量数。**坑**：Union-Find 的路径压缩（`find(x)` 时挂到根）和按秩合并（带 rank 数组）配合可达近 O(1) 均摊；用 DFS 时每访问一个未访问节点就 +1 计数。
- [ ] **数组/前缀积**：Product of Array Except Self（Medium）— 关联已掌握 LC53 数组遍历 + LC1 巧用辅助空间。**核心**：输出 `res[i] = 左侧所有数之积 × 右侧所有数之积`，两次遍历「先从左累乘（res[i] 是左侧积前缀），再从右累乘（res[i] *= runningRight）」，**禁用除法**。**坑**：O(1) 额外空间除答案数组外——只能用 1 个 runningRight 变量；常见错误是漏掉初始化 `res[0] = 1`，或在第二遍时把 res[i] 直接赋值为右侧积而非 `*=` 累乘左侧积。

## 历史复习记录
- 2026-07-26：链表、图论 BFS/DFS、动态规划（股票系列）
- 2026-07-25：滑动窗口 & 字符串、数组 & 二分查找、设计题
- 2026-07-24：树与递归、图论 BFS/DFS、动态规划（股票系列）
- 2026-07-23：数组 & 二分查找、链表
- 2026-07-22：树与递归、滑动窗口 & 字符串
- 2026-07-20：图论 BFS/DFS、链表
- 2026-07-19：动态规划、数组 & 二分查找
- 2026-07-18：树与递归、图论 BFS/DFS、滑动窗口 & 字符串
- 2026-07-17：数组 & 二分查找、链表
- 2026-07-16：树与递归、图论 BFS/DFS
- 2026-07-15：链表、滑动窗口 & 字符串
- 2026-07-14：数组 & 二分查找、图论 BFS/DFS
- 2026-07-13：树与递归、动态规划
- 2026-07-12：滑动窗口、链表
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
| Array | 2 | `array/` |
| Binary Search | 2 | `binary-search/` |
| Design | 2 | `design/` |
| Sliding Window | 2 | `sliding-window/` |
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

**Blind 75 完成：22 / 76**（见 `knowledge/blind-75-overview.md`）
**总共 LeetCode 完成：31 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
