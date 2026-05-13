---
题号: 206
难度: easy
tags: [linked-list]
状态: ✅ 已做
日期: 2026-05-12
---

# 206. Reverse Linked List

## 题目
反转单链表。1 -> 2 -> 3 -> null → 3 -> 2 -> 1 -> null。

## 思路

### 解法 1：迭代（三指针推移）
需要三个指针：`prev`（前驱）、`curr`（当前）、`next_temp`（暂存下一站）。每次让 `curr.next` 指向 `prev`。

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head
    while curr:
        next_temp = curr.next  # 1. 存下一站
        curr.next = prev       # 2. 反转指向
        prev, curr = curr, next_temp  # 3. 整体移动
    return prev
```

```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null, curr = head;
        while (curr != null) {
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }
}
```

复杂度：O(n) / O(1)

### 解法 2：递归（从后往前反转）

核心思想：假设后面已经反转好了，让 `head.next.next = head` 实现反转。

```python
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head  # 让下一个节点指向我
    head.next = None       # 断链
    return new_head
```

复杂度：O(n) / O(n)（系统栈）

### 关键点

- **迭代**：从前往后，O(1) 空间，面试首选
- **递归**：从后往前，代码极简但要防栈溢出
- Python 多元赋值：`a, b = b, a` 是原子操作，可省临时变量
