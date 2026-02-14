"""
计算逆序存储的链表
解法：
    模拟竖式加法
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next

        return "->".join(vals)

class Solution:
    def AddTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        res = dummy

        total = carry = 0

        while l1 or l2 or carry:

            total = carry

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

Sol = Solution()

result = Sol.AddTwoNumbers(l1, l2)
print(result)
