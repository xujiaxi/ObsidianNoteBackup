---
题号: 100
难度: easy
tags: [tree, dfs, recursion]
状态: ✅ 已完成
日期: 2026-06-24
---

# 100. Same Tree

## 问题

给定两个二叉树的根节点 p 和 q，判断它们是否**结构相同**且**节点值相同**。

## 核心思路

**同步 DFS 递归**：同时遍历两棵树的对应节点，一旦发现不匹配立即返回 False。

**Fail-Fast 模式**：把所有失败条件（节点空值不同、值不同）合并成一个 if 提前返回，主干只处理成功路径。

## 解法对比

| 解法 | 思路 | 时间 | 空间 |
|------|------|------|------|
| 递归 DFS（最优）| 同步遍历，fail-fast 模式 | O(min(N,M)) | O(min(H₁,H₂)) |
| 迭代 BFS | 双队列同步入队/出队 | O(min(N,M)) | O(min(N,M)) |

## 代码实现

### Python — 递归 DFS（最优解）

```python
class Solution(object):
    def isSameTree(self, p, q):
        # 都为空 → 相同
        if not p and not q:
            return True
        # 一个空、或值不同 → 不相同
        if not p or not q or p.val != q.val:
            return False
        # 递归检查左右子树
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### Python — 迭代 BFS（双队列）

```python
from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        queue = deque([(p, q)])
        while queue:
            p_node, q_node = queue.popleft()
            if not p_node and not q_node:
                continue
            if not p_node or not q_node or p_node.val != q_node.val:
                return False
            queue.append((p_node.left, q_node.left))
            queue.append((p_node.right, q_node.right))
        return True
```

## 关键知识点

- **Fail-Fast 模式**：`if not p or not q or p.val != q.val` 合并三个失败条件，代码更简洁
- **递归终止条件**：两个都为空是 True（成功基例），一个为空或值不同是 False
- 递归 DFS 空间复杂度由树高决定，最坏 O(N)（退化成链表）

## 坑点

- 不要写成 `if p.val != q.val and p and q`——如果 p 或 q 为空会 AttributeError
- `not p or not q or p.val != q.val` 利用了 Python 的短路求值（short-circuit），当 not p 为 True 时不会执行 p.val，安全
- 递归实现的 `and` 连接左右子树检查，左子树失败时不会递归右子树（短路）

## 参考链接

- https://leetcode.com/problems/same-tree/
