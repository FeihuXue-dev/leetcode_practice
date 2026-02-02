#
# @lc app=leetcode id=27 lang=python3
# @lcpr version=30307
#
# [27] Remove Element
#

# @lc code=start
from typing import List 
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0 
        
        slow = 0 
        fast = 0 

        while fast < len(nums):
            if nums[fast] !=  val:
                nums[slow] = nums[fast]
                slow += 1 

            fast += 1 

        return slow

# @lc code=end



#
# @lcpr case=start
# [3,2,2,3]\n3\n
# @lcpr case=end

# @lcpr case=start
# [0,1,2,2,3,0,4,2]\n2\n
# @lcpr case=end

#

