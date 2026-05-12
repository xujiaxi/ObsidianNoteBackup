---
题号: 153
难度: medium
tags: [array, binary-search]
状态: 📝 待做
日期: 2026-05-12
---

# 153. Find Minimum in Rotated Sorted Array

## 题目
在一个旋转过的升序数组中找最小值。要求 O(logN)。

## 思路
**Template**: 找极值 → `while (left < right)`

**关键洞察**：右边界 `nums[right]` 永远属于"小段升序"末尾。
- `nums[mid] > nums[right]` → mid 在大段升序中，最小值在右边 → `left = mid + 1`
- `nums[mid] < nums[right]` → mid 已进入小段升序，mid 自己可能是最小值 → `right = mid`

## Java 解法

```java
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;  // mid 不可能是最小值，跳过
            } else {
                right = mid;     // mid 可能是最小值，保留
            }
        }
        return nums[left];  // left == right
    }
}
```

复杂度：O(logN) / O(1)

## 关键点
- 用右边界判断（左边界有二义性）
- 为什么 `right = mid` 而不是 `mid - 1`？因为 mid **可能**就是最小值
- 循环条件 `left < right`，退出时返回谁都一样
