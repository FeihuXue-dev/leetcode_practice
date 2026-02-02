"""删除链表中的倒数第k个结点
如何找到链表中的倒数第k个节点：
使用两个指针p1, p2,首先令p1=head, 使其先走k步，则其到达k+1处。
此时，再令p2=head, 使其跟着p1一起前进,当p1到达链表末端的时候,p2和p1此段走了n-k步。
则此时p1位于链表末端。p2位于链表的n-k+1处
"""
from typing import Optional

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def __lt__(self, other):
        return self.val < other.val
