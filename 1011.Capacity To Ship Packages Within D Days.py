#
# @lc app=leetcode id=1011 lang=python3
# @lcpr version=30400
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        res = right 

        while left <= right:
            mid = left + (right - left) // 2 

            current_weight = 0 
            required_days = 1 

            for w in weights:
                if current_weight + w > mid:
                    required_days += 1 
                    current_weight = 0 

                current_weight += w 

            if required_days <= days:
                res = mid 
                right = mid - 1 

            else:
                left = mid + 1 

        return res 

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,2,2,4,1,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,1]\n4\n
# @lcpr case=end

#

