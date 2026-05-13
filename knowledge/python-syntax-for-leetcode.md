# LeetCode 刷题 Python 语法速查

> 对比 Java 视角，聚焦刷题中容易混淆的 Python 语法点

## 类型提示 (Type Hints)

Python 3 的类型注解，**不会强制约束运行**，但让 IDE 能帮你补全和检查。

| 写法 | 含义 |
|------|------|
| `def f() -> int:` | 返回 int |
| `def f() -> None:` | 无返回值 |
| `def f(root: TreeNode) -> TreeNode:` | 参数和返回都是 TreeNode |
| `def f(root: Optional[TreeNode]) -> TreeNode:` | 参数可能是 TreeNode 或 None |
| `def f() -> List[List[int]]:` | 返回二维 int 列表 |
| `def f(visited: List[int]) -> bool:` | visited 是 int 列表 |
| `def f(head: Optional[ListNode]) -> Optional[ListNode]:` | 参数和返回值都可能为 None |

**Optional[T] 等价于 Union[T, None]，Python 3.10+ 可简写为 `T | None`。**

## 空值判断

```python
# ✅ Python 风格（推荐）
if not node:     # 检查 None
if node:         # 检查非 None

# ❌ Java 风格（不推荐）
if node == None:
if node is None:
```

## 默认初始值

Java 中 `int[] arr = new int[10]` 自动填 0，但 Python 列表**没有默认值**：

```python
# 需要手动初始化
visited = [0] * n           # ✅ 正确：[0, 0, 0, ...]
visited = [False] * n       # ✅ 布尔值也可以
count = [0] * 128           # ✅ 滑动窗口用的频率数组
arr = [[] for _ in range(n)]  # ✅ 二维空列表，注意不能 [[]]*n（那是引用同一个对象）

# ❌ 常见错误
arr = [0] * n   # 如果 n 是 0，arr 是 []，后面 arr[索引] 会越界
```

## deque：队列首选

BFS 中**必须用 deque**，不要用 list 做队列。

```python
from collections import deque

q = deque([root])         # 初始化
node = q.popleft()        # 队首弹出 — O(1)
q.append(node.left)       # 队尾加入 — O(1)
q.appendleft(val)         # 队首加入 — O(1)（栈/DFS 时用）
len(q)                    # 队列长度
```

| 操作 | deque | list |
|------|-------|------|
| `popleft()` / `pop(0)` | **O(1)** | **O(N)**（所有元素前移） |
| `append()` | O(1) | O(1) |
| `pop()` | O(1) | O(1) |

**list.pop(0) 会导致 BFS 退化为 O(N²)，必超时。**

## 多元赋值 / 元组解包 (Tuple Unpacking)

Python 的 `a, b = b, a` 是**原子操作**，不需要临时变量。

```python
# 交换两个变量
a, b = b, a

# 链表反转（一行版，面试慎用）
curr.next, prev, curr = prev, curr, curr.next

# 同时处理多个返回值
left, right = right, left  # 翻转二叉树
```

⚠️ **注意顺序**：Python 先计算等号右边的所有表达式，再统一赋值给左边。所以 `curr.next, prev, curr = prev, curr, curr.next` 中，`curr.next` 拿到的是旧的 `prev` 值。

## `or` 做 None 合并

相当于 C# 的 `??` 或 JavaScript 的 `??`：

```python
# 返回第一个非 None 的值
return left or right         # left 非 None 返回 left，否则返回 right
curr.next = l1 or l2         # l1 非 None 接 l1，否则接 l2

# 等价于
return left if left else right
```

## 三元表达式

```python
# Python 风格（没有 ?: 运算符）
max_val = a if a > b else b
res.append(left) if left else res.append(right)

# Java 风格
int maxVal = (a > b) ? a : b;
```

## `not` vs `!=` vs `is not`

```python
if not node:          # node 为 None/False/0/空列表时成立（宽松）
if node is not None:  # 严格检查 node 不是 None
if node != None:      # 等于判断，通常也可以用，但不如 `is not` 地道

# LeetCode 中推荐
if not head or not head.next: return False  # ✅ 简洁
if head is None or head.next is None: ...   # ❌ 啰嗦
```

## 字典操作

```python
# 频率统计
count = {}
for c in s:
    count[c] = count.get(c, 0) + 1    # 推荐：用 get 设默认值

# 等价写法
from collections import defaultdict
count = defaultdict(int)
for c in s:
    count[c] += 1

# 检查 key 是否存在
if c in count:     # ✅
if count.get(c):   # ⚠️ 如果值是 0，这个判断不成立

# 删除
del count[c]
```

## 列表生成式

```python
# 快速初始化
arr = [i for i in range(n)]           # [0, 1, 2, ...]
squares = [x*x for x in range(10)]    # [0, 1, 4, 9, ...]
even = [x for x in range(10) if x%2==0]

# 二维列表
matrix = [[0] * cols for _ in range(rows)]  # ✅ 正确
matrix = [[0] * cols] * rows                  # ❌ 所有行是同一个对象！

# 字典生成式
inorder_map = {val: i for i, val in enumerate(inorder)}
```

## enumerate：同时获取索引和值

```python
# 取代 Java 的 for 循环
for i, c in enumerate(s):
    # i 是索引，c 是字符
    pass

# 对比 Java
# for (int i = 0; i < s.length(); i++) {
#     char c = s.charAt(i);
# }
```

## range 循环

```python
for _ in range(n):       # 循环 n 次，不要索引
for i in range(n):       # 0 到 n-1
for i in range(1, n):    # 1 到 n-1
for i in range(n-1, -1, -1):  # n-1 到 0（倒序）
```

## ord()：字符转 ASCII 码

用于滑动窗口的数组计数法：

```python
need = [0] * 128
window = [0] * 128

for c in t:
    need[ord(c)] += 1

# 访问时
window[ord(c)] += 1
```

## 递归中修改外层变量：nonlocal

```python
def buildTree(self, preorder, inorder):
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0  # 这个变量要在嵌套函数里修改

    def helper(left, right):
        nonlocal pre_idx  # ⚠️ 不声明这个会报 UnboundLocalError
        if left > right:
            return None
        root_val = preorder[pre_idx]
        pre_idx += 1
        # ...
```

## 字符串操作

```python
s = "hello"

len(s)              # 长度
s[0]                # 索引（不能修改！字符串不可变）
s[1:3]              # 切片 "el"
s[::-1]             # 反转 "olleh"
"".join(list)       # 列表转字符串（重要！不要用 + 拼接大量字符串）
s.startswith("he")  # 前缀检查
s.endswith("lo")    # 后缀检查
s.find("ll")        # 查找子串（返回索引或 -1）
```

## 常用 import 一句话

```python
from collections import deque        # BFS 队列
from collections import defaultdict  # 自动默认值的字典
from typing import List, Optional    # 类型提示
import heapq                         # 堆 / 优先队列
import math                          # 数学运算
```

## 性能小贴士

```python
# ❌ 慢
res = []
for item in items:
    res += [item]           # 每次创建新列表

# ✅ 快
res = []
for item in items:
    res.append(item)        # O(1) 摊销
```
