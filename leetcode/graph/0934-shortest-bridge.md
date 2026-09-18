---
题号: 934
难度: medium
tags: [graph, matrix, dfs, bfs, queue, multi-source-bfs]
状态: ✅ 已做
日期: 2026-09-18
---

# 934. Shortest Bridge

> 面经出处：整份面经出现 **6 次**（面经 5、13、14、15、16、17），是全列表最高频的题。
> 计划位置：`plans/two-week-plan-2026-09-18.md` Day 1。

## 题目
网格里有两个由 1 组成的岛，求连接两岛需要翻转的最少 0 的个数（即两岛之间的最短"桥"长度）。

## 思路

两步走，前半段是 LC 200，后半段是多源 BFS：

1. **标岛**：遍历网格找到第一个 1，用 DFS 洪水填充把整个岛原地标记为 2，**同时把这个岛的所有格子塞进队列**——它们是多源 BFS 的初始层（steps = 0 的那一层）。
2. **多源 BFS 扩水**：从队列整体向外逐层扩展。遇到 0 就标记成 2 并入队；遇到 1 说明触达第二个岛，立刻返回当前 steps。

**为什么是多源 BFS**：要找的是两岛之间最近的一对格子。把岛 1 的每个格子都当作源点同时扩散，第 d 轮覆盖的格子的"到最近源点距离 = d"，所以第一次触达岛 2 的轮数就是 `min over 源点 dist(源点, 岛2)`，即全局最短。

## 面试最终版（Python，迭代 DFS 防爆栈）

```python
from collections import deque

class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        # 1) 迭代 DFS 标出第一个岛，岛格子同时作为多源 BFS 的初始层
        queue = deque()
        found = False
        for i in range(n):
            if found:
                break
            for j in range(m):
                if grid[i][j] != 1:
                    continue
                stack = [(i, j)]
                grid[i][j] = 2                      # 进栈即标记，避免重复入栈
                while stack:
                    x, y = stack.pop()
                    queue.append((x, y))
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if in_bounds(nx, ny) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            stack.append((nx, ny))
                found = True
                break

        # 2) 多源 BFS：steps = 需要翻转的 0 的个数
        steps = 0
        while queue:
            for _ in range(len(queue)):             # 只处理当前这一层
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if not in_bounds(nx, ny) or grid[nx][ny] == 2:
                        continue
                    if grid[nx][ny] == 1:           # 触达第二个岛
                        return steps
                    grid[nx][ny] = 2                # 遇水：标记后入队
                    queue.append((nx, ny))
            steps += 1
        return -1
```

复杂度：时间 O(n·m)，空间 O(n·m)（队列 + 栈）。

## 第一版实现的问题（当天实际踩的）

| # | 问题 | 后果 | 修正 |
|---|---|---|---|
| 1 | `while counter > -1` 是永真条件 | 循环只能靠"题目保证有两个岛"退出；单岛输入会死循环 | 改 `while queue`，靠数据结构自然终止 |
| 2 | 递归 DFS 标岛 | Python 默认递归上限 1000，而 n ≤ 100 → 岛最大 10000 格，**RecursionError** | 换迭代 DFS（显式栈）或 `sys.setrecursionlimit` |
| 3 | dfs/bfs 各手写 4 个方向的 if（共 8 段） | 面试紧张时极易把 i-1 写成 i+1 | `dirs` 元组 + `in_bounds()` helper |
| 4 | `bfs(queue)` 内 `queue = newqueue` 遮蔽参数 | 分层读起来绕 | `for _ in range(len(queue))` 原地分层，省掉 newqueue |
| 5 | 找到第一个岛后写了两个 break | 第二个 break 永远执行不到，外层循环继续跑 | 直接 `return bfs()` 或 `found` 标志位 |
| 6 | 变量名 `counter` | 语义不明（其实是"已穿过的海水层数"） | 改名 `steps` |

## 关键点（面试要主动说出来的）

- **steps 计数的正确性（不变量）**：每一轮 BFS 开始时，队列里装的是"与岛 1 距离恰好等于 steps 的格子"（steps=0 是岛本身）。所以队列中格子的邻居若是岛 2，岛 2 与岛 1 的距离 = steps + 1，而"距离 = k"意味着中间夹了 k−1 个 0 —— **需要翻转 steps 个格子**，所以 `return steps` 而不是 `steps + 1`。
- **手跑验证用例**：`[1,0,1]` → 第一轮把中间的 0 标记入队、steps 变 1；第二轮从 0 看到右边的 1，返回 1。答案就是 1。
- **分层模板**：`for _ in range(len(queue))` —— 循环里新 append 的节点不会被本轮吃到，天然分层。这个模板后面 1091、994、1631 都能直接套。
- **原地标记省 visited 数组**：岛 1 和扩过的水都标成 2；第二个岛保持 1 不变，这样"遇到 1"就是触达信号。
- **网格题 Python 递归红线（2026-09-18 本地实测，CPython 3.13.5，默认 limit=1000）**：

  | 输入形态 | 实测最大递归深度 | 结果 |
  |---|---|---|
  | n×n 全 1 实心方块 | **正好 n²**（n=10→100，n=30→900） | n ≥ 32（1024）就 RecursionError |
  | 100×100 随机网格，密度 0.3 | 16 | 通过 |
  | 100×100 随机网格，密度 0.5 | 85 | 通过 |
  | 100×100 随机网格，密度 0.7 / 0.9 | > 998 | **RecursionError** |

  结论：栈深度由**最大连通块的蛇形路径长度**决定，不是网格尺寸。实心块是纯蛇形路径，所以深度 = 格数 = n²；稀疏网格被水切断，深度很小。所以"递归能 AC"往往只是用例不够极端。

  **平台差异（关键）**：LeetCode 判题环境的 `sys.getrecursionlimit()` 实测为 **550000**（2026-09-18 用户确认），不是默认的 1000。所以这题的递归解在 LeetCode 上永远不会爆栈，但换到 HackerRank / CoderPad（默认 1000）同样的代码会直接 `RecursionError`。面试时主动写迭代 DFS 或主动说明这个风险。

## 追问预演

1. **为什么用 BFS 不用 Dijkstra？** 所有边长相等（每步代价 1），BFS 就是退化情形下的最短路，O(n·m) 且不需要堆。对比面经 22 那道"边权不同、每条路径取最大边"的必须上 Dijkstra。
2. **递归 DFS 会不会爆栈？** 会 —— n 最大 100 → 单岛可达 10000 格 > Python 默认 1000 上限。所以用显式栈的迭代 DFS。
3. **改成 8 方向移动 / 要求输出具体翻转哪些格子？** 8 方向只改 `dirs`；要输出坐标就记 parent 指针回溯，或 BFS 时存"入队来源"。
4. **如果有 k 个岛求最近的一对？** 多源 BFS 跑 k 次，或先用并查集分组再两两 BFS。

## 60 秒口述模板

> 网格类最短路问题，两步。先用 DFS 洪水填充把第一个岛原地标记成 2，并把这个岛的所有格子塞进队列作为初始层；然后从这个岛做多源 BFS 逐层向外扩水，每扩一层 steps 加一，一旦邻居是第二个岛的 1 就返回当前 steps——因为距离 = steps+1，中间夹了 steps 个 0 格。时间 O(nm)，空间 O(nm) 给队列。标岛我用迭代 DFS 而不是递归，因为 n ≤ 100 时单岛可达 10000 格，Python 默认递归上限 1000 会爆栈。
