---
题号: 253
难度: medium
tags: [heap, sweep-line, sorting]
状态: ✅ 已完成
日期: 2026-06-16
---

# 253. Meeting Rooms II (会议室 II)

## 核心问题
给定一组会议时间 `intervals = [[start, end]]`，求**至少需要多少个会议室**

等价于：求**同一时刻最多有多少个会议在同时进行**

## 两种解法对比

### 解法一：双指针（时间线扫描）
拆散所有开始/结束时间，排序后用双指针模拟会议室的占用与释放

```python
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starts = sorted(s for s, _ in intervals)
        ends   = sorted(e for _, e in intervals)

        used = 0        # 当前占用的会议室数
        s, e = 0, 0
        max_rooms = 0

        while s < len(intervals):
            if starts[s] >= ends[e]:
                used -= 1
                e += 1
            used += 1
            s += 1
            max_rooms = max(used, max_rooms)

        return max_rooms
```

### 解法二：最小堆（优先队列）
维护"最早结束"的会议室，每次看能否复用。堆内元素只增不减，最终堆的大小即总会议室数

```python
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])  # 按开始时间排序
        rooms = [intervals[0][1]]          # 堆内存结束时间

        for start, end in intervals[1:]:
            # 堆顶是最早结束的会议，若已腾出新会议室
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)

        return len(rooms)
```

## 关键知识点

### Python `heapq` 设计哲学
- Python 采用**函数 + 列表**的轻量设计，而非 Java 的 `PriorityQueue` 封装类
- `list` + `heapq` 函数就地操作，不另建类实例，减少内存开销
- 底层 C 高度优化，效率与 Java 对等
- 时间复杂度与 Java `PriorityQueue` 完全一致：peek O(1) / push/pop O(log K)

### Python heapq 用法速查
```python
import heapq
heap = []
heapq.heappush(heap, 10)       # 加入元素
earliest = heap[0]             # 查看最小值 (O(1))
min_val = heapq.heappop(heap)  # 弹出最小值 (O(log K))
```

### 排序写法
```python
# 对 intervals 按开始时间排序（原地排序）
intervals.sort(key=lambda x: x[0])
# 或等价的：
intervals.sort()  # Python 默认按列表第 0 个元素比较，可省略 lambda
```

### 两种解法的时空复杂度
| 维度 | 双指针 | 最小堆 |
|------|--------|--------|
| 时间复杂度 | O(N log N) 排序 | O(N log N) 排序 + 堆操作 |
| 空间复杂度 | O(N) 分离的数组 | O(N) 堆存储结束时间 |
| 直观度 | 高（模拟会议室占用） | 高（堆顶=最早腾出的房间） |
| 面试推荐 | 可解释性强 | 更优雅，空间开销更小 |

## 坑点
- 不要用 `max` 作变量名，覆盖 Python 内置 `max()` 函数会导致后续 `max()` 调用报错 TypeError
- 边界条件 `not intervals` 必须处理
- 时间重叠判断用 `<=`（前一个结束时间 <= 当前开始时间 → 不重叠）

## 参考
- LeetCode 253: https://leetcode.com/problems/meeting-rooms-ii/
