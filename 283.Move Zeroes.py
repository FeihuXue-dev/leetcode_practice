#
# @lc app=leetcode id=283 lang=python3
# @lcpr version=30307
#
# [283] Move Zeroes
#

# @lc code=start
from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = self.removeElements(nums, 0)

        for i in range(p, len(nums)):
            nums[i] = 0 

    def removeElements(self, nums:List[int], val:int) -> List:
        if len(nums) == 0:
            return 0 
        
        slow, fast = 0,0 
        
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1 
            fast += 1 

        return slow 
        
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

