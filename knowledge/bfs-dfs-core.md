# BFS / DFS 核心要点

> 来源：Blind 75 专题精讲（Number of Islands + Clone Graph + Course Schedule）

## 什么时候用什么

| 场景 | 推荐 | 原因 |
|------|------|------|
| 连通分量计数 | DFS | 代码简洁，递归直观 |
| 最短路径 | BFS | 天然逐层搜索，第一次到达即最短 |
| 拓扑排序 | BFS (Kahn) | 入度表 + Queue，迭代无栈溢出 |
| 环检测 | DFS (三色) 或 BFS (Kahn) | 三色标记发现环 / Kahn 检查入度 |
| 遍历所有路径 | DFS (回溯) | 本质就是 DFS |

## 三大 DFS 场景模板

### 1. 矩阵搜索（Number of Islands）
```java
void dfs(char[][] grid, int r, int c) {
    if (越界 || 是水) return;
    grid[r][c] = '0';  // 淹没
    dfs(grid, r-1, c); // 四个方向
    dfs(grid, r+1, c);
    dfs(grid, r, c-1);
    dfs(grid, r, c+1);
}
```

### 2. 图深拷贝（Clone Graph）
```java
HashMap<Node, Node> visited = new HashMap<>();
Node dfs(Node node) {
    if (visited.containsKey(node)) return visited.get(node);
    Node clone = new Node(node.val, ...);
    visited.put(node, clone);  // 先入表！再递归！
    for (Node neighbor : node.neighbors)
        clone.neighbors.add(dfs(neighbor));
    return clone;
}
```

### 3. 环检测三色标记（Course Schedule）
```java
// int[] visited: 0=未访问 1=访问中 2=已完成
boolean dfs(int curr) {
    if (visited[curr] == 1) return true;  // 发现环
    if (visited[curr] == 2) return false; // 剪枝
    visited[curr] = 1;
    for (int next : neighbors) dfs(next);
    visited[curr] = 2;
    return false;
}
```

## DFS vs BFS 内存对比

| 维度 | DFS (递归) | BFS (迭代) |
|------|-----------|-----------|
| 内存位置 | 系统调用栈 (Stack) | 堆内存队列 (Heap) |
| 主要开销 | 递归深度（函数栈帧） | 队列宽度（每层节点数） |
| 风险 | 大数据 → StackOverflow | 大数据 → OutOfMemory |
| 代码量 | 极简 | 较长，需 Queue + visited |

## 堆 vs 栈（面试必问）

```
Heap (堆): 存放数组/图的数据实体（只有一份）
Stack (栈): 存放函数的"分身"（每个递归调用一个栈帧）

每个栈帧只记录：
  - 当前坐标 / 节点引用
  - 返回地址

结论：撑爆内存的是"函数分身的数量"，不是"数据本身的大小"
```

## Kahn 算法（BFS 拓扑排序）

```java
// 核心：入度数组 + 队列
int[] indegree = new int[n];
Queue<Integer> q = new LinkedList<>();
for (int i = 0; i < n; i++)
    if (indegree[i] == 0) q.offer(i);

while (!q.isEmpty()) {
    int curr = q.poll();
    count++;
    for (int next : adj[curr]) {
        indegree[next]--;
        if (indegree[next] == 0) q.offer(next);
    }
}
return count == n; // 有环则 count < n
```

**不需要 visited 数组**：`indegree[next] == 0` 天然防重。

## 关键设计模式

### 1. 淹没策略（Sinking）
直接改原数组做 visited 标记，省额外空间。
```java
grid[r][c] = '0';
```
⚠️ 面试确认是否允许修改原数据

### 2. 哈希表防环
```java
visited.put(node, cloneNode);  // 先入表！再递归！
```
否则 A→B→A 环 → 无限递归 StackOverflow

### 3. 矩阵 vs 图对比
| 维度 | 矩阵题 | 图题 |
|------|--------|------|
| 邻居定义 | 坐标运算 | node.neighbors |
| 越界风险 | 坐标出界 | 无越界，只有 null |
| 检查条件 | `r < 0 || r >= rows` | `node == null` |

## Java 细节
- `int[]` 默认初始化为 **0**（不是 null）
- 包装类型 `Integer[]` 默认为 **null**
- 面试建议用参数传递（传引用），比全局变量更符合工程实践
