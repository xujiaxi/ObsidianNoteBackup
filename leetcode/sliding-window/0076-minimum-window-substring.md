---
题号: 76
难度: hard
tags: [string, sliding-window, hash-table]
状态: 📝 待做
日期: 2026-05-12
---

# 76. Minimum Window Substring

## 题目
在 s 中找最短子串，使其包含 t 中所有字符。

例子：s = "ADOBECODEBANC", t = "ABC" → "BANC"

## 思路
**滑动窗口（找最短）**：窗口不满足条件时 r 扩张，窗口满足条件时 l 试探收缩。

**核心设计：valid 计数器**
- `need[]`：t 中每种字符的需求量
- `window[]`：当前窗口计数
- `valid`：已有多少种字符满足 need
- `totalNeeded`：t 中不同字符的种类数

## Java 解法

```java
class Solution {
    public String minWindow(String s, String t) {
        int[] need = new int[128];
        for (char c : t.toCharArray()) need[c]++;

        int[] window = new int[128];
        int left = 0, right = 0, valid = 0;
        int totalNeeded = 0;
        for (int i = 0; i < 128; i++) {
            if (need[i] > 0) totalNeeded++;
        }

        int start = 0, minLen = Integer.MAX_VALUE;

        while (right < s.length()) {
            char c = s.charAt(right);
            if (need[c] > 0) {
                window[c]++;
                if (window[c] == need[c]) valid++;
            }

            // 窗口已覆盖 t → 收缩
            while (valid == totalNeeded) {
                if (right - left + 1 < minLen) {
                    start = left;
                    minLen = right - left + 1;
                }
                char d = s.charAt(left);
                if (need[d] > 0) {
                    if (window[d] == need[d]) valid--;
                    window[d]--;
                }
                left++;
            }
            right++;
        }
        return minLen == Integer.MAX_VALUE ? "" : s.substring(start, start + minLen);
    }
}
```

复杂度：O(N + M) / O(1)

## 关键点

### valid vs 全量对比
- 不用 valid：每次移动都要遍历 need[128] → O(K×N)
- 用 valid：在 `window[c] == need[c]` 瞬间 +1 → O(1)

### HashMap 替代方案（减法计数法）
只用一个 map，存 t 的需求量，通过 `count = t.length()` 减到 0 判断覆盖。
但面试推荐 valid 方案：更通用、可读性更高。

### Java 避坑
```java
// ❌ 错误：Integer 对象用 == 比较
if (visited.get(c) == target.get(c))

// ✅ 正确：用 .equals()
if (visited.get(c).equals(target.get(c)))

// 原因：Java 只缓存 -128~127 的 Integer，超出范围 == 比的是地址
```
