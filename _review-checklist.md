# 🎯 面试复习清单

## 📅 今日复习（2026-08-02）

### 需要回顾
- [ ] **树与递归（基础）**：Maximum Depth（LC104）、Same Tree（LC100）、Invert Binary Tree（LC226）、Level Order Traversal（LC102） — **核心：递归三要素——base case（空节点返回 0 / True / None）、左右子树递归、汇总（max+1、逻辑与、swap 后递归）；LC102 层序 BFS 模板——deque 队列 + 每层开始前固定 `len(q)` 决定本层节点数。**面试口述**：树的题先定「遍历方式」——求高度/翻转用递归，按层输出用 BFS，路径/祖先用 DFS；递归永远先写 base case 再写递推。**坑：LC102 必须用 deque（`list.pop(0)` 是 O(n)）；内层循环用 `range(len(q))` 固定长度，循环中动态取 len 会把下一层节点混进当前层；LC104 递归栈深 O(H)，链状树（退化成链表）可能 StackOverflow，数据量大换迭代。**
- [ ] **树与递归（进阶）**：Construct Binary Tree（LC105）、Validate BST（LC98）、LCA of BST（LC235）、LCA of Binary Tree（LC236） — **核心：LC105 preorder 第一个元素永远是当前根 + inorder 以根为界切左右子树，用 HashMap 存 inorder 值→索引加速查找；LC98 双模板——上下界递归（向下传 (min, max) 开区间）或中序遍历（序列严格递增，是 BST 充要条件）；LC235 利用 BST 值大小「指路」——p、q 同侧就往下走，一左一右（或一个是 root）即 LCA，迭代 O(1) 空间；LC236 后序汇总——左右子树各自找 p/q，两边都有结果当前节点就是 LCA。**面试口述**：BST 题先想能否用值大小剪枝；「验证」类题中序递增是充要条件，但上下界法在错误靠近根时剪枝更早。**坑：LC98 绝不能只看直接子节点（必须传上下界或整棵子树中序），反例 [5,1,4,null,null,3,6]；节点值可能为 0 → 边界判断用 `is not None` 不用隐式布尔；`prev >= node.val` 是严格递增（重复值非法）；LC105 `pre_idx` 自增必须在递归前，且必须先递归左再递归右（preorder 顺序 [根,左,右]，反了重建出错）；LC236 base case `if not root or root == p or root == q` 同时处理空节点与命中。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：LC206 三指针 prev/curr/next_temp 迭代反转（O(1) 空间，面试首选），或递归 `head.next.next = head`（从后往前）；LC141 快慢指针 Floyd 判环——快 2 步慢 1 步，相遇即环；LC21 dummy 节点 + 拉链式比较，谁小接谁，剩余部分直接 `curr.next = l1 or l2`；LC19 dummy + 快指针先走 N+1 步，让 slow 停在待删节点的前驱，`slow.next = slow.next.next` 删除。**面试口述**：链表题先问「要不要 dummy」——删头节点、需要前驱的场景一律 dummy；「找中点 / 判环 / 倒数第 N 个」都是快慢指针家族，一个套路。**坑：LC206 必须先存 next_temp 再改 `curr.next`，顺序反了指针丢失、链表断裂；LC141 循环条件 `while fast and fast.next` 防 `fast.next.next` 空指针；LC19 走 N+1 步不是 N 步（否则 slow 停在待删节点本身删不掉）；LC21 递归版 O(n+m) 栈，长链表用迭代。**
- [ ] **数组 & 二分查找**：Two Sum（LC1）、Maximum Subarray（LC53）、Find Minimum in Rotated Sorted Array（LC153）、Search in Rotated Sorted Array（LC33） — **核心：LC1 一遍哈希——先查 complement 再存自己，天然防止匹配到同一个元素；LC53 Kadane——`prev_max = max(prev_max + nums[i], nums[i])`（延续前面的子数组 vs 自己重新开始），`ans` 记全局最大；LC153 与右边界比较——`nums[mid] > nums[right]` → 最小值在右半边（`left = mid + 1`），否则 `right = mid`（mid 可能就是最小值），模板 `while left < right`；LC33 任一切口至少一半绝对有序——先判断哪半有序、target 是否在其中，再排除另一半。**面试口述**：二分先分清「找特定值」（`left <= right` + 排除法）还是「找极值/边界」（`left < right` + 保留候选）；旋转数组优先与右边界比较（左边界有二义性）。**坑：LC53 prev_max（当前连续和）与 ans（全局最大）必须两个变量分开维护，混用一个变量会把不相邻的元素加在一起（如 [-2,1,-3,4] 算出 0 而非 4）；LC33 `nums[left] <= nums[mid]` 必须用 `<=`（两元素 [3,1] 时 left==mid）；LC153 `right = mid` 不是 mid-1；LC1 两遍哈希要 `hashmap[complement] != i` 防自匹配（一遍版先查后存无此问题）。**

