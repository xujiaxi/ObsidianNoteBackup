---
题号: 3
难度: medium
tags: [string, sliding-window, hash-table]
状态: 📝 待做
日期: 2026-05-12
---

# 3. Longest Substring Without Repeating Characters

## 题目
给定字符串，找无重复字符的最长子串长度。

## 思路
**滑动窗口（找最长）**：窗口合法时 r 继续走，窗口非法（有重复）时 l 收缩。

**int[128] 替代 HashMap**：字符类题目用数组性能更好（连续内存，O(1) 访问）。

## Java 解法

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] count = new int[128];
        int left = 0, right = 0, res = 0;

        while (right < s.length()) {
            char rChar = s.charAt(right);
            count[rChar]++;            // 加入窗口

            // 重复了 → 收缩左边界
            while (count[rChar] > 1) {
                char lChar = s.charAt(left);
                count[lChar]--;        // 先移出
                left++;                // 再移动
            }

            res = Math.max(res, right - left + 1);
            right++;
        }
        return res;
    }
}
```

复杂度：O(N) / O(1)（固定大小 128）

## 常见错误（你的代码）

```java
// ❌ 错误：先 l++ 再 remove，移错了字符
l++;
map.remove(s.charAt(l));

// ❌ 错误：r 不移动，死循环
// ✅ 修正：r 每一轮只加一次

// ❌ 错误：维护 ans 独立计数器
// ✅ 修正：统一用 right - left + 1
```

## 优化思路
可用 HashMap<Character, Integer> 记录每个字符**上次出现的位置**，发现重复时 left 直接跳到上次位置 + 1，不需要 while 逐步收缩。
