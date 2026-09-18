---
题号: 323
难度: medium
tags: [graph, union-find, dfs, connected-components]
状态: ✅ 已做
日期: 2026-09-18
---

# 323. Number of Connected Components in an Undirected Graph

> 面经出处：面经 6「find connected components in the graph」。
> ⚠️ 这题在 LeetCode 上是 **Premium 会员题**，免费替代是 **LC 547 Number of Provinces**（同样求连通分量数，输入换成 n×n 邻接矩阵），两个代码本文都给了。
> 计划位置：`plans/two-week-plan-2026-09-18.md` Day 1。并查集模板见 `knowledge/union-find-template.md`。

## 题目
给定 n 个节点（编号 0 ~ n-1）和一组无向边，求连通分量个数。

## 思路

### Union-Find 版（首选）

1. 初始化：每个节点自成一个集合，`count = n`
2. 遍历每条边，`union(u, v)`
3. 每次**成功合并**（两个根不同）才 `count -= 1`
4. 返回 `count`

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:            # 路径压缩
            self.parent[x], x = root, self.parent[x]
        return root

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                          # 已连通，边成环
        if self.size[ra] < self.size[rb]:         # 按大小合并
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return uf.count
```

### DFS 版（对照）

```python
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        seen = [False] * n
        count = 0
        for i in range(n):
            if seen[i]:
                continue
            count += 1
            stack = [i]
            seen[i] = True                      # 入栈即标记
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if not seen[w]:
                        seen[w] = True
                        stack.append(w)
        return count
```

### LC 547 替代版（邻接矩阵输入）

```python
class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):        # 只走上三角，避免重复 union
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count
```

## 复杂度

| 解法 | 时间 | 空间 |
|------|------|------|
| Union-Find | O(n + E·α(n))，α(n) 可视作常数 | O(n)（parent + size） |
| DFS | O(n + E) | O(n + E)（邻接表） |

## 关键点与选择

- **什么时候用 UF 而不是 DFS**：动态加边场景（LC 305 Number of Islands II）、只需知道"是否连通"不需要遍历邻居、要顺便判环。静态一次性图两者都行。
- 每条边只 union 一次，**不需要建邻接表**——这是 UF 的代码量优势（但 UF 类模板本身有 20 行）。
- **检测环的用法**：`union` 返回 False 说明两个端点已连通，这条边构成环。LC 261 Graph Valid Tree 就是"边数 = n-1 且没有环"。
- 编号如果从 1 开始（如 LC 261 用的是 0-based，但很多题是 1~n），数组开 `n + 1`。

## 坑清单

- `count` 只在成功合并时减 1（写成每条边都减就错了）
- union 的是**根**不是元素（必须先 find）
- 547 的邻接矩阵是**对称的**，只走 `j > i` 可以省一半操作
- DFS 版入栈时就要标记 seen，否则同一节点会重复入栈

## 追问预演

1. **复杂度为什么是 α(n)**？路径压缩让树扁平化，按大小合并控制树高，两者叠加后单次操作的摊销成本是反阿克曼函数，n < 10^600 时不超过 4。
2. **能不能求"最大连通块的大小"**？可以，`size[find(x)]` 就是所在分量的大小。
3. **如果边会动态删除呢**？Union-Find 不支持删除（父指针单向），要么重建，要么用可撤销并查集。
4. **和 DFS 性能对比**？稀疏图上同一量级但 UF 常数更小；密集网格（LC 200 那种）UF 反而慢 3 倍（实测数据见 `knowledge/union-find-template.md` 第 10 节）。

## 60 秒口述模板

> 求连通分量个数，两种解法。并查集：初始化 n 个独立集合、计数器 count = n，遍历边做 union，每次成功合并 count 减一，最后返回 count；find 带路径压缩、union 按大小合并，单次摊销 O(α(n)) 近似常数，总时间 O(n + E·α(n))，空间 O(n)。DFS 版则是建邻接表 + 一次遍历数连通块，O(n+E)。如果边是动态加进来的（比如岛屿一个个出现），只有并查集能做到增量更新。
