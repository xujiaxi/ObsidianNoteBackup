---
题号: 200
难度: medium
tags: [matrix, graph, dfs, bfs]
状态: 📝 待做
日期: 2026-05-12
---

# 200. Number of Islands

## 题目
二维网格，'1' 是陆地，'0' 是水。统计独立岛屿数（水平/垂直相邻组成一个岛屿）。

## 思路
**核心策略：淹没（Sinking）**
遍历网格，遇到 '1' → count++ → DFS/BFS 把整个岛全部标记为 '0'。

**选择**：求连通分量 → DFS 更简洁；求最短路径 → BFS。

## Java 解法（DFS）

```java
class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;
        int count = 0, rows = grid.length, cols = grid[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int r, int c) {
        // 越界 或 是水 → 返回
        if (r < 0 || c < 0 || r >= grid.length
            || c >= grid[0].length || grid[r][c] == '0') {
            return;
        }
        grid[r][c] = '0';  // 淹没
        dfs(grid, r - 1, c);  // 上
        dfs(grid, r + 1, c);  // 下
        dfs(grid, r, c - 1);  // 左
        dfs(grid, r, c + 1);  // 右
    }
}
```

复杂度：O(M×N) / O(M×N) — 最坏情况全陆地，递归深度 M×N

## 关键点
- **淹没策略**：直接改原数组 `grid[r][c] = '0'`，省 visited 数组
- **base case**：越界 + 是水
- **rows/cols 获取方式**：grid.length / grid[0].length（数组自带属性，有引用就能拿）
- 也可以用 BFS（Queue），但 DFS 代码更短

## 内存模型
| 区域 | 存放内容 |
|------|---------|
| Heap | grid 数组实体（只有一份） |
| Stack | 每个 dfs 调用的栈帧（r, c 坐标 + 返回地址） |
| 风险 | 全陆地时栈深度 = 格子数，可能 StackOverflow |
| 解决 | 大数据换 BFS 或迭代 DFS |
