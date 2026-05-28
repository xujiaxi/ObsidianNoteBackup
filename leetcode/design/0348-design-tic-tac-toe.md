---
题号: 348
难度: medium
tags: [design, array, matrix]
状态: ✅ 已做
日期: 2026-05-27
---

# 348. Design Tic-Tac-Toe

## 题目

设计一个 n×n 的井字棋（Tic-Tac-Toe）游戏，实现 `move(row, col, player)` 方法：

- 玩家 1 和玩家 2 轮流在空位落子
- 每次落子后判断该玩家是否获胜
- 获胜条件：某玩家在**任意一行、一列、主对角线或副对角线**上连满 n 个棋子
- 题目保证每次落子都是合法的（不会下在已有棋子的位置）

---

## 知识点 & 前置概念

| 概念 | 说明 |
|------|------|
| Python 列表推导式 | `[[0]*n for _ in range(n)]` 初始化二维数组 |
| 列表引用陷阱 | `[[0]*n] * n` 会导致多行共享同一内存，改一行全变 |
| `all()` 内置函数 | 判断可迭代对象中所有元素是否满足条件，短路执行 |
| 正负计分法 | 用 +1/-1 替代直接加 player(1/2)，避免混合棋子误判 |
| `abs()` 绝对值判断 | `abs(score) == n` 判断是否有一方连满 |
| 副对角线坐标规律 | 副对角线上 `row + col == n - 1` |

### Python 二维数组初始化详解

```python
# ✅ 正确写法：列表推导式
board = [[0] * n for _ in range(n)]

# ❌ 错误写法：多行共享同一引用
board = [[0] * n] * n   # 修改 board[0][0] 会影响所有行

# 这里拆解一下 [[0] * n for _ in range(n)]：
#   [0] * n           → 生成长度为 n 的一维列表 [0, 0, ..., 0]
#   for _ in range(n) → 重复 n 次，每次生成独立的新列表
#   _                 → 占位符，表示"只需要循环次数，不需要索引值"
```

---

## 解法 1：暴力法（Brute Force）— O(N)

**核心思想**：用 n×n 棋盘记录落子，每次 move 后遍历检查该行、该列、两条对角线。

### 实现

```python
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player

        # 检查行
        if all(self.board[row][i] == player for i in range(self.n)):
            return player

        # 检查列
        if all(self.board[i][col] == player for i in range(self.n)):
            return player

        # 检查主对角线 (左上→右下：row == col)
        if all(self.board[i][i] == player for i in range(self.n)):
            return player

        # 检查副对角线 (右上→左下：row + col == n - 1)
        if all(self.board[i][self.n - 1 - i] == player for i in range(self.n)):
            return player

        return 0
```

### `all()` 函数详解

```python
# 直接写法（不推荐，容易忘记重置标记变量）
ans = player
for i in range(self.n):
    if self.board[row][i] != player:
        ans = 0
        break
if ans == player:
    return player

# ⭐ 用 all() 一行搞定（推荐）
if all(self.board[row][i] == player for i in range(self.n)):
    return player
```

**`all()` 的优点**：
- 语义直观，代码可读性高
- 底层有短路机制（遇到第一个 False 就停止），性能等价于 break
- 避免手动维护标记变量导致忘记重置的 Bug

**面试技巧**：先写出带 `all()` 的 O(N) 解法保底，然后主动说"我可以优化到 O(1)"。

### 时间的 vs 空间

| 维度 | 值 |
|------|----|
| 时间复杂度 | O(N) / 次 move（遍历行/列/对角线） |
| 空间复杂度 | O(N²)（存储 n×n 棋盘） |

---

## 解法 2：计分法（Score Tracking）— O(1) ⭐ 最优解

**核心思想**：放弃存储棋盘，只记录行、列、对角线的**累计分数**。

### 计分规则

| 玩家 | 加分值 | 获胜条件 |
|------|--------|---------|
| 玩家 1 | +1 | 某行/列/对角线总分 == **n** |
| 玩家 2 | -1 | 某行/列/对角线总分 == **-n** |

**为什么用±1而不是直接加player（1和2）？**

假设 n = 5 的棋盘，第一行：玩家2下了两步（+2+2=4），玩家1下一步（+1=5），此时总分 = 5。
如果检查 `score == 5 * 1` → 会错误判定玩家1获胜，但实际只下了 3 步，根本没有连满。

**±1 计分法**：混合棋子会正负抵消，只有纯 1 或纯 -1 的累加才能达到 ±n，杜绝假阳性。

### 实现

```python
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.counter = [[0] * n for _ in range(2)]  # counter[0]=行, counter[1]=列
        self.diag = [0, 0]  # diag[0]=主对角线, diag[1]=副对角线

    def move(self, row: int, col: int, player: int) -> int:
        # player(1,2) → 加分值(1,-1)
        add = 1 if player == 1 else -1

        # 1. 更新行
        self.counter[0][row] += add
        if abs(self.counter[0][row]) == self.n:
            return player

        # 2. 更新列
        self.counter[1][col] += add
        if abs(self.counter[1][col]) == self.n:
            return player

        # 3. 更新主对角线（只有 row == col 时才在此线上）
        if row == col:
            self.diag[0] += add
            if abs(self.diag[0]) == self.n:
                return player

        # 4. 更新副对角线（row + col == n - 1 才在此线上）
        if row + col == self.n - 1:
            self.diag[1] += add
            if abs(self.diag[1]) == self.n:
                return player

        return 0
```

### 时间和空间

| 维度 | 值 |
|------|----|
| 时间复杂度 | **O(1)** / 次 move（只有常数次加减法和判断） |
| 空间复杂度 | **O(N)**（两个长度为 n 的数组 + 两个整数） |

---

## 关键坐标规律

| 方向 | 条件 |
|------|------|
| **主对角线**（左上→右下） | `row == col` |
| **副对角线**（右上→左下） | `row + col == n - 1` |

**为什么副对角线的坐标是 `self.n - 1 - i`？**
- n=3 时，副对角线上三点为 (0,2)、(1,1)、(2,0)
- 规律：**行坐标 + 列坐标 = n - 1**
- 所以当行 = i 时，列 = n - 1 - i

**注意**：Tic-Tac-Toe 只有连接棋盘角落的**最长对角线**才算获胜，其余短的斜线不算。

---

## 两种解法对比

| 维度 | 暴力法 | 计分法 ⭐ |
|------|--------|----------|
| 时间复杂度 | O(N) / move | **O(1)** / move |
| 空间复杂度 | O(N²) | **O(N)** |
| 代码复杂度 | 简单直观 | 需要理解计分思想 |
| 适用场景 | 新手入门学习 | 面试最优解 |

## 面试节奏推荐

1. 先用暴力法写出带 `all()` 的 O(N) 解法（保底）
2. 主动提出优化："每次 move 都需要 O(N) 遍历，其实可以优化到 O(1)"
3. 展示计分法（±1 正负计分 + `abs()` 判断），这才是面试官最想看到的满分答案
