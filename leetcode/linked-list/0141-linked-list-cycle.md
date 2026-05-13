---
题号: 141
难度: easy
tags: [linked-list, two-pointers]
状态: ✅ 已做
日期: 2026-05-12
---

# 141. Linked List Cycle

## 题目
判断链表是否有环。

## 思路

**Floyd's Cycle-Finding Algorithm（快慢指针）**

类比操场跑步：一个跑得快（每次 2 步），一个跑得慢（每次 1 步），有环则快的一定会套圈慢的。

```python
def hasCycle(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
        return False
    slow = fast = head
    while fast and fast.next:
        slow = slow.next          # 走 1 步
        fast = fast.next.next     # 走 2 步
        if slow == fast:          # 相遇即有环
            return True
    return False
```

```java
public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) return false;
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) return true;
        }
        return false;
    }
}
```

复杂度：O(n) / O(1)

## 关键点

- **空指针防护**：`while (fast != null && fast.next != null)` — 确保安全使用 `fast.next.next`
- 快慢指针还用于：找链表中间节点、找入环节点
