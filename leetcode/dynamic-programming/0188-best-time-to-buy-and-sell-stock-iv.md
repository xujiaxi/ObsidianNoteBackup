---
题号: 188
难度: hard
tags: [dynamic-programming, stock, state-machine]
状态: ✅ 已完成
日期: 2026-06-24
---

# 188. Best Time to Buy and Sell Stock IV

## 问题

与 123 题相同，但**最多可以完成 k 笔交易**。k 是参数，0 ≤ k ≤ 100。

## 核心思路

将 123 题的 4 个状态（buy1/sell1/buy2/sell2）泛化为长度为 k 的两个数组：

- `buy[j]`：第 j+1 次买入后的最大利润
- `sell[j]`：第 j+1 次卖出后的最大利润

### 状态转移

```
buy[0]  = max(buy[0], -price)
sell[0] = max(sell[0], buy[0] + price)
for j in range(1, k):
    buy[j]  = max(buy[j], sell[j-1] - price)
    sell[j] = max(sell[j], buy[j] + price)
```

## 关键优化：贪心特判

当 k ≥ N // 2 时，限制失效，退化为无限次交易（122 题贪心），时间复杂度从 O(NK) 降为 O(N)：

```python
if k >= len(prices) // 2:
    # 使用 122 题的贪心算法
    ...
```

## 代码实现

### Python — 完整版（含贪心特判）

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # 优化：k 足够大时退化为无限次交易
        if k >= n // 2:
            ans = 0
            prev = prices[0]
            for price in prices:
                if price > prev:
                    ans += price - prev
                prev = price
            return ans

        # 常规 DP：最多 k 次交易
        buys = [-prices[0]] * k
        sells = [0] * k

        for price in prices:
            buys[0] = max(buys[0], -price)
            sells[0] = max(sells[0], buys[0] + price)
            for j in range(1, k):
                buys[j] = max(buys[j], sells[j-1] - price)
                sells[j] = max(sells[j], buys[j] + price)

        return sells[-1]
```

## 解法对比

| 解法 | 适用场景 | 时间 | 空间 | 说明 |
|------|---------|------|------|------|
| O(NK) DP | 一般情况 | O(NK) | O(K) | 标准状态机 |
| 贪心特判 | K ≥ N/2 | O(N) | O(1) | 降维到 122 题 |
| k = 0 特判 | 不允许交易 | O(1) | O(1) | 直接返回 0 |

## 关键知识点

- **泛化能力**：从 2 次到 k 次，只需把 4 个变量换成 2 个长度为 k 的数组
- **贪心优化**：面试加分项——当 K 足够大时主动提出退化
- k = 0 必须特判，否则 `buys = [-prices[0]] * 0` 会生成空列表，后续索引越界

## 坑点

- k = 0 边界条件：初始化 `[-prices[0]] * 0` 为空列表，访问 `buys[0]` 越界
- `buys = [-prices[0]] * k` 是浅拷贝，但这里元素是不可变整数，安全
- 循环内 buys[0] 单独处理（不依赖前一次 sell），for j in range(1, k) 从 1 开始

## 参考链接

- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
