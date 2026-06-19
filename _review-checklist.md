# 🎯 面试复习清单

## 📅 今日复习（2026-06-18）

### 需要回顾
- [ ] **树**：最大深度（LC104）、翻转二叉树（LC226）、层序遍历（LC102）、从前序中序构造二叉树（LC105）、LCA of BST（LC235）、LCA of BT（LC236） — **核心：递归 base case 处理 null 节点；分清递归返回值含义（是子树结果还是布尔）。层序遍历用队列 BFS 逐层；LCA 在 BST 利用左小右大性质，在一般 BT 用递归找左右侧是否包含目标后剪枝。**
- [ ] **链表综合**：反转链表（LC206）、合并两个有序链表（LC21）、环形链表（LC141）、删除倒数第 N 个（LC19） — **核心：反转要保存 next 防断链；合并用 dummy 哨兵简化头处理；环检测用快慢指针（Floyd），相遇后再用慢指针从 head 出发找入口。**
- [ ] **Intervals / 区间**：会议室 II（LC253） — **核心：最小堆维护结束时间，按开始时间排序后遍历，若当前会议开始时间 ≥ 堆顶结束时间则复用会议室，否则新开一间，转化为求最大重叠区间数。**

### 重点坑
- **链表操作中指针丢失** — 反转链表时忘记保存 next 指针或断链导致无法继续遍历；合并链表时某个链表已经为空还继续取 next（NullPointerException）。写之前先在纸上画一遍指针移动。
- **快慢指针初始化不一致** — Floyd 判环时快指针从 head 开始、慢指针从 head 开始，每次快指针走两步；但找中间点时根据题意快指针可以从 head 或 head.next 开始，导致中点偏左或偏右。写之前先确定要找的是“第一个中点”还是“第二个中点”。
- **树递归剪枝时机** — LCA 类题目中如果两侧都返回 null 说明当前子树不含目标，但如果某一侧返回 null 而另一侧返回非 null，应该直接返回非 null 的一侧（向上传递），不要 incorrectly 返回 null。理解“自底向上传递信息”和“自顶向下传递约束”的区别。
- **区间重叠边界判断** — `interval1.end >= interval2.start` 才是重叠，易把等号漏掉或方向搞反。合并/插入区间时先按 start 排序，处理完一个再处理下一个，不要跳跃。

### 建议刷的新题
- [ ] **树**：Same Tree（Easy） — 关联已掌握树递归思维，**递归比较根值 + 左右子树是否同时相等。base case 处理两个都 null 返回 true，一个 null 一个非 null 返回 false。**
- [ ] **链表**：Reorder List（Medium） — 关联已掌握的链表操作（反转 + 合并 + 快慢指针），**三步：快慢指针找中点（剪断） → 反转后半部分 → 交错合并两个链表**。注意翻转时不要形成环。
- [ ] **数组/双指针**：3Sum（Medium） — 关联已掌握的排序 + 双指针思想，**排序后固定一个数，剩余部分用双指针找两数之和等于 -num[i]。注意去重（固定值、左指针、右指针重复时都要跳过），返回的是值不是索引。**
- [ ] **树/递归**：Validate Binary Search Tree（Medium） — 关联已掌握的树遍历思维，**中序遍历验证单调递增（或递归维护每个节点的上下界）。不能用单一节点的孩子大小判断，必须考虑祖先节点的约束。**

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
