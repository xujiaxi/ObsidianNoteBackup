---
题号: 14
难度: easy
tags: [string]
状态: ✅ 已做
日期: 2026-06-22
---

# 14. Longest Common Prefix (最长公共前缀)

## 题目

编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串 `""`。

**示例：**
```
输入: strs = ["flower","flow","flight"]
输出: "fl"

输入: strs = ["dog","racecar","car"]
输出: ""
```

## 思路

求多个字符串的公共前缀，本质是**逐列比对**——所有字符串的第 i 个字符必须相同，否则终止。

## 解法概览

| 解法 | 思路 | 时间复杂度 | 空间复杂度 |
|------|------|-----------|-----------|
| 纵向扫描（基础） | 逐列比对所有字符串 | O(m×n) | O(m) |
| 纵向扫描（切片优化） | 发现不匹配时用切片直接截取 | O(m×n) | O(1) |
| 极值法 (min/max) | 只比字典序最小和最大的两个字符串 | O(m×n) 但 C 底层快 | O(1) |
| 横向扫描 | 逐个字符串削短前缀 | O(m×n) | O(1) |
| zip + set | Python 魔法，一行核心逻辑 | O(m×n) | O(m) |
| 分治法 | 递归拆成两半分别求 | O(m×n) | O(log n) 栈 |
| 二分查找 | 对最短长度做二分，检查前缀是否匹配 | O(m×n log m) | O(1) |

## 解法 1：纵向扫描（基础版）

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    ans = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return ans
        ans += strs[0][i]

    return ans
```

复杂度：O(m×n) / O(m)  （ans 拼接产生新字符串）

**缺点：** ans 频繁拼接会创建多个中间字符串对象。

## 解法 2：纵向扫描（切片优化 ✅ 最终版本）

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return strs[0][:i]

    return strs[0]
```

复杂度：O(m×n) / O(1)

**改进点：** 用切片 `strs[0][:i]` 替代 ans 拼接，空间降到 O(1)。

## 解法 3：极值法（min / max）— 最快写法

利用 Python 的字典序原理：如果整个数组有公共前缀，那么**字典序最小的字符串**与**字典序最大的字符串**的公共前缀就是整个数组的答案。

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    s1, s2 = min(strs), max(strs)
    for i, c in enumerate(s1):
        if s2[i] != c:
            return s1[:i]

    return s1
```

复杂度：O(m×n) 但由 C 底层 min/max 实现，实际速度极快

**为什么 min/max 不会引入 O(n log n)：**
- `min()` / `max()` 只是线性遍历一次找极值，不是对整个数组排序
- 相当于"打擂台"——遍历所有字符串，逐个比较字典序，记录最小/最大的
- 理论和纵向扫描一样是 O(m×n)，但 C 底层的循环开销远小于 Python 双层 for 循环

**为什么不需要判断越界：**
- 如果 max_str 比 min_str 短且前面字符完全一样，则 max_str 是 min_str 的前缀
- 字典序中，前缀永远小于带后缀的字符串（如 "ab" < "abc"）
- 既然 max 是最大的，它就不可能是 min 的前缀，所以一定会在越界前出现字符不匹配

## 解法 4：横向扫描

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

复杂度：O(m×n) / O(1)

## 解法 5：zip + set（Python 优雅写法）

利用 `zip(*strs)` 按列打包（自动以最短字符串长度截断，不会越界），
每列去重后若集合长度 > 1 则结束。

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""

    ans = ""
    for chars in zip(*strs):
        if len(set(chars)) != 1:
            break
        ans += chars[0]

    return ans
```

复杂度：O(m×n) / O(m)

**zip 的妙处：** 自动以最短字符串为准截断，天然避免越界。

## 关键点

- 纵向扫描的核心是"一列一列地检查"，遇到不同就立即 return
- Python 切片 `strs[0][:i]` 比累加拼接更高效（不创建中间字符串）
- min/max 法利用字典序特性，把 m 个字符串的比较简化成 2 个
- zip(*strs) 是 Python 独有的优雅写法，面试中可以展示语言掌握度
- 注意处理空数组的边界情况
