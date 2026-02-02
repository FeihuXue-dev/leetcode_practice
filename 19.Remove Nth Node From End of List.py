#
# @lc app=leetcode id=19 lang=python3
# @lcpr version=30307
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def FindFormEnd(head: ListNode, k:int) -> ListNode:
    p1 = head 

    for i in range(k):
        p1 = p1.next 

    p2 = head 
    
    while p1!= None:
        p2 = p2.next 
        p1 = p1.next 

    return p2 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        x = FindFormEnd(dummy, n+1)
        x.next = x.next.next 

        return dummy.next


        



# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

