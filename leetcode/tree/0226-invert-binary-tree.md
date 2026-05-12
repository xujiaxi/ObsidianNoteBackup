---
题号: 226
难度: easy
tags: [tree, dfs]
状态: ✅ 已做
日期: 2026-05-12
---

# 226. Invert Binary Tree

## 题目
翻转二叉树（镜像反转）。

## 思路

**自顶向下，交换每个节点的左右子节点，然后递归。**

```python
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left  # 交换
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
```

```java
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return null;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
}
```

复杂度：O(n) / O(h) — h 为树高

## 关键点

- Python 多元赋值一行完成交换，极简
- 这就是那题 Homebrew 作者在白板上没写出来的题
