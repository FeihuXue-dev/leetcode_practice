#
# @lc app=leetcode id=86 lang=python3
# @lcpr version=30307
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummpy1 = ListNode(-1)
        dummpy2 = ListNode(-1)

        p = head  
        p1 = dummpy1 
        p2 = dummpy2

        while p:
            if p.val < x:
                p1.next = p 
                p1 = p1.next
            else:
                p2.next = p 
                p2 = p2.next 

            temp = p.next 
            p.next = None 
            p = temp

        p1.next = dummpy2.next

        return dummpy1.next 
    
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

