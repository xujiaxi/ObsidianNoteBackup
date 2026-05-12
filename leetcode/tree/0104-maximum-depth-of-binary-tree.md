---
题号: 104
难度: easy
tags: [tree, dfs, bfs]
状态: ✅ 已做
日期: 2026-05-12
---

# 104. Maximum Depth of Binary Tree

## 题目
求二叉树的最大深度（根节点到最远叶节点的节点数）。

## 思路

### 解法 1：DFS 递归（自底向上）

当前深度 = 1 + max(左子树深度, 右子树深度)。

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
```

复杂度：O(n) / O(h)

### 解法 2：BFS（按层数）

最大深度 = 树有多少层。

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    q = deque([root])
    depth = 0
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return depth
```

复杂度：O(n) / O(w) — w 为最大宽度

### 解法 3：迭代 DFS（手动栈）

```python
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    stack = [(root, 1)]
    max_d = 0
    while stack:
        node, d = stack.pop()
        max_d = max(max_d, d)
        if node.right: stack.append((node.right, d + 1))
        if node.left: stack.append((node.left, d + 1))
    return max_d
```

## 三种解法对比

| 方法 | 空间 | 风险 | 推荐场景 |
|------|------|------|---------|
| DFS 递归 | O(h) | 深树栈溢出 | 树不深，优先 |
| BFS | O(w) | 满二叉树时宽 | 极深树（防溢出） |
| 迭代 DFS | O(n) | 无栈溢出 | 需要可控性 |
