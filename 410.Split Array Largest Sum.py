#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=30400
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List 

"""在指定的区间中，寻找最值"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        res = right 

        while left <= right:
            mid = left + (right - left) // 2 

            current_nums = 0 
            required_col = 1 

            for num in nums:
                if current_nums + num > mid:
                    required_col += 1
                    current_nums = 0 

                current_nums += num

            if required_col <= k:
                res = mid 
                right = mid - 1 

            else:
                left = mid + 1 

        return res 

            
# @lc code=end



#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#

