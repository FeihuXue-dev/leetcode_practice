"""
按照要求从head开始反转链表节点
解法：采用三个指针，通过迭代实现
"""

from typing import Optional

# 链表结点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeLinkedList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        pre, cur, nxt = None, head, head.next

        while cur != None:
            cur.next = pre

            pre = cur
            cur = nxt

            if nxt is not None:
                nxt = nxt.next

        return pre
