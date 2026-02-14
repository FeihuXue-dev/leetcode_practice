#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30307
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.

from typing import Optional 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummpy = ListNode()

        res = dummpy 

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
            dummpy.next = ListNode(num)
            dummpy = dummpy.next 

        return res.next 


# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

