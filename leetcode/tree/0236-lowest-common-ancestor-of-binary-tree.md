---
题号: 236
难度: medium
tags: [tree, dfs]
状态: ✅ 已做
日期: 2026-05-12
---

# 236. Lowest Common Ancestor of a Binary Tree

## 题目
在普通二叉树中找到两个节点 p、q 的最近公共祖先（不是 BST，不能用值大小判断）。

## 思路

### 解法 1：DFS 递归（后序汇总，推荐）

自底向上：左右子树各自汇报搜索结果，当前节点汇总判断。

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # 左右各找到一边 → 当前节点是 LCA
    if left and right:
        return root
    # 只有一边有结果 → 继续向上传
    return left or right
```

```java
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}
```

复杂度：O(n) / O(h)

### 解法 2：存储父节点（Parent Pointers）

把树问题变成两个链表找交点。遍历全树存父亲，然后 p 向上爬记录祖先，q 向上爬找交点。

```python
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent = {root: None}
    stack = [root]
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q
```

复杂度：O(n) / O(n)

## 关键点

- **后序汇总**：先处理左右子树，再在当前节点判断 — LCA 类问题的通用模板
- Base Case：`if not root or root == p or root == q` 同时处理了空节点和命中
- 递归版代码极简，但 p/q 不在树中时会返回存在的那个节点
