# 链表核心要点

> 来源：Blind 75 专题精讲
> 核心：通过改变引用（指针）的指向来重构数据结构

## 三大铁律

1. **断链预警**：修改 `curr.next` 之前，先存下 `curr.next`
2. **空指针检查**：用 `.next.next` 前，确保 `fast` 和 `fast.next` 都不是 None
3. **Dummy Node**：`dummy = ListNode(0)` 简化头节点增减判断

## 链表初始化 (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## 核心技巧总结

| 技巧 | 适用场景 | 核心目的 |
|------|---------|---------|
| Dummy Node | 合并、删除、修改头节点 | 避免处理 `head is None` 或头节点变动的特殊逻辑 |
| 快慢指针 | 找中点、判断环、找倒数第 N 个 | 在单向遍历中获取"位置关系"或"速度差" |
| 反转指针 | 反转链表、判断回文 | 改变链表的物理结构 |
| 多指针 | 合并有序链表、分区链表 | 同时处理多个逻辑流 |

## 相关题目

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
