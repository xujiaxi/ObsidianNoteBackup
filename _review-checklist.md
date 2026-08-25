# 🎯 面试复习清单

## 📅 今日复习（2026-08-24）

### 需要回顾
- [ ] **图论 BFS/DFS**：Clone Graph（LC133）、Course Schedule（LC207）、Number of Islands（LC200） — **核心：LC200 沉岛算法——访问过的陆地直接改成 '0' 避免重复计数，四方向 DFS；LC207 环检测用三色标记法（0 未访问 / 1 访问中 / 2 已完成），或 Kahn 拓扑排序——入度数组 + deque，出队 count == n 才无环；LC133 克隆图用 HashMap 存「原节点 → 克隆节点」，先入表再递归。**面试口述：先确认场景——连通分量计数用 DFS、最短路径/层序用 BFS、拓扑排序用 Kahn；BFS 队列必须用 deque（list.pop(0) 是 O(N)）。**坑：LC200 忘记沉岛会死循环/重复计数；LC207 只用 visited 布尔无法区分「访问中」与「已完成」，会漏判环；LC133 不先入表，A→B→A 环会无限递归 StackOverflow；深树/大图递归注意 Stack vs Heap——递归栈可能溢出，改迭代。**
- [ ] **链表**：Reverse Linked List（LC206）、Linked List Cycle（LC141）、Merge Two Sorted Lists（LC21）、Remove Nth Node From End（LC19） — **核心：三大铁律——① 改 curr.next 前先存 next（断链预警）；② 用 .next.next 前保证 fast 和 fast.next 非空；③ dummy 哨兵节点简化头节点增减。LC206 三指针 prev/curr/next 反转；LC141 快慢指针（2 步 vs 1 步）判环；LC19 快指针先走 n 步再同步移动，配合 dummy 删头节点。**面试口述：动头节点就先上 dummy；找中点/环/倒数第 N 个用快慢指针。**坑：LC206 不先存 next 直接断链；LC141 循环条件 `while fast and fast.next` 顺序不能反，否则空指针；LC21 合并完要接上剩余链表；LC19 单指针遍历无法知道倒数位置。**
- [ ] **树与递归**：Max Depth（LC104）、Same Tree（LC100）、Invert（LC226）、Level Order（LC102）、Construct from Pre+In（LC105）、Validate BST（LC98）、LCA of BST/BT（LC235/236） — **核心：递归三要素——base case（空节点返回 None/0/True）、递归逻辑（左右子树）、返回值向上汇总；LC104 后序 max(left, right)+1；LC226 交换左右子树；LC102 层序 BFS 每层先固定 len(q) 再出队；LC105 前序第一个是根，中序定位根再切左右子树（HashMap 存中序索引）；LC98 递归传 (min, max) 边界，或中序遍历必须严格升序；LC235 利用 BST 大小关系指路，LC236 后序汇总左右子树结果。**面试口述：先讲 base case 和返回值；BST 题优先想中序遍历升序性质。**坑：LC98 只比较直接子节点会漏判「右子树里的左子树」；LC105 中序索引偏移易算错（左子树长度 = 根索引 − inLeft）；LC102 不固定 len(q) 会把下一层混进来；深树递归栈溢出，可改迭代栈。**

### 重点坑
- [ ] **图论**：LC200 沉岛必须「访问即标记」，忘了会死循环/重复计数；LC207 三色标记（0/1/2）不能省——visited 布尔分不清「访问中」和「已完成」，会漏判环；LC133 先入 HashMap 再递归，否则环导致无限递归；BFS 队列用 deque，list.pop(0) 退化成 O(N²)。
- [ ] **链表**：LC206 改指针前必须先存 next_temp，顺序反了丢失后续链表；LC141 循环条件 `while fast and fast.next`（先 fast 再 fast.next）；LC19 删除头节点必须 dummy；LC21 收尾记得接剩余链表。
- [ ] **树与递归**：LC98 必须传 (min, max) 区间，只比直接子节点会漏判；LC105 中序索引偏移（左子树长度 = 根位置 − inLeft）；LC102 每层先固定 queue 大小；Python 类变量陷阱——self.prev 必须在方法内初始化；深度递归可能 StackOverflowError（Stack vs Heap 内存模型）。

