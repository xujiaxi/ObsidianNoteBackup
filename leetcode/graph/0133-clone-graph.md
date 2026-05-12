---
题号: 133
难度: medium
tags: [graph, dfs, bfs, hash-table]
状态: 📝 待做
日期: 2026-05-12
---

# 133. Clone Graph

## 题目
深拷贝一个无向连通图。不能只复制引用，必须创建全新节点并保持连接关系。

## 思路
**核心：HashMap 作为备忘录**
- Key: 原始节点
- Value: 克隆节点
- 作用：防止环导致死循环 + 建立新旧节点映射

**DFS 流程**：
1. 查表：节点已克隆 → 直接返回克隆件
2. 克隆：创建新节点，**先入表**（关键！防止环死循环）
3. 递归：处理所有邻居，把邻居的克隆件加入新节点的 neighbors

## Java 解法

```java
class Solution {
    private HashMap<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;

        // 1. 已克隆过 → 直接返回
        if (visited.containsKey(node)) {
            return visited.get(node);
        }

        // 2. 创建新节点
        Node cloneNode = new Node(node.val, new ArrayList<>());
        visited.put(node, cloneNode);  // 必须在处理邻居前入表！

        // 3. 递归处理所有邻居
        for (Node neighbor : node.neighbors) {
            cloneNode.neighbors.add(cloneGraph(neighbor));
        }

        return cloneNode;
    }
}
```

复杂度：O(N + E) / O(N) — 哈希表存 N 个节点

## 关键点
- **先入表再递归**：交换顺序会导致环时 StackOverflow（A→B→A 永远查不到表）
- **全局 shared HashMap**：所有递归调用共享，不能私有
- **`if (node == null)` 双重作用**：
  1. 处理初始输入 `cloneGraph(null)` → 防 NPE
  2. 递归中 neighbor 列表含 null → 安全返回
- **矩阵 vs 图对比**：
  - 矩阵：邻居靠坐标计算，需检查越界
  - 图：邻居在 List 中，只有 null 风险，没有越界

## 思考题
为什么 HashMap 必须在处理邻居之前 put？
（A→B, B→A：如果先递归再存表，A 调 B，B 调 A，A 还没进表 → 无限递归）
