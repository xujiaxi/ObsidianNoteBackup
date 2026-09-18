# Union-Find（并查集）模板与要点

> 用途：维护一组不相交集合，支持「合并两个集合」和「查询两点是否同集合」
> 关联题：LC 323（面经 6）、LC 547、LC 200（变体解法）、LC 305（动态加岛）、LC 1631（面经 8/22 的并查集解法）、Kruskal 最小生成树
> 数据来源：2026-09-18 本机实测（20 组随机对拍 + 300×300 性能对比 + 各题示例）

## 1. 它解决什么问题

一句话：**图上的边是逐渐加进来的，随时要回答"这两个点连通吗"或"现在有几个连通块"**。

| 场景 | 该用谁 |
|------|--------|
| 图一次建好，之后只遍历/查询 | DFS / BFS，O(V+E) |
| 边逐渐加入，边加边问连通性 | **Union-Find** |
| 要找具体路径或最短路径 | BFS / Dijkstra（Union-Find 做不到） |
| 判断无向图有没有环 | Union-Find（`union` 返回 false 即有环） |

## 2. 数据结构长什么样

每个元素一个父指针 `parent[i]`：

- `parent[i] == i` → i 是它所在集合的**根**（代表元）
- 每个集合是一棵**树**，根就是集合的代表

```
初始：每个元素自成一棵树
  parent = [0, 1, 2, 3, 4]       n = 5 个独立集合，count = 5

union(0,1)、union(1,2)：        union(3,4)：
        0                              3
        |                              |
        1                              4
        |
        2
  count = 2（{0,1,2}、{3,4}）
```

## 3. 两个操作

```
find(x)    : 沿 parent 向上走到根，返回根
union(a,b) : 先 find 各自的根，把其中一棵树挂到另一棵下面
```

朴素实现的问题：union 时随便挂 → 树可能退化成一条长链 → find 变成 O(n)。
所以需要下面的两个优化，这是面试必问点。

## 4. 两个优化（面试必答）

### 4.1 路径压缩（Path Compression）

`find` 的时候顺手把路径上所有节点直接挂到根上，树瞬间变扁平：

```
find(4) 之前:                之后:
  1                            1
   \                          /|\
    2          ──►           2 3 4
     \
      3
       \
        4
```

作用：把后续 find 的成本压到接近 O(1)，摊销 O(log n)。

### 4.2 按大小合并（Union by Size）

union 时**把小树挂到大树下面**，保证树高不暴涨。只做这一个也是 O(log n)。

### 4.3 两个一起用 → O(α(n))

α 是**反阿克曼函数**，增长极慢：n < 10^600 时 α(n) ≤ 4。

> 面试标准答案：路径压缩 + 按大小合并 → find/union 摊销 **O(α(n))，可视作常数**。

## 5. 模板（Python）

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # 每个元素自成一个集合
        self.size = [1] * n
        self.count = n                 # 连通分量个数（很多题的答案就是它）

    def find(self, x):
        """带路径压缩（迭代版，不怕深链）"""
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[x] != root:          # 把路径上所有节点直接挂到根
            self.parent[x], x = root, self.parent[x]
        return root

    def find_recursive(self, x):
        """递归版更短，但深链会爆栈（Python 默认 limit 1000）"""
        if self.parent[x] != x:
            self.parent[x] = self.find_recursive(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                       # 已连通 → 这条边构成环
        if self.size[ra] < self.size[rb]:      # 小树挂到大树下
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

## 6. 复杂度

| 实现 | find / union | 说明 |
|------|--------------|------|
| 朴素 | O(n) | 链状退化 |
| 仅路径压缩 | 摊销 O(log n) | |
| 仅按大小合并 | O(log n) | |
| **两者都有（标准写法）** | **摊销 O(α(n)) ≈ O(1)** | |
| 空间 | O(n) | parent + size |

## 7. 坑清单

- 忘记 `parent = list(range(n))` 初始化，直接用 `[0]*n` → 全部指向 0
- **union 的是根，不是元素**：必须先 `find`，不能 `parent[a] = b`
- `count` 语义搞错：只有"成功合并"（两个根不同）时才 `count -= 1`
- 节点编号 1-based（如城市 1~n）→ 开 `n + 1` 的数组
- 路径压缩的递归版在深链上爆栈 → 用迭代版
- 网格题里忘了把坐标压成一维（`id = r * C + c`），或忘了减掉水分量
- 问"两点是否连通"时不要写 `parent[a] == parent[b]`（那只是父节点相同，不是根相同）

## 8. 面试口述模板

> 并查集用来维护动态连通性。每个元素有一个父指针，每个集合是一棵树，根是代表元；find 沿父指针找根，union 把两个根接起来。为了性能我做两个优化：find 时路径压缩把路径上的点直接挂到根上，union 时按大小合并把小树挂到大树下面，两者叠加后单次操作摊销 O(α(n))，可视作常数。空间 O(n)。它适合"边逐渐加入 + 频繁问连通性"的场景，但做不到求路径，也不支持删除。

## 9. 进阶（面试加分）

- **可撤销并查集**：去掉路径压缩，只保留按大小合并，用栈记录每次 union 以便回滚（处理"删边/回溯"类问题）
- **带权并查集**：parent 旁边再维护"到根的距离/异或值"，解 LC 399（除法求值）、LC 990（等式方程可满足性）
- **不支持删除/分裂**：父指针是单向的，拆不开；要支持删除得换 Euler Tour Tree 之类
- **LC 305 Number of Islands II**：UF 的经典场景——陆地一个个加上来，每次问岛屿数。DFS 版本每次都要重跑，UF 只需 union 一次

## 10. 实测数据（2026-09-18，本机 CPython 3.13.5）

结果正确性：LC 323 / 547 / 200 的 UF 解与 DFS 解在 20 组随机网格上结果全部一致。

性能对比（300×300 全陆地网格，求岛屿数）：

| 解法 | 耗时 | 结果 |
|------|------|------|
| Union-Find | 0.786s | 1 |
| 迭代 DFS | 0.224s | 1 |

**结论：网格连通块类题目（LC 200 / 934）首选 DFS/BFS，Union-Find 在网格上要 union 4·m·n 次，慢 3 倍以上。** Union-Find 的优势在"稀疏图 + 动态加边"，不是在密集网格上刷性能。
