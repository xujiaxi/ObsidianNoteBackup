---
题号: 123
难度: hard
tags: [dynamic-programming, stock, state-machine]
状态: ✅ 已完成
日期: 2026-06-24
---

# 123. Best Time to Buy and Sell Stock III

## 问题

与 122 题相同（可多次交易），但**最多只能完成 2 笔交易**。不能再使用贪心。

## 核心思路

**状态机 DP**（4 个状态变量）。

把每一天结束时可能的状态抽象为 4 个：

| 状态 | 含义 | 转移方程 |
|------|------|----------|
| buy1 | 第一次买入后 | max(昨天 buy1, -price) |
| sell1 | 第一次卖出后 | max(昨天 sell1, buy1 + price) |
| buy2 | 第二次买入后 | max(昨天 buy2, sell1 - price) |
| sell2 | 第二次卖出后 | max(昨天 sell2, buy2 + price) |

最终答案 = sell2（sell2 自动继承 sell1 的利润，不需要额外取 max）。

## 初始化

| 变量 | 第一天值 | 含义 |
|------|---------|------|
| buy1 | -prices[0] | 第一天买入 |
| sell1 | 0 | 第一天买入又卖出（利润 0）|
| buy2 | -prices[0] | 第一天买入→卖出→再买入 |
| sell2 | 0 | 第一天买入→卖出→买入→卖出 |

## 代码实现

### Python — O(N) 时间, O(1) 空间

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1 = -prices[0], 0
        buy2, sell2 = -prices[0], 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
```

**注意**：因为同一天买入又卖出利润为 0，所以依次更新（而非同时赋值）在数学上等价，不会出错。

## 关键知识点

- **状态机 DP 首次引入**：121 → 2 个状态，122 → 2 个状态，123 → 4 个状态（2×k）
- **空间优化**：从 dp[天数][5] 二维数组压缩为 4 个变量，因为每天只依赖前一天的旧值
- sell2 天然 >= sell1，因为可以在第二天做一笔 0 利润的虚拟交易

## 坑点

- 不要用 `{}` 大括号初始化——Python 中这是集合（set），不是列表（list），不支持索引
- 初始化 buy2 不要设为 0，应该设为 -prices[0]（因为可以在第一天完成两次虚拟交易）

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
