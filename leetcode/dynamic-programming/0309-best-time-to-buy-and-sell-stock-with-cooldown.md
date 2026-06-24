---
题号: 309
难度: medium
tags: [dynamic-programming, stock, state-machine]
状态: ✅ 已完成
日期: 2026-06-24
---

# 309. Best Time to Buy and Sell Stock with Cooldown

## 问题

无限次交易（同 122 题），但增加限制：**卖出股票后，第二天无法买入（冷冻期 1 天）**。

## 核心思路

因为冷冻期，「手里没股票」的状态要拆成两个：刚卖（明天不能买）vs 空仓（明天可以买）。

### 3 状态定义

| 状态 | 含义 | 转移来源 |
|------|------|----------|
| hold | 手里有股票 | 昨天就有 hold，或昨天 rest 今天买入 |
| sold | 今天刚卖出（明天冷冻期）| 昨天 hold + 今天卖出（唯一来源）|
| rest | 空仓且可买（含冷冻期后）| 昨天 rest，或昨天 sold 进入冷冻期 |

### 转移方程（多元赋值，保证每个方程读取的都是旧值）

```python
hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
```

**为什么必须多元赋值？** day N 的 sold 依赖 day N-1 的 hold，如果依次更新会覆盖旧值。

## 代码实现

### Python — O(N) 时间, O(1) 空间

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, rest = -prices[0], 0, 0
        # hold  — 手里有股票
        # sold  — 今天刚卖出（明天冷冻期）
        # rest  — 空仓可买（含冷冻期后）

        for price in prices[1:]:
            hold, sold, rest = (
                max(hold, rest - price),   # 继续持有 或 今天买入
                hold + price,              # 今天卖出（唯一来源）
                max(rest, sold)            # 继续空仓 或 冷冻期结束
            )

        return max(sold, rest)
```

## 关键知识点

- **冷冻期 = 引入第 3 个状态**：从 122 题的 2 状态（hold/not_hold）扩展到 3 状态
- **多元赋值的必要性**：sold 依赖旧 hold，hold 依赖旧 rest，用 Python 的 `a, b, c = x, y, z` 一次赋值
- 最终答案取 `max(sold, rest)`：冷冻期后可能手里没股票但还有利润

## 坑点

- 初始化时已经处理了 prices[0]，循环应从 `prices[1:]` 开始
- 不要写成 `sell = max(buy + price, rest + price)`，rest 状态下没股票可卖
- 如果只写 `sell = buy + price` 会更严谨，但 `max(buy + price, rest)` 也能通过

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