### 重点坑
- [ ] **LC98 验证 BST 必须检查整个子树**：只比较左右直接子节点会漏掉「右子树的左孩子小于根」这类违规（经典反例 [5,1,4,null,null,3,6]）。**正确**：上下界递归传 (min, max) 开区间，或中序遍历验证严格递增；节点值可能为 0 → 判空用 `is not None`，不用隐式布尔。
- [ ] **LC206 反转链表的指针顺序**：必须「先存 next_temp → 再改 curr.next → 最后整体移动」，三句顺序任何一步反了都会丢指针、链表断裂。**坑**：递归版记得 `head.next = None` 断链，否则产生环。
- [ ] **LC19 快指针先走 N+1 步 + dummy 节点**：走 N 步会让 slow 停在待删节点本身而不是前驱，删不掉；不用 dummy 时删除头节点要特判。**口诀**：「倒数第 N 个」= 快慢指针间距 N，slow 要停在前驱就得 N+1。
- [ ] **旋转数组二分一律与右边界比较**：LC153 只有 `nums[mid] > nums[right]` 才敢 `left = mid + 1`，否则 `right = mid`（mid 可能就是最小值）；LC33 判断有序半区用 `nums[left] <= nums[mid]`（`<=` 处理两元素情况）。**坑**：LC153 是「找极值」模板 `while left < right`，LC33 是「找目标」模板 `while left <= right`，别混。
- [ ] **LC53 Kadane 双变量分离**：`prev_max`（以当前元素结尾的连续和）与 `ans`（全局最大）分开维护；用同一个变量 `ans = max(ans + nums[i], nums[i])` 会把不相邻的元素加在一起。**坑**：`prev_max` 初始化为 `nums[0]`，循环从 `i=1` 开始。

### 建议刷的新题
- [ ] **树**：Subtree of Another Tree（Easy）— 关联已掌握 LC100 Same Tree 递归比较模板。**核心**：对 root 的每个节点调用 isSameTree（节点为空直接 false，命中即 true）；isSameTree 递归「当前值相等 && 左子树相等 && 右子树相等」。**坑**：isSubtree 的 base case 是 `if not root: return False`（空树不是任何非空树的子树）；subRoot 为空应返回 True（空树是任何树的子树）。
- [ ] **树**：Kth Smallest Element in a BST（Medium）— 关联已掌握 LC98 中序遍历递增性质。**核心**：BST 中序 = 升序序列，第 k 个被访问的节点就是答案；递归计数或迭代栈（找到即停，更省）。**坑**：k 递减放在「弹出/访问节点时」而不是「入栈时」；迭代栈模板 `while stack or cur`。
- [ ] **链表**：Reorder List（Medium）— 关联已掌握 LC206 反转链表 + LC141 快慢指针找中点。**核心**：三步走——快慢指针找中点 → 反转后半段 → 交替合并两段。**坑**：反转前先把前半段尾节点的 next 置 null 断开（否则成环）；奇数长度时统一 slow 停在中点的取法；交替合并时先存 next 再改指针防丢。
- [ ] **链表**：Merge K Sorted Lists（Hard）— 关联已掌握 LC21 合并两个有序链表 + 堆。**核心**：小顶堆（优先队列）存 k 个头节点，每次弹出最小节点接入结果，再把该链表的下一个节点入堆，O(N log k)；等价解法是两两分治合并。**坑**：Java PriorityQueue 要写 Comparator；初始入堆时跳过 null 头；堆空说明全部合并完。
- [ ] **数组 / 双指针**：3Sum（Medium）— 关联已掌握 LC1 Two Sum 哈希思想。**核心**：先排序 → 固定第一个数 i → 双指针 left/right 收缩找两数之和 = -nums[i]；排序是为了去重 + 双指针 O(n²)。**坑**：去重有三处——i 跳过重复值、left/right 命中后各自跳过重复值；排序后 `nums[i] > 0` 可提前剪枝；双指针条件 left < right。

## 历史复习记录
- 2026-08-02：树与递归、链表、数组 & 二分查找
- 2026-08-01：图论 BFS/DFS、滑动窗口 & 字符串、动态规划（股票系列）
- 2026-07-30：链表、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-07-29：树与递归、滑动窗口 & 字符串、动态规划（股票系列）
- 2026-07-28：数组 & 二分查找、链表、图论 BFS/DFS
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
**总共 LeetCode 完成：31 道题。掌握基于这些题型的核心思路，可以应对类似面试问题。**

## 待复习（按优先级）

- [x] **树基础** — LC226 + LC105 + LC235 + LC236 + LC102 + LC104 + LC98
- [x] **滑动窗口** — LC3 无重复字符最长子串 + LC76 最小覆盖子串
- [x] **链表基础** — LC206 + LC141 + LC21 + LC19
- [x] **图 DFS/BFS** — LC133 Clone Graph + LC207 Course Schedule + LC200 Number of Islands
- [x] **二分查找** — LC153 旋转数组最小值 + LC33 搜索旋转排序数组
- [x] **数组基础** — LC1 Two Sum + LC121 Best Time to Buy and Sell Stock
