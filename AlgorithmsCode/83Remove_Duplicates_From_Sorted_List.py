"""
移除非严格排序的链表中的重复数字
解法：
    使用快慢指针的解法来解决
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeDuplicatedFromsortedList(self, head:Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    slow = head
    fast = head

    while fast is not None:
        if slow.val != fast.val:
            slow.next = fast
            slow = slow.next

        fast = fast.next

    slow.next = None
    return head
