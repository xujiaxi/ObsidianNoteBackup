---
题号: 714
难度: medium
tags: [dynamic-programming, stock, state-machine]
状态: ✅ 已完成
日期: 2026-06-24
---

# 714. Best Time to Buy and Sell Stock with Transaction Fee

## 问题

无限次交易（同 122 题），但**每次交易需要支付固定手续费 fee**。

## 核心思路

回到 122 题的 2 状态模型，在**买入时**（或卖出时）扣除手续费即可。本题选择在买入时扣除。

### 状态定义

| 状态 | 含义 | 转移方程 |
|------|------|----------|
| hold | 手里有股票（含已扣手续费）| max(昨天 hold, 昨天 not_hold - price - fee) |
| sell | 手里没股票 | max(昨天 sell, 昨天 hold + price) |

两种扣费方式等价（选一种，不要重复扣）：
- **买入扣费（本解法）**：`buy = max(buy, sell - price - fee)`
- **卖出扣费**：`sell = max(sell, buy + price - fee)`

## 代码实现

### Python — 买入时扣手续费

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, sell = -prices[0] - fee, 0
        for price in prices[1:]:
            hold, sell = (
                max(hold, sell - price - fee),
                max(sell, hold + price)
            )
        return sell
```

### Python — 卖出时扣手续费（等价写法）

```python
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold, sell = -prices[0], 0
        for price in prices[1:]:
            hold, sell = (
                max(hold, sell - price),
                max(sell, hold + price - fee)
            )
        return sell
```

## 关键知识点

- 没有冷冻期 → 回到 2 状态（hold / not_hold），不需要 3 状态
- **手续费只扣一次**：在买入或卖出中选一个时机扣，不能两头扣
- 初始化时，如果买入扣费则 hold = -prices[0] - fee；如果卖出扣费则 hold = -prices[0]（首次买入后还没卖出，不扣费）

## 解法对比

| 解法 | 时间 | 空间 | 说明 |
|------|------|------|------|
| 状态机 DP（买入扣费）| O(N) | O(1) | 推荐，与 309 题写法一致 |
| 状态机 DP（卖出扣费）| O(N) | O(1) | 等价写法 |
| 贪心 + fee | O(N) | O(1) | 需要维护 min_price_with_fee，较复杂 |

## 坑点

- 不要把 fee 写死成数字 2 或其它示例值——必须用参数 `fee`
- 不要买入扣一次、卖出又扣一次——同一笔交易只交一次手续费
- 多元赋值确保 hold 和 sell 互不影响

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
