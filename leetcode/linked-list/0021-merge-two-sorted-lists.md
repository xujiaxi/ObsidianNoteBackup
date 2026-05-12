---
题号: 21
难度: easy
tags: [linked-list]
状态: ✅ 已做
日期: 2026-05-12
---

# 21. Merge Two Sorted Lists

## 题目
合并两个升序链表，返回一个新升序链表。

## 思路

### 解法 1：迭代（Dummy Node）

像拉链一样比较两个链表当前节点，谁小就接在后面。Dummy Node 避免头节点特殊判断。

```python
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2  # 接上剩余部分
    return dummy.next
```

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
```

复杂度：O(n+m) / O(1)

### 解法 2：递归（美感写法）

```python
def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1: return l2
    if not l2: return l1
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    l2.next = self.mergeTwoLists(l1, l2.next)
    return l2
```

复杂度：O(n+m) / O(n+m)（系统栈）

## 关键点

- Dummy Node 统一了头节点判断逻辑
- 剩余部分直接 `curr.next = l1 or l2`（Python）或三元运算符（Java）
