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

## 深入理解

### 上下界递归 vs 中序遍历：执行逻辑差异

虽然两者都是 DFS，最坏情况复杂度相同，但**检查时机和信息流向**截然不同：

| 维度 | 上下界递归（解法一） | 中序遍历（解法二/三） |
|------|--------------------|--------------------|
| 遍历色彩 | 前序（自顶向下） | 中序（从左到右） |
| 检查时机 | 到达节点**立刻**检查 | 先摸到最左下角，**回溯时**检查 |
| 本质 | 拿着区间规则向下派发 | 把节点排成一队挨个检查 |

**剪枝效率差异**（面试加分点）：
考虑树根 = 10，左子节点 = 100（已违规），但 100 下面挂着一棵深度一万层的合法左子树：

- **上下界法**：走到 100 时发现 max=10，**立刻 return False**，一步不多走
- **中序遍历法**：不知道 100 越界，顺着 100 一路往下走一万层，摸到最左叶子才开始回溯比较，走到 100 时才发现违规

结论：当错误靠近根节点时，上下界法剪枝更早；错误在深层叶子时二者差不多。

### yield vs yield from：底层语义

| 语法 | 作用 | Java 类比 |
|------|------|-----------|
| `yield x` | 递出**一个**元素 | `list.add(x)` |
| `yield from iterable` | 把另一个集合的**所有元素**逐个递出 | `list.addAll(collection)` |

结合代码理解：

```python
def inorder(self, node):
    if node:
        yield from self.inorder(node.left)  # 左子树是一串值 → addAll
        yield node.val                       # 当前节点是一个值 → add
        yield from self.inorder(node.right) # 右子树是一串值 → addAll
```

- `yield node.val`：`node.val` 是单个数字，用 `yield` 吐出去
- `yield from self.inorder(...)`：`self.inorder()` 返回的是生成器（一串值），不是单个值。如果写成 `yield self.inorder(node.left)`，外部会收到一个生成器对象 `Generator object at 0x...`，而非里面的数字
- `yield from` 等价于内部隐式的 for 循环：`for val in self.inorder(node.left): yield val`

### Python 迭代器协议：为什么 for val in self.inorder(root) 能工作

不需要像 Java 那样手动实现 `Iterable` + `Iterator`（hasNext/next）。

**yield 的魔法**：当 Python 解析器在函数里看到 `yield`，调用时**不会立即执行函数体**，而是自动返回一个**生成器对象**。这个生成器内置了迭代器协议（`__iter__` 和 `__next__`）。

**for...in 的底层工作**：

1. 调用 `self.inorder(root)` → 返回生成器对象（不执行任何代码）
2. `for` 循环调用 `next()` → 生成器运行到第一个 `yield`，**暂停**并返回值
3. 循环体执行完毕 → 再次 `next()` → 从暂停处**恢复**，运行到下一个 `yield`...
4. 函数结束没有更多 `yield` → 自动抛出 `StopIteration` → `for` 循环捕获并优雅结束

**对比 Java**：
```java
// Java：需要手动实现 Iterator
class InorderIterator implements Iterator<Integer> {
    Stack<TreeNode> stack = new Stack<>();
    // 手动维护 hasNext()、next()、栈状态...
}

for (Iterator<Integer> it = new InorderIterator(root); it.hasNext(); ) {
    int val = it.next();
    // 检查...
}
```

```python
# Python：yield 自动搞定一切
for val in self.inorder(root):
    # 检查...
```

`yield` 就是自动记录状态的"暂停键"，`for` 就是不断按"播放键"的机器。两者结合，递归生成器一气呵成。

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
