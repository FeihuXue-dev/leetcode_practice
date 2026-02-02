"""判断两个表链是否存在相交
给你两个指针实现
解法：取两个指针，让指针走两个链表，也就是将两个链表作为一个链表来走，这样两个指针才会同时相遇。
两个指针刚好相遇的时候就是交点，不相遇则没有没有交点
"""

from typing import Optional


class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def intersectionOfTwoLinkedLists(self, HeadA:Optional[ListNode], HeadB:Optional[ListNode]) -> Optional[bool]:

        p1 = HeadA
        p2 = HeadB
