"""Partition List"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(self, head: Optional[ListNode], x:int) -> Optional[ListNode]:
    p = head
    dummpy1 = ListNode(-1)
    dummpy2 = ListNode(-1)

    p1 = dummpy1
    p2 = dummpy2

    while p:
        if p.val < x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next

        temp = p
        p.next = None
        p = temp

    return dummpy1.next
