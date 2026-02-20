#
# @lc app=leetcode id=875 lang=python3
# @lcpr version=30400
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        res = right

        while left <= right:
            mid = left + (right - left) // 2 
            total_hours = 0 

            for p in piles:
                total_hours += (p + mid -1) // mid 

            if total_hours <= h:
                res = mid 
                right = mid - 1 
            else:
                left = mid + 1 
        return res 

# @lc code=end



#
# @lcpr case=start
# [3,6,7,11]\n8\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n5\n
# @lcpr case=end

# @lcpr case=start
# [30,11,23,4,20]\n6\n
# @lcpr case=end

#

