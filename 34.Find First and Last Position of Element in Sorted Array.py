#
# @lc app=leetcode id=34 lang=python3
# @lcpr version=30400
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start

from typing import List 
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1 

        res = [-1, -1] 

        while left <= right:
            mid = left + (right - left) // 2 
                       
            if nums[mid] == target:
                l_bound = mid 
                r_bound = mid 

                while l_bound > 0 and nums[l_bound - 1] == target:
                    l_bound -= 1 

                while r_bound < len(nums) - 1 and nums[r_bound + 1] == target:
                    r_bound += 1 
                    
                res = [l_bound, r_bound]
                break
            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1 

        return res 


# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

