---
题号: 53
难度: medium
tags: [array, dp, divide-and-conquer, kadane]
状态: ✅ 已做
日期: 2026-07-15
---

# 53. Maximum Subarray（最大子数组和）

## 问题

给定一个整数数组 `nums`，找到一个具有最大和的**连续子数组**（子数组最少包含一个元素），返回其最大和。

**示例：**
```
输入: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
输出: 6
解释: 连续子数组 [4, -1, 2, 1] 的和最大，为 6。
```

## 思路

核心决策：对于每个元素，是**延续前面的子数组**（前面的和为正数，锦上添花），还是**自己重新开始**（前面的和为负数，拖了后腿）。

## 解法对比

| 解法 | 时间 | 空间 | 特点 |
|------|------|------|------|
| 暴力枚举 | O(n²) ~ O(n³) | O(1) | 直观但效率低 |
| DP（Kadane，数组版） | O(n) | O(n) | 状态转移清晰易懂 |
| **Kadane（空间优化版）** | **O(n)** | **O(1)** | 面试最优解 |
| 分治法 | O(n log n) | O(log n) | 理解递归分治思维，线段树基础 |

## 解法一：暴力枚举（Brute Force）

```python
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    ans = float('-inf')
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += nums[j]
            ans = max(ans, cur)
    return ans
```

枚举所有起点 i 和终点 j，累加求最大值。优化后 O(n²)，不优化 O(n³)。

复杂度：O(n²) / O(1)

## 解法二：动态规划 —— Kadane 算法（数组版 ✅ 推荐教学）

定义 `dp[i]` 为**以 nums[i] 结尾的连续子数组的最大和**。

**状态转移**：
```
dp[i] = max(nums[i], dp[i-1] + nums[i])
        ^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^
       自己单干    延续前面的子数组
```

**初始条件**：`dp[0] = nums[0]`

```python
def maxSubArray(self, nums: List[int]) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    ans = dp[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        ans = max(ans, dp[i])

    return ans
```

复杂度：O(n) / O(n)

## 解法三：Kadane 空间优化版（⭐ 面试最优解）

`dp[i]` 只依赖于 `dp[i-1]`，所以不需要整个数组，一个变量足矣。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = nums[0]  # 以当前元素结尾的最大和（相当于 dp[i]）
        ans = prev_max       # 全局最大值

        for i in range(1, len(nums)):
            prev_max = max(prev_max + nums[i], nums[i])
            ans = max(ans, prev_max)

        return ans
```

**关键点**：
- `prev_max` 是「以当前元素结尾的最大连续和」，不是「全局最大和」
- 必须用两个变量分开维护（`prev_max` 做状态转移，`ans` 记全局最大）
- 如果用同一个变量：`ans = max(ans + nums[i], nums[i])` 会错，因为 `ans` 存的是全局最大值而非当前连续和，累加时可能把不相邻的元素加在一起

复杂度：O(n) / O(1)

## 解法四：分治法（Divide & Conquer）

分治法的精髓是「分而治之」。对于任意区间 `[left, right]`，最大子数组有三种情况：

1. **完全在左半部分** `[left, mid]`
2. **完全在右半部分** `[mid+1, right]`
3. **横跨中点** mid（必须包含 `nums[mid]` 和 `nums[mid+1]`）

前两种直接递归。第三种从中点向两边扩散求最大和。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide(left, right):
            if left == right:
                return nums[left]

            mid = (right - left) // 2 + left

            left_max = divide(left, mid)
            right_max = divide(mid + 1, right)

            # 计算横跨中点的最大和
            cross_max = nums[mid]
            l = mid - 1
            r = mid + 1
            curr_sum = nums[mid]

            # 向左扩散
            while l >= left:
                curr_sum += nums[l]
                l -= 1
                cross_max = max(cross_max, curr_sum)

            # 向右扩散（基于左侧最大和继续向右延伸）
            curr_sum = cross_max
            while r <= right:
                curr_sum += nums[r]
                r += 1
                cross_max = max(curr_sum, cross_max)

            return max(left_max, right_max, cross_max)

        return divide(0, len(nums) - 1)
```

**cross_max 计算详解**：
- 先向左扩散，找到包含 `nums[mid]` 的最大左侧和 L
- 再从 L 出发向右扩散，遍历所有可能的右侧组合
- 由于 L 是定值，`max(L + 右侧前缀)` = `L + max(右侧前缀)`，数学等价于标准答案的左右分开计算再相加

**避免的坑**：
- ❌ 右半部分递归传参写成 `divide(right, mid)`
- ❌ 顶层调用写成 `divide(0, len(nums))`——合法索引到 `len(nums)-1`
- ✅ 正确：`divide(mid + 1, right)` 和 `divide(0, len(nums) - 1)`

复杂度：O(n log n) / O(log n)（递归栈深度）

**为什么 O(n log n)？**
```
T(n) = 2T(n/2) + O(n)
```
根据主定理（Master Theorem），a=2, b=2, f(n)=O(n) → T(n) = O(n log n)。

每个元素在不同递归层被多次累加（平均 log n 次），但每次 cross_max 计算的是**强制锚定在不同中点**的不同子数组，不会重复计算同一个子数组。

## 深入理解

### 为什么分治法的 cross_max 不会重复计算同一个子数组？

每一层的 cross_max 强制锚定在该层的中心点 mid。不同层的 mid 位置不同，所以计算的子数组必定不同。真正的最大子数组（如 `[4, -1, 2, 1]`），只在**某一层**作为 cross_max 被计算一次，在其他层被切分到左右递归中，不会再作为 cross_max 出现。

### 分治法的意义

虽然 Kadane 的 O(n) 比分治的 O(n log n) 更优，但分治法有独特价值：
- 理解**线段树**（Segment Tree）的基础——如果题目变成"动态修改数组元素 + 随时查询最大子数组和"，Kadane 就失效了，必须用线段树
- 锻炼递归分治思维

## 关键知识点

- Kadane 算法的本质：**退化到 O(1) 空间的 DP**
- 状态定义：`dp[i]` = 以 nums[i] **结尾**的最大和（不是前 i 个元素的最大和）
- 决策点：延续 vs 重新开始 → `max(dp[i-1] + nums[i], nums[i])`
- 分治法：三类子问题（左、右、横跨中点）取最大，注意递归边界

## 坑点

- Kadane 空间优化版中，**不要**把「当前连续和」和「全局最大和」混用一个变量
- 分治法的顶层调用用 `len(nums) - 1` 而不是 `len(nums)`，否则数组越界
- 分治法递归参数：右侧从 `mid+1` 开始，不是从 `mid` 开始（会无限递归）

## 参考链接

- https://leetcode.com/problems/maximum-subarray/
- Blind 75 — Arrays
