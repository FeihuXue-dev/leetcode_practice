#
# @lc app=leetcode id=26 lang=python3
# @lcpr version=30307
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        
        slow = 0 
        fast = 0 
        
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1 
                nums[slow] = nums[fast]

            fast += 1 

        return slow + 1 
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

