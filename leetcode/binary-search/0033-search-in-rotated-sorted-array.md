---
题号: 33
难度: medium
tags: [array, binary-search]
状态: 📝 待做
日期: 2026-05-12
---

# 33. Search in Rotated Sorted Array

## 题目
在旋转过的升序数组中找 target。要求 O(logN)。

## 思路
**Template**: 找特定目标 → `while (left <= right)`

**核心思维**：在任一 mid 切开，**至少有一半是绝对有序的**。先找到有序的那一半，检查 target 是否在其中。

1. 算出 mid
2. 判断哪一半有序：`nums[left] <= nums[mid]` → 左边有序
3. 检查 target 是否在有序区间内
4. 在 → 去那一半找；不在 → 去另一半

## Java 解法

```java
class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) return mid;

            if (nums[left] <= nums[mid]) {  // 左半边有序
                if (target >= nums[left] && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {  // 右半边有序
                if (target > nums[mid] && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
}
```

复杂度：O(logN) / O(1)

## 关键点
- 先判断哪边有序（左右等价，习惯先判断左边）
- `mid - 1` / `mid + 1`：因为已确认 `nums[mid] != target`
- `nums[left] <= nums[mid]` 用 `<=`：处理两个元素时的情况（[3, 1], left=0, mid=0）
- **排除法思维**：先检查有序区间 → target 不在里就去另一半（可能含断层）
