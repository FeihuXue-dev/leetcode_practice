"""将k个链表进行排序
使用二叉堆来递归节点
heapq Function:
    将列表转化为堆（默认为最小堆）
    heapq.heapify(list)——将无序列表转化为最小堆 | O(N)
    heapq.heappush(heap, item)——将item放入堆中，并保持堆的特性 | O(logN)
    heapq.heappop(heap)——弹出并返回堆中的最小元素（根节点）| O(logN)
"""
import heapq
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists:List[Optional[ListNode]]) -> Optional[ListNode]:

        if lists is None:
            return None

        dummpy = ListNode(-1)

        p = dummpy
        pq = []

        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node

            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))

            p = p.next

        return dummpy.next
