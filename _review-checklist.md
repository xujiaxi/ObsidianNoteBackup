# 🎯 面试复习清单

## 📅 今日复习（2026-07-27）

### 需要回顾
- [ ] **树与递归**：Maximum Depth of Binary Tree（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Binary Tree Level Order Traversal（LC102）— **核心：LC104 后序递归 `max(depth(left), depth(right)) + 1`，base case `root==null` 返回 0。LC100 同时递归左右子树逐节点比对，先比 root.val 再递归 `isSame(left) && isSame(right)`。LC226 递归反转——`root.left, root.right = invert(root.right), invert(root.left)`，base case `null` 返回 null。LC102 BFS 层序——Queue 存当前层节点，外层 while 队列非空，内层 for 当前 size 逐个出队 + 左右子入队，收集本层 list 加入结果。**
- [ ] **滑动窗口 & 字符串**：Longest Substring Without Repeating Characters（LC3）、Minimum Window Substring（LC76）— **核心：LC3 滑动窗口通用模板——`right` 扩展，遇重复字符（用 HashSet/HashMap 或 `int[128]` 频次表）则收缩 `left` 直到无重复，过程中维护 `maxLen = right - left + 1`。LC76 同样「扩右缩左」但收缩条件为窗口已满足 t 的字符频次（用 `need`/`window` 频次 + `valid` 计数）——满足时缩 left 找更优解，记录起止位置；**坑**：收缩 left 时必须同步更新 `valid` 和 window 频次，打断条件易导致 BUG。**面试口述**：通用模板是「外层 while 扩展 right，内层 while 满足/违约束 收缩 left」，配合灵活的窗口状态判定。两者用 ASCII `int[128]` 优化空间到 O(1)。**
- [ ] **间隔题 / 堆：设计题**：Meeting Rooms II（LC253）、Design Hit Counter（LC362）、Design Tic-Tac-Toe（LC348）— **核心：LC253 双端 PriorityQueue 或者扫描线——题目求最少会议室数 = 任意时刻「正在开的会议数」的最大值。法 1：按 start 排序后 MinHeap 维护各会议 end，新会议 `start >= heap.peek()` 则复用（poll 后 push）；否则 push;堆大小即答案。法 2：扫描线——把 (time, ±1) 排序后扫描累加取 max。LC362 Hit Counter：环形队列存 hit 时间戳，`getHits(t)` 把窗口 `t-300` 外的过期 hit 出队并返回队列长度。LC348 Tic-Tac-Toe：行/列计数 + 主副对角线计数，玩家落子后 `rows[row] == n` 或 `cols[col] == n` 即胜。**坑**：LC253 排序时若同时按 start / end 单独排序（两个 sorted array）做扫描线，需要区分「相同时间点结束先于开始」使会议数不虚高。**面试口述**：LC253 和 LC362 都考察「时间事件 + 数据结构选型」，熟练口述复杂度（LC253 O(n log n) / LC362 getHits O(1) 均摊）。**

### 重点坑
- [ ] **LC102 BFS 层序「内层 for 循环必须先取 size」的快照问题**：Queue BFS 时如果写 `for (int i = 0; i < queue.size(); i++)`，**循环内 push 的本层子节点会污染 size**，下一轮计数错乱。正确做法是进入内层前先 `int size = queue.size()`，再 for 到 size。**坑**：Java 里用 `LinkedList<TreeNode>`，poll() + offer() 顺序也不能颠倒——先 poll 再 offer 子，size 取值时机别错。**面试口述**：手写时把「snapshot size」用注释标出来，避免面试官追问时露馅。
- [ ] **LC3 无重复字符滑动窗口的「含重复字符判定方式」**：用 HashSet 时 `set.contains(s.charAt(right))` 为真就只 `left++` 一次并 `set.remove(s.charAt(left))`——可以 AC 但对长字符串效率差（最坏 O(2n)）；用 `int[128]` 频次表时收缩条件应为「`while (window[c] > 1)`」的 while 而非 if，否则只收缩一次会漏掉多个重复。**坑**：写 `if` 时收缩完仍没去掉重复字符，下一轮 right 扩展直接把答案算错；写 HashMap 含「索引」时还应 `left = max(left, map.get(c) + 1)` 而非 `left = map.get(c) + 1`（**对 `abba` 这类字符串会回退 left**）。
- [ ] **LC76 收缩 left 时「同步更新 valid 计数」**：`valid` 是已满足的 t 中字符种类数；当 `window[c]--` 后降到 `need[c]-1` 时必须 `valid--`，**且必须在 left 移动的那一次 loop 内判**，不能在外层 right 循环里补判。**坑**：先 `left++` 再更新 window/valid 的顺序错了会漏判或错判 valid；收缩时把 `need` 里的字符 **和 need 不等的字符混在一起处理** 会错修 valid——valid 只跟「need 里出现的字符」走。此外 `t` 中有重复字符时 `need[c]` 可能 > 1，**`valid==need.size()` 比较的是种类数不是总字符数**，写错条件永远进不去「找到最小窗口」分支。
- [ ] **LC253 Meeting Rooms II「扫描线 同时间点结束事件先于开始事件」**：把 (start, +1) 和 (end, -1) 合并排序，**Comparator 必须 end 在前**，否则同一时刻刚好结束的会议室不能被复用，会议室数会虚高 1。**坑**：用 PQ 法时如果 MinHeap 存的是 Interval 对象，Comparator 写错（比较 start 而非 end）结果错；用扫描线时排序成 (time, type)，type 越小越优先（end=0 < start=1）。**面试口述**：被追问「两个会议一个 1 结束一个 1 开始能共用同一会议室吗」时回答 yes，自然推出 end 优先排序的结论。
- [ ] **LC362 Hit Counter「环形队列 vs 普通队列 的过期清理」**：用普通 FIFO 队列存 hit 时间戳，`getHits(t)` 时「**先**把 queue 头部时间 < t-300 的元素全 poll 掉」再返回队列长度——**顺序反了**（先数再 poll）会把已过期的 hit 当成新窗口内计入。**坑**：getHits 是读操作，理论上不应该有「副作用」，但 poll 会改改 queue——面试口述要明确说明 **「摊还 O(1) 因为每个 hit 至多被 poll 一次」**；高级版需要支持多线程时用 `synchronized` 或者 `ConcurrentLinkedQueue`。