### 建议刷的新题
- [ ] **树**：Binary Tree Maximum Path Sum（LC124，Hard）— 关联已掌握知识点：LC104 后序递归汇总、LC236 LCA（已完成）。**核心**：后序遍历，每层返回「单边最大路径和」= max(left, right) + val，全局变量 ans 更新「经过当前节点的最大路径」= left + right + val。**坑**：负值分支直接丢弃（取 max(0, ...)）；ans 初始化为负无穷而非 0。
- [ ] **图 / 哈希**：Longest Consecutive Sequence（LC128，Medium）— 关联已掌握知识点：LC200 沉岛「标记已访问」思想（已完成）。**核心**：全部元素入 HashSet，只从「序列起点」（num-1 不在集合中）开始向后数，均摊 O(N)。**坑**：不判断起点每个数都数一遍会退化为 O(N²)。
- [ ] **矩阵 / 回溯**：Word Search（LC79，Medium）— 关联已掌握知识点：LC200 四方向 DFS（已完成）。**核心**：每个格子作起点 DFS 匹配单词，访问过的格子标记后必须回溯恢复（原地改字符或 visited 数组）。**坑**：回溯不恢复现场会影响后续分支；先判断越界再访问。
- [ ] **链表**：Reorder List（LC143，Medium）— 关联已掌握知识点：LC206 反转 + LC141 快慢指针（已完成）。**核心**：快慢指针找中点 → 反转后半段 → 交替合并两个链表。**坑**：找中点注意奇偶长度；合并时先存 next 再改指向，防止断链。
- [ ] **树 / 序列化**：Serialize and Deserialize Binary Tree（LC297，Hard）— 关联已掌握知识点：LC102 层序 BFS + LC105 前序重建（已完成）。**核心**：序列化用层序/前序 + 空节点占位（如 "null"），反序列化按同序重建；字符串解析用队列/索引。**坑**：空节点必须显式编码否则无法重建树形；注意负数节点值的解析。

## 历史复习记录
- 2026-08-24：图论 BFS/DFS、链表、树与递归
- 2026-08-23：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-22：图论 BFS/DFS、链表、树与递归
- 2026-08-21：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-20：图论 BFS/DFS、链表、树与递归
- 2026-08-19：滑动窗口 & 字符串、动态规划（股票系列）、间隔 / 设计题（堆）
- 2026-08-18：图论 BFS/DFS、链表、树与递归
- 2026-08-17：滑动窗口 & 字符串、动态规划（股票系列）、数组 & 二分查找
- 2026-08-16：图论 BFS/DFS、链表、树与递归
- 2026-08-15：动态规划（股票系列）、间隔 / 设计题（堆）、数组 & 二分查找
- 2026-08-14：链表、树与递归、滑动窗口 & 字符串
- 2026-08-13：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-12：动态规划（股票系列）、链表、树与递归
- 2026-08-11：数组 & 二分查找、图论 BFS/DFS、滑动窗口 & 字符串
- 2026-08-10：链表、树与递归、间隔 / 设计题（堆）
- 2026-08-09：图论 BFS/DFS、数组 & 二分查找、动态规划（股票系列）
- 2026-08-08：链表、树与递归、滑动窗口 & 字符串
- 2026-08-07：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-06：滑动窗口 & 字符串、动态规划（股票系列）、树与递归
- 2026-08-05：间隔 / 设计题（堆）、数组 & 二分查找、图论 BFS/DFS
- 2026-08-04：动态规划（股票系列）、树与递归、链表
- 2026-08-03：图论 BFS/DFS、间隔 / 设计题（堆）、滑动窗口 & 字符串
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
