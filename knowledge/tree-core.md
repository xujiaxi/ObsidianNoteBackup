# 树 (Tree) 核心要点

> 来源：Blind 75 专题精讲
> 核心：树天然是递归结构 — 80% 的树题目可以用同一套 DFS/BFS 模板秒杀

## 节点定义 (Python)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## DFS vs BFS 抉择

| 场景 | 推荐 | 原因 |
|------|------|------|
| 求深度、反转、路径 | DFS（递归） | 代码极简，自底向上汇总 |
| 层序遍历、最短距离 | BFS（Queue） | 天然逐层搜索 |
| 深树（可能栈溢出） | 迭代 DFS（手动栈） | 把空间压力从系统栈转到堆内存 |

## DFS 三种遍历模板

### 前序 (Preorder: 根 → 左 → 右)
```python
def dfs(node):
    if not node: return
    # 处理当前节点
    dfs(node.left)
    dfs(node.right)
```

### 中序 (Inorder: 左 → 根 → 右) — BST 升序
```python
def dfs(node):
    if not node: return
    dfs(node.left)
    # 处理当前节点
    dfs(node.right)
```

### 后序 (Postorder: 左 → 右 → 根) — LCA 汇总
```python
def dfs(node):
    if not node: return
    dfs(node.left)
    dfs(node.right)
    # 处理当前节点（左右子树的结果已到手）
```

## BFS 层序遍历模板

```python
from collections import deque

def bfs(root):
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

## 迭代 DFS（手动维护栈）

```python
def iterative_dfs(root):
    if not root: return []
    stack = [root]
    while stack:
        node = stack.pop()
        # 前序：处理当前节点
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
```

## BST 性质

- 左子树所有值 < 根节点值 < 右子树所有值
- 中序遍历 BST 得到升序序列
- 利用大小关系可以"指路"（如 LCA 235）

## 递归三要素

1. **Base Case**：`if not root: return ...`（通常是 None / 0 / True）
2. **递归逻辑**：处理左子树、处理右子树
3. **返回值**：将子树结果向上汇总（深度/节点/布尔值）

## 相关题目

- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [100. Same Tree](https://leetcode.com/problems/same-tree/)
- [235. Lowest Common Ancestor of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [236. Lowest Common Ancestor of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
