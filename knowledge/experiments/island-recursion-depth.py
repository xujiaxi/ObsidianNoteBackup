"""
网格 DFS 递归深度实测（LC 200 / 934 类题目）

用途：验证"Python 递归 DFS 什么时候爆栈"。
结论：栈深度由最大连通块的蛇形路径长度决定，不是网格尺寸。
      n×n 全 1 实心块 → 深度 = n²（n ≥ 32 就超 Python 默认 limit=1000）。
      100x100 随机网格：密度 0.5 深度仅 ~85，密度 0.7+ 直接爆栈。

运行：python3 island-recursion-depth.py
记录日期：2026-09-18（CPython 3.13.5, Raspberry Pi / aarch64）
"""

import random
import sys

print("python", sys.version.split()[0], "| default recursionlimit =", sys.getrecursionlimit())


def probe_solid(n):
    """n x n 全 1 方块：最坏情况"""
    grid = [["1"] * n for _ in range(n)]
    maxd = 0

    def dfs(r, c, d):
        nonlocal maxd
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != "1":
            return
        if d > maxd:
            maxd = d
        grid[r][c] = "0"
        dfs(r - 1, c, d + 1)
        dfs(r + 1, c, d + 1)
        dfs(r, c - 1, d + 1)
        dfs(r, c + 1, d + 1)

    try:
        dfs(0, 0, 1)
        return f"n={n:4d}  格数={n * n:6d}  通过  max深度={maxd}"
    except RecursionError:
        return f"n={n:4d}  格数={n * n:6d}  RecursionError (爆在 {maxd})"


def probe_random(n, p, seed):
    """n x n 随机网格，密度 p"""
    random.seed(seed)
    grid = [["1" if random.random() < p else "0" for _ in range(n)] for _ in range(n)]
    maxd = 0

    def dfs(r, c, d):
        nonlocal maxd
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != "1":
            return
        if d > maxd:
            maxd = d
        grid[r][c] = "0"
        dfs(r - 1, c, d + 1)
        dfs(r + 1, c, d + 1)
        dfs(r, c - 1, d + 1)
        dfs(r, c + 1, d + 1)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "1":
                try:
                    dfs(i, j, 1)
                except RecursionError:
                    return f"密度{p}  seed{seed}: RecursionError (已到深度 {maxd})"
    return f"密度{p}  seed{seed}: 通过  max深度={maxd}"


if __name__ == "__main__":
    print("\n[1] 实心方块（最坏情况）")
    for n in (10, 20, 30, 32, 40, 100, 300):
        print("   ", probe_solid(n))

    print("\n[2] 100x100 随机网格")
    for p in (0.3, 0.5, 0.7, 0.9):
        print("   ", probe_random(100, p, 1))
