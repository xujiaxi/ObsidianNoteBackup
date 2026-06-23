---
题号: 1
难度: easy
tags: [array, hash-table]
状态: ✅ 已做
日期: 2026-06-22
---

# 1. 两数之和

## 题目

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

**示例：**
```
输入: nums = [2, 7, 11, 15], target = 9
输出: [0, 1]
解释: 因为 nums[0] + nums[1] == 9，返回 [0, 1]。
```

## 思路

核心思想：用哈希表（Python dict）建立 **数值 → 索引** 的映射，实现 O(1) 查找 complement。

## 解法 1：一遍哈希表（One-pass，边查边存 ✅ 推荐）

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    return []
```

**流程（以 nums = [3, 3], target = 6 为例）：**
- i=0: complement=3，dict 空 → 没找到 → 存入 {3: 0}
- i=1: complement=3，dict 里有 3 → 找到！返回 [1, 0]

复杂度：O(n) / O(n)

## 解法 2：两遍哈希表（Two-pass，先存后查）

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]
    return []
```

复杂度：O(n) / O(n)

## 两种解法对比

| 维度 | 一遍哈希表 | 两遍哈希表 |
|------|-----------|-----------|
| 遍历次数 | 1 次，边查边存 | 2 次，先存后查 |
| 重复数处理 | 天然防止自匹配（先查后存） | 需显式 `hashmap[complement] != i` |
| 提前退出 | 找到即 return，可能提前结束 | 必须遍历完两次 |
| 实际效率 | 略快 | 稍慢 |
| 代码简洁度 | 更简洁 | 多几行 |

## Python 细节

- `hashmap = {}` 等价于 `hashmap = dict()`，底层是**哈希表（Hash Table）**，插入和查找都是 O(1)
- `return null` 是错的！Python 里用 `return None` 或 `return []`
- 为什么不用 `Counter()`？因为需要记录的是**索引**而不是频次。Counter 只统计出现次数，没有位置信息

## 关键点

- 一遍哈希表的精髓：**先检查 complement 是否已在 dict 中，再将自己存入**。保证不会匹配到同一个元素
- 遇到重复数字（如 [3, 3], target=6）不会出错：因为匹配到就立即 return，轮不到后面的覆盖
- 字典的键是数字本身，值是索引
- 题目保证有唯一解，所以不需要处理找不到的情况，但保持 return [] 是良好习惯
