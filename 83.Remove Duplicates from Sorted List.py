#
# @lc app=leetcode id=83 lang=python3
# @lcpr version=30307
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
        
        slow = head 
        fast = head 

        while fast is not None:
            if fast.val != slow.val:
                slow.next = fast 
                slow = slow.next 
            
            fast = fast.next 

        slow.next = None

        return head
        
    

# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

