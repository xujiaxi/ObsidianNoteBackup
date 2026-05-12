---
题号: 19
难度: medium
tags: [linked-list, two-pointers]
状态: ✅ 已做
日期: 2026-05-12
---

# 19. Remove Nth Node From End of List

## 题目
删除链表倒数第 N 个节点。要求一次遍历（One Pass）。

## 思路

**快慢指针保持间距 N**

让快指针先走 N+1 步，然后快慢一起走。当快指针走到终点时，慢指针正好在待删除节点的**前驱**位置。

为什么走 N+1 步？为了让 `slow` 停下来时指向被删节点的前一个，而不是被删节点本身。

```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n + 1):   # 先走 N+1 步
        fast = fast.next
    while fast:               # 一起走到底
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next  # 删除
    return dummy.next
```

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy, slow = dummy;
        for (int i = 0; i < n + 1; i++) fast = fast.next;
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }
        slow.next = slow.next.next;
        return dummy.next;
    }
}
```

复杂度：O(L) / O(1)

## 关键点

- **Dummy Node + 快慢指针**，一次遍历搞定
- 为什么走 N+1 步：间距 N+1 意味着 `slow` 停在被删节点的前一个
- 如果不用 Dummy Node，删除头节点时需要单独处理
