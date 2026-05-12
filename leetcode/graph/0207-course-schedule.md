---
题号: 207
难度: medium
tags: [graph, dfs, bfs, topological-sort]
状态: 📝 待做
日期: 2026-05-12
---

# 207. Course Schedule

## 题目
给定 numCourses 门课（0 到 numCourses-1）和先修关系 prerequisites[i] = [a, b]（b → a，先修 b 才能修 a）。判断是否能修完所有课（即图中有无环）。

## 思路

### DFS 三色标记法（环检测）

**三种状态**：
- `0`（未访问）：Java int[] 默认初始值，还没看过
- `1`（正在访问）：当前 DFS 路径上，**再次碰到 = 有环**
- `2`（已完成）：该节点及所有后继已确认无环，**再次碰到 = 剪枝**

**为什么需要状态 2？**
只用 0 和 1 也能检测环，但状态 2 用来**剪枝**。如果从 A → B → C 已经确认无环，后来 D → B 再次遇到 B 时，看到状态 2 直接跳过，不用重复遍历。

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // 1. 建邻接表
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        for (int[] pre : prerequisites) {
            adj.get(pre[1]).add(pre[0]); // pre[1] -> pre[0]
        }

        // 2. 三色状态数组
        int[] visited = new int[numCourses]; // 0:未访问 1:访问中 2:已完成

        // 3. 对每门课做 DFS
        for (int i = 0; i < numCourses; i++) {
            if (hasCycle(i, adj, visited)) return false;
        }
        return true;
    }

    private boolean hasCycle(int curr, List<List<Integer>> adj, int[] visited) {
        if (visited[curr] == 1) return true;  // 碰到正在访问的 = 环
        if (visited[curr] == 2) return false; // 已确认无环 = 剪枝

        visited[curr] = 1; // 标记为访问中

        for (int next : adj.get(curr)) {
            if (hasCycle(next, adj, visited)) return true;
        }

        visited[curr] = 2; // 标记为已完成
        return false;
    }
}
```

复杂度：O(N + E) / O(N)

### BFS Kahn 算法（拓扑排序）

**核心概念：入度（In-degree）**—— 指向该节点的边数

**算法流程**：
1. 建邻接表 + 统计入度
2. 所有入度为 0 的节点入队（"入门课"）
3. 出队 → 计数 +1 → 所有后继入度 -1 → 入度为 0 的入队
4. 最后 processedCourses == numCourses → 无环

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());

        for (int[] pre : prerequisites) {
            int course = pre[0], preCourse = pre[1];
            adj.get(preCourse).add(course);
            indegree[course]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) queue.offer(i);
        }

        int count = 0;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            count++;
            for (int next : adj.get(curr)) {
                indegree[next]--;
                if (indegree[next] == 0) queue.offer(next);
            }
        }
        return count == numCourses;
    }
}
```

复杂度：O(N + E) / O(N + E)

## 关键点

| 方法 | 环检测方式 | 优势 |
|------|-----------|------|
| DFS 三色 | 撞见状态 1 | 代码简洁，逻辑直观 |
| BFS Kahn | 入度永远到不了 0 | 迭代无栈溢出风险 |

- **int[] 默认初始化为 0，不是 null**
- **Kahn 不需要 visited 数组**——入度降为 0 才入队，天然防重
- 如果要求输出修课顺序（Course Schedule II），直接把 poll() 的顺序记录下来
