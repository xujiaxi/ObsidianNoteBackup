---
题号: 122
难度: medium
tags: [greedy, stock, array]
状态: ✅ 已完成
日期: 2026-06-24
---

# 122. Best Time to Buy and Sell Stock II

## 问题

与 121 题相同，但可以**进行任意多次交易**（每次买入前必须卖出已有股票）。求最大总利润。

## 核心思路

**贪心算法**：只要今天的价格比昨天高，就进行一次「昨天买今天卖」的模拟交易。把所有正差价累加即为最大利润。

为什么贪心是对的？连续上涨时，P₃ - P₁ = (P₃ - P₂) + (P₂ - P₁)，分段交易等价于一次交易。所以「只要有利润就卖」不会错过任何收益。

## 解法对比

| 解法 | 思路 | 时间 | 空间 |
|------|------|------|------|
| 贪心（最优） | 累加所有 price[i] > price[i-1] 的差价 | O(N) | O(1) |
| 状态机 DP | hold = max(hold, not_hold - price); not_hold = max(not_hold, hold + price) | O(N) | O(1) |
| 峰谷法 | 找所有上升段的谷底和峰顶 | O(N) | O(1) |

## 代码实现

### Python — 贪心（最优解）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        prev = prices[0]
        for price in prices:
            if price > prev:
                ans += price - prev
            prev = price
        return ans
```

### Python — 状态机 DP

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -prices[0]   # 持有股票
        not_hold = 0        # 不持股票
        for price in prices:
            hold = max(hold, not_hold - price)
            not_hold = max(not_hold, hold + price)
        return not_hold
```

## 关键知识点

- **贪心 vs DP**：无限次交易下贪心是捷径，但加限制条件后（冷冻期、手续费、次数限制）必须回归状态机 DP
- 第 122 题的状态机只有 2 个状态，是理解后面 3 状态（309）和 2k 状态（188）的基础

## 坑点

- 贪心解法中，`prev = price` 必须放在 if 外面——无论是否交易都需要更新 prev
- 初始化 prev = prices[0] 没有问题，遍历从 prices 第一项开始即可

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
