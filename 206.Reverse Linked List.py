#
# @lc app=leetcode id=206 lang=python3
# @lcpr version=30307
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

