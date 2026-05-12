---
题号: 105
难度: medium
tags: [tree, dfs, hash-table, divide-and-conquer]
状态: 📝 待做
日期: 2026-05-12
---

# 105. Construct Binary Tree from Preorder and Inorder Traversal

## 题目
根据前序遍历（Preorder）和中序遍历（Inorder）重建二叉树。

## 核心密码：两种遍历的特性

| 遍历 | 顺序 | 暗号 |
|------|------|------|
| **Preorder** | 根 → 左 → 右 | **第一个元素永远是当前树的根节点** |
| **Inorder** | 左 → 根 → 右 | **根节点左边的全是左子树，右边的全是右子树** |

## 思路
1. 从 preorder 拿到第一个元素作为 root
2. 在 inorder 中找到这个 root 的位置（索引 i）
3. 以 i 为界，把 inorder 切成左右两半：
   - 左半部分 = 左子树节点
   - 右半部分 = 右子树节点
4. 递归重复

**为什么 preorder 指针自增即可？**
preorder 顺序固定：`[根, (整个左子树的根), (整个右子树的根)]`。每创建一个节点就消耗一个元素，指针一直往后走，下次指出的准是"当前子树的根"。

## Python 解法

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 哈希表：值 → inorder 索引，避免每次 index() 查找
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            mid = inorder_map[root_val]

            root.left = helper(left, mid - 1)   # 必须先左后右
            root.right = helper(mid + 1, right) # preorder 是 [根,左,右]

            return root

        return helper(0, len(inorder) - 1)
```

复杂度：O(N) / O(N) — 哈希表 + 递归栈

## 关键点
- **必须先递归左子树，再递归右子树**：因为 preorder 的顺序就是 [根, 左, 右]
- **哈希表加速**：用 `inorder_map` 避免每次 O(N) 查找
- **Python 风格**：用 `self.pre_idx` 而不是全局变量传递
