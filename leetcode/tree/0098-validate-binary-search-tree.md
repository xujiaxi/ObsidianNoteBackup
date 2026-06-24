---
题号: 98
难度: medium
tags: [tree, bst, dfs, recursion, inorder]
状态: ✅ 已完成
日期: 2026-06-24
---

# 98. Validate Binary Search Tree

## 问题

给定一个二叉树的根节点，判断它是否是有效的**二叉搜索树（BST）**。

BST 定义：
- 左子树所有节点的值 **<** 当前节点值
- 右子树所有节点的值 **>** 当前节点值
- 左右子树也必须是 BST

## 解法对比

| 解法 | 思路 | 时间 | 空间 |
|------|------|------|------|
| 上下界递归 | 递归时传递 (min_val, max_val) 区间参数 | O(N) | O(H) |
| 中序遍历 | BST 中序遍历序列严格递增 | O(N) | O(H) |
| 中序 + yield | 生成器惰性遍历，解耦验证逻辑 | O(N) | O(H) |

## 解法一：上下界递归（Fail-Fast）

每个节点都有允许的取值范围，递归时向下传递：

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_val, max_val):
            if not node:
                return True
            if (min_val is not None and node.val <= min_val) or \
               (max_val is not None and node.val >= max_val):
                return False
            return helper(node.left, min_val, node.val) and \
                   helper(node.right, node.val, max_val)

        return helper(root, None, None)
```

**关键细节**：`min_val is not None` 而不是 `if min_val:` —— 因为节点值可能为 0，0 在 Python 中被视为 False。

## 解法二：中序遍历（递归版）

BST 中序遍历序列是严格递增的。用一个 `prev` 变量记录上一个访问的节点值，每次比较。

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.inorder(root)

    def inorder(self, node):
        if not node:
            return True

        if not self.inorder(node.left):
            return False

        if self.prev is not None and self.prev >= node.val:
            return False
        self.prev = node.val

        return self.inorder(node.right)
```

**Python 陷阱**：函数默认返回 `None`，`None` 被当作 False。所以最后需要 `return self.inorder(node.right)` 而不是只调用不返回。

## 解法三：中序 + yield 生成器（Pythonic）

将**遍历**与**验证**完全解耦，代码清晰且惰性求值（找到非法值立即停止遍历）。

```python
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        for val in self.inorder(root):
            if val <= prev:
                return False
            prev = val
        return True

    def inorder(self, node):
        if node:
            yield from self.inorder(node.left)
            yield node.val
            yield from self.inorder(node.right)
```

**`yield from`**：Python 3.3+ 语法，代理另一个生成器，把子生成器吐出的值一个个继续吐出去。

## 关键知识点

- BST 验证必须检查**整个子树**，不能只看直接子节点
- 中序遍历递增是 BST 的**充要条件**
- Python 类变量陷阱：`class Solution:` 下直接写 `prev = None` 是类变量（= Java static），LeetCode 多用例运行时残留数据。应在方法内用 `self.prev = None` 初始化
- `None` vs `0`：条件判断必须用 `is not None`，不能用隐式布尔值
- `yield from` 实现递归生成器——Python 独有特性

## 坑点

- 节点值可能为 `Integer.MIN_VALUE` / `float('-inf')`——用 `None` 标记"无边界"，比用极值更安全
- 中序遍历中 `prev >= node.val` 而不是 `>`（BST 要求严格递增，重复值非法）
- Python 没有方法重载，不能定义两个 `isValidBST`——助手方法要改名（如 `helper`）

## 参考链接

- https://leetcode.com/problems/validate-binary-search-tree/
- Blind 75 — Trees