### 建议刷的新题
- [ ] **树**：Binary Tree Maximum Path Sum（Hard）— 关联已掌握 LC104 Maximum Depth of Binary Tree、LC236 LCA。**核心**：在 DFS 后序过程中维护「以本节点为最高点的路径」（单侧）和「以本节点为转折点的路径」（双侧），后者更新全局 max；递归返回「单侧最大值」给上层，**不能返回双侧**（双侧路径不能跨越当前节点继续上行）。**坑**：负权节点处理——`gain = max(0, dfs(child))` 把负收益剪掉；递归返回值和答案更新值不同（单侧 vs 双侧）。
- [ ] **树**：Serialize and Deserialize Binary Tree（Hard）— 关联已掌握 LC105 由前序+中序建树、LC102 层序遍历。**核心**：序列化用前序 + 占位符（如 `#` 表示 null）；反序列化用队列 + 递归——读一个 token，`#` 返回 null，数字建节点递归构建左右子。**坑**：字符串分隔用 split(",") 后需遍历队列而非用 index 全局指针（或用 Deque，pollFirst 消费 token）；注意序列化时叶子节点要补「`#,#`」否则反序列化时无法定位 null 边界。
- [ ] **滑动窗口/字符串**：Longest Repeating Character Replacement（Medium）— 关联已掌握 LC3 无重复字符最长子串、LC76 最小覆盖子串。**核心**：长度为 k 的替换机会内，最大化窗口内「出现次数最多的字符」`maxFreq`，窗口合法条件为 `right - left + 1 - maxFreq <= k`，**不合法就缩 left**。**坑**：`maxFreq` 不需要随收缩实时减小——因为窗口只在合法时更长才更优，旧 maxFreq 偏大不会高估当前合法解；用 O(26) 内层循环算当前 maxFreq 也可保证 O(26n) 仍可接受。
- [ ] **方形矩阵 / 模拟**：Rotate Image（Medium）— 关联已掌握 LC102 层序、二维数组遍历。**核心**：n×n 矩阵原地旋转 90°——**两步法**「先转置、再水平镜像翻转」最易写：`swap(matrix[i][j], matrix[j][i])` 沿主对角线翻转（`i<j`），然后每行 `reverse`；也可用「外圈到内圈一圈一圈旋转」找 `(i, j) ↔ (j, n-1-i) ↔ (n-1-i, n-1-j) ↔ (n-1-j, i)` 四元环。**坑**：转置循环上界是 `i < j` 不是 `i <= j`（对角线不动不需要处理）；手动四元环交换时别忘 `n` 为奇数时中心元素需跳过。
- [ ] **树/BST**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 Validate BST、LC235 LCA of BST。**核心**：BST 中序遍历严格递增——做中序遍历到第 k 个返回即可；迭代写法（栈模拟中序）category 可读性更好：一路 push 左子树到栈，pop 后计数+1 等于 k 返回，然后转向右子。进阶：若频繁查询可用 「BST 节点维护子树节点数」 让每次查询 O(log n)。**坑**：递归中序时若用 `int count = 0` 传参需用类变量/数组（Java 不可传引用）；k 从 1 计数而非从 0，要避免「先 +1 再比较」把第 k 个误成第 k-1 个。

## 历史复习记录
- 2026-07-27：树与递归、滑动窗口 & 字符串、间隔题 / 设计题（堆）
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
**总共 LeetCode 完成：32 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
