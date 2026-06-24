---
题号: 121
难度: easy
tags: [dynamic-programming, array, stock]
状态: ✅ 已完成
日期: 2026-06-24
---

# 121. Best Time to Buy and Sell Stock

## 问题

给定一个数组 prices，prices[i] 表示第 i 天的股票价格。只能进行一次交易（一次买入 + 一次卖出），求最大利润。不能先卖后买。

## 核心思路

维护一个**历史最低价**（min_price），遍历每一天时计算「当天价格 - 历史最低价」作为当天卖出的利润，取全局最大值。

这本质上是 **DP 状态机的最简形式**：`buy = max(buy, -price)` → `sell = max(sell, buy + price)`，但由于只能交易一次，退化为一个变量 min_price。

## 解法对比

| 解法 | 思路 | 时间 | 空间 |
|------|------|------|------|
| 暴力枚举 | 双重循环，枚举所有买入/卖出对 | O(N²) | O(1) |
| 一次遍历（最优） | 维护 min_price，每天尝试卖出 | O(N) | O(1) |
| 状态机 DP | buy = max(buy, -price); sell = max(sell, buy + price) | O(N) | O(1) |

## 代码实现

### Python — 一次遍历（最优解）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
```

### Python — 状态机 DP（为股票系列做准备）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = -prices[0]   # 买入后余额（负数）
        sell = 0            # 卖出后余额
        for price in prices:
            buy = max(buy, -price)          # 买入或不操作
            sell = max(sell, buy + price)   # 卖出或不操作
        return sell
```

## 关键知识点

- **一次遍历技巧**：只用 O(1) 空间记录历史最低价
- **状态机思维**：将每一天抽象为"持有/未持有"两个状态
- 初始化 min_price = prices[0] 是安全的（题目保证 prices 长度 ≥ 1）

## 坑点

- 如果 prices 长度小于 2，直接返回 0（但题目约束 ≥1，只需注意遍历从 [1:] 开始）
- 不能先卖后买——确保卖出发生在买入之后，min_price 只记录已遍历过的价格

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- Blind 75 — Arrays & Stock Series 开篇
