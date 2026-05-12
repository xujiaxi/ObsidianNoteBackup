---
题号: 235
难度: medium
tags: [tree, bst, dfs]
状态: ✅ 已做
日期: 2026-05-12
---

# 235. Lowest Common Ancestor of a Binary Search Tree

## 题目
在 BST 中找到两个节点 p、q 的最近公共祖先。

## 思路

**利用 BST 性质"指路"**

BST 性质：左子树 < 根 < 右子树。对于任意节点 root：
- p 和 q 都在左边 → LCA 在 `root.left`
- p 和 q 都在右边 → LCA 在 `root.right`
- 一左一右 或 其中一个就是 root → root 本身就是 LCA

### 解法 1：迭代（O(1) 空间，推荐）

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

### 解法 2：递归

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root
```

复杂度：O(h) / O(1)（迭代） 或 O(h)（递归）

## 关键点

- 利用 BST 值大小关系，不需要遍历全树
- 判断条件：`(root.val - p.val) * (root.val - q.val) <= 0` 即为分叉点
