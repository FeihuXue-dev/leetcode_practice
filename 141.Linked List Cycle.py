#
# @lc app=leetcode id=141 lang=python3
# @lcpr version=30307
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:    
            slow = head 
            fast = head.next

            while slow is not fast:
                slow = slow.next 
                fast = fast.next.next 

            return True
        except:
            return False 
       
    
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

