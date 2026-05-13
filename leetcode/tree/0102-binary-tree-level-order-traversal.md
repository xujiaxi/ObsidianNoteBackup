---
题号: 102
难度: medium
tags: [tree, bfs]
状态: ✅ 已做
日期: 2026-05-12
---

# 102. Binary Tree Level Order Traversal

## 题目
二叉树层序遍历，每一层作为一个列表返回。

## 思路

**BFS 标准模板**：使用 deque 队列，每层开始前记录 `len(queue)` 确定当前层的节点数。

```python
from collections import deque

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res
```

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.offer(node.left);
                if (node.right != null) q.offer(node.right);
            }
            res.add(level);
        }
        return res;
    }
}
```

复杂度：O(n) / O(n)（队列最宽时）

## 关键点

- **必须用 `deque`**（Python）或 `LinkedList`（Java）做队列，`pop(0)` 是 O(n) 行为
- BFS 和迭代 DFS 的代码仅差一字：Queue 用 `popleft()` / `poll()`，Stack 用 `pop()`
