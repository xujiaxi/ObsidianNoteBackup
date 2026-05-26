---
题号: 362
难度: medium
tags: [design, queue, binary-search]
状态: ✅ 已做
日期: 2026-05-26
---

# 362. Design Hit Counter

## 题目

设计一个敲击计数器 HitCounter，统计**过去 5 分钟（300 秒）内**的敲击次数。

- `hit(timestamp)` — 在给定时间戳记录一次敲击
- `getHits(timestamp)` — 返回过去 300 秒内的敲击总数

**核心约束**：所有对 `hit` 和 `getHits` 的调用，传入的 timestamp 都是**单调递增**的（时光不会倒流）。

---

## 知识点 & 前置概念

| 概念 | 说明 |
|------|------|
| `collections.deque` | Python 双端队列，头尾操作均为 O(1) |
| 滑动窗口 | 只关心最近 300 秒的数据，过期数据可丢弃 |
| 均摊分析 | 每个元素入队一次、出队一次，总操作均摊 O(1) |
| `bisect_right` | Python 二分查找库，找第一个 > target 的索引 |
| 动态数组扩容 | Python list 底层同 Java ArrayList，可无限 append |

**Python deque 常用操作（对应 Java 写法）：**

| 操作 | Python | Java |
|------|--------|------|
| 初始化 | `q = deque()` | `Deque<int[]> q = new ArrayDeque<>()` |
| 尾部入队 | `q.append(val)` | `q.offerLast(val)` |
| 头部出队 | `q.popleft()` | `q.pollFirst()` |
| 查看头部 | `q[0]` | `q.peekFirst()` |
| 查看尾部 | `q[-1]` | `q.peekLast()` |
| 队列大小 | `len(q)` | `q.size()` |

---

## 解法 1：队列（deque）— 基础版

**核心思想**：用一个 deque 按时间顺序存 timestamp，查询时清理头部过期数据，队列长度即为结果。

```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # 清理过期数据：队头时间戳 <= timestamp - 300 即为过期
        while self.q and self.q[0] <= timestamp - 300:
            self.q.popleft()
        return len(self.q)
```

```java
class HitCounter {
    private Deque<Integer> q;

    public HitCounter() {
        q = new ArrayDeque<>();
    }

    public void hit(int timestamp) {
        q.offerLast(timestamp);
    }

    public int getHits(int timestamp) {
        while (!q.isEmpty() && q.peekFirst() <= timestamp - 300) {
            q.pollFirst();
        }
        return q.size();
    }
}
```

| 操作 | 时间复杂度 | 说明 |
|------|-----------|------|
| `hit` | O(1) | 尾部追加 |
| `getHits` | 均摊 O(1) | 每个元素最多入队出队各一次 |
| 空间 | O(N) | 只存 300 秒内的数据，N ≤ 300 |

**注意**：
- 判断条件是 `<=` 不是 `<`。第 301 秒查 `getHits(301)`，区间是 [2, 301]，第 1 秒的数据应被清除，此时 `timestamp - 300 = 1`，`q[0] <= 1` 成立，所以用 `<=`。
- 访问 `q[0]` 前要判空，否则空队列会报 `IndexError`。

---

## 解法 2：队列 + Pair — 海量并发优化（进阶）

**为什么要优化**：如果同一秒内有 100 万次 `hit`，解法 1 会在队列里塞 100 万个相同的时间戳，浪费内存。

**优化方案**：存 `[timestamp, count]` pair，同一秒的敲击合并为一个元素。

```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.q = deque()       # 存储 [timestamp, count]
        self.total = 0         # 实时维护当前有效敲击总数

    def hit(self, timestamp: int) -> None:
        self.total += 1
        # 如果队尾时间戳相同 → 合并计数
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1][1] += 1
        else:
            self.q.append([timestamp, 1])

    def getHits(self, timestamp: int) -> int:
        # 清理头部过期数据，并同步扣除 total
        while self.q and self.q[0][0] <= timestamp - 300:
            expired = self.q.popleft()
            self.total -= expired[1]
        return self.total
```

**关键细节**：
- 用 list `[timestamp, count]` 而不是 tuple `(timestamp, count)`，因为 tuple 不可修改，无法直接 `+= 1`。
- 维护 `self.total` 变量作为「记账本」：入队时加，出队时减，永远等于队列中有效敲击数。**不需要 copy**，因为过期数据已被永久移除，不会复活。
- 右侧（队尾）不需要清理。因为 timestamp 单调递增，队列里不会有「未来的数据」，队尾数据必定在当前 300 秒窗口内。

| 操作 | 时间复杂度 | 空间优势 |
|------|-----------|---------|
| `hit` | O(1) | 同一秒 100 万次 = 1 个元素 |
| `getHits` | 均摊 O(1) | 同上 |
| 空间 | O(K)，K = 过去 300 秒内**不同的秒数**（最多 300 个元素） |

---

## 解法 3：数组 + 二分查找 — 历史查询场景

**场景**：如果面试官问「不能丢弃历史数据，要支持回查任意历史时刻呢？」

利用**单调递增 = 天然有序**的特性，用 list 保留全部历史记录，查询时用二分查找定位分界点。

### 使用 bisect 标准库

```python
import bisect

class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        # bisect_right 返回第一个 > target 的索引 = 过期数据个数
        index = bisect.bisect_right(self.hits, target)
        return len(self.hits) - index
```

### 手写二分查找（面试追问版）

```python
class HitCounter:
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        target = timestamp - 300
        # 左闭右开模板：找到第一个 > target 的元素
        left, right = 0, len(self.hits)
        while left < right:
            mid = (left + right) // 2
            if self.hits[mid] <= target:
                left = mid + 1
            else:
                right = mid
        # left = 过期数据个数
        return len(self.hits) - left
```

**手写模板记忆点**（`bisect_right` 等价实现）：
- `left < right` 而非 `left <= right`
- 当 `self.hits[mid] <= target` 时，继续向右找 → `left = mid + 1`
- 当 `self.hits[mid] > target` 时，缩小右边界 → `right = mid`
- 循环结束时 `left = 第一个 > target` 的索引

| 操作 | 时间复杂度 | 空间 |
|------|-----------|------|
| `hit` | O(1) | O(N)，全部历史 |
| `getHits` | O(log N) | — |

**这道题的 tag 会包含 Binary Search 的原因**：利用「单调递增 = 有序」的特点，二分查找也是一条可行的路。

---

## 三种解法对比

| 维度 | 解法 1（队列） | 解法 2（Pair） | 解法 3（二分） |
|------|--------------|---------------|---------------|
| 查询时间 | O(1) 均摊 | O(1) 均摊 | O(log N) |
| 空间 | O(N), N≤300 | O(K), K≤300 | O(N)，无限增长 |
| 丢弃历史 | ✅ 丢弃 | ✅ 丢弃 | ❌ 保留全部 |
| 面试推荐 | 最经典 | 进阶 Follow-up | 针对追问的备选 |

## Python 常见坑

1. **缩进**：手写二分时 `return` 不要缩进到 `while` 循环内部，否则函数会在第一次迭代就返回，不会完成二分搜索。
2. **空队列访问**：`q[0]` 或 `q[-1]` 前必须先 `if q:` 判空。
3. **tuple vs list**：tuple 不可修改，要修改队尾时用 list `[timestamp, count]`。
4. **Python list 无需声明长度**：同 Java ArrayList，动态扩容，`append` 均摊 O(1)。
5. **deque 不是默认导入的**：需要 `from collections import deque`。
