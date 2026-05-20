# 🎯 面试复习清单

## 📅 今日复习（2026-05-19）

### 需要回顾
- [ ] **图 — DFS/BFS 遍历与拓扑排序**：LC133 克隆图（HashMap 深拷贝，**先入表再递归**防环，否则 A→B→A 无限递归 StackOverflow）、LC200 岛屿数量（沉岛算法 `grid[r][c] = '0'` 直接改原数组省 visited、DFS 递归四方向遍历，注意越界检查）、LC207 课程表（DFS 三色标记法环检测：0=未访问→1=访问中→2=已完成，撞见状态 1 则为环；BFS Kahn 算法：入度数组 + 队列，入度为 0 入队，poll 后后继入度减 1，最终 count == numCourses 则无环）— **三色标记 + Kahn 入度是图面试两大核心模板，务必熟记**
- [ ] **滑动窗口 — 找最长 vs 找最短模板**：LC3 无重复最长子串（`int[128]` 计数，r 扩张遇到重复时 l 收缩 while，`right - left + 1` 更新 max，**常见错误**：先 `l++` 再 `remove` 导致删除错误字符）、LC76 最小覆盖子串（`need[]` + `window[]` 双数组 + `valid` 计数器，窗口满足条件 (`valid == totalNeeded`) 时 l 试探收缩更新 minLen，**关键**：`valid` 在 `window[c] == need[c]` 瞬间 +1，避免 O(K) 全量遍历；`var` 用自动拆箱注意 Integer `==` 陷阱）— **LC3 非法收缩 vs LC76 合法收缩，两个模板方向相反，面试混用必挂**

### 重点坑
- [ ] **Kahn 入度更新遗漏** — LC207 Course Schedule BFS：出队节点后必须遍历其**全部邻接节点**逐一减入度，`adj.get(curr).forEach(next -> indegree[next]--)`，漏掉一个邻居就导致入度永远降不到 0，count 永远到不了 numCourses。和 LC200 的沉岛不同，沉岛只淹当前格子无需遍历邻居列表
- [ ] **Clone Graph 的先入表再递归顺序** — LC133：`visited.put(node, cloneNode)` 必须在 `for (neighbor)` 递归之前执行。Tree 的克隆（先递归子树再创建节点 + 赋值）和图恰恰相反。**口诀：树是后序 → 先孩子再自己；图是先入表 → 先自己再孩子，防环**
- [ ] **滑动窗口收缩方向混淆** — LC3（找最长无重复）：`while (count[rChar] > 1)` 窗口**非法时收缩**，合法时记录结果。LC76（找最短覆盖）：`while (valid == totalNeeded)` 窗口**合法时收缩**，非法时扩张。方向搞反 → 结果全错。找最长：非法收缩；找最短：合法收缩

### 建议刷的新题
- [ ] **图/DFS**：Pacific Atlantic Water Flow（Medium）— 从太平洋和大西洋边界分别逆向 DFS 向中间推进，标记各自能到达的格子，交集即为答案；关联已掌握的 LC200 沉岛算法的坐标遍历（四方向递归）+ DFS 框架，同一套「从边界出发逆向遍历」思路是高频变体
- [ ] **滑动窗口**：Longest Repeating Character Replacement（Medium）— 窗口内 `maxFreq` 统计 + 收缩条件 `windowLen - maxFreq > k`（超过 k 次替换允许时收缩）；关联已掌握的 LC3 int[128] 计数 + LC76 valid 计数器，三道题覆盖滑动窗口**全部**模板（去重、覆盖、替换），面经中 90% 变体出自这三题
- [ ] **链表综合**：Reorder List（Medium）— 三步走：快慢指针找中点 → 反转后半段 → 交替合并；一题检验三项基本功，关联已掌握的 LC206 反转、LC141 快慢指针、LC21 合并链表，面试中频
- [ ] **数组/贪心**：Best Time to Buy and Sell Stock（Easy）— 一次遍历更新 `minPrice` 和 `maxProfit`，O(n) 扫描单变量维护；关联已掌握的滑动窗口扫描模式 + LC76 的「移动过程中维护状态」思想，Array 专题最佳进阶起点
- [ ] **数组/DP 入门**：House Robber（Medium）— 一维 DP：`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`，空间可优化到 O(1) 滚动数组；关联已掌握的 Tree 分治递归（LC104 `max(left, right) + 1` 结构与 `max(取, 不取)` 一致），DP 专题最佳突破口，从递归到 DP 的自然过渡

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
