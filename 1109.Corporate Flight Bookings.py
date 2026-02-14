#
# @lc app=leetcode id=1109 lang=python3
# @lcpr version=30307
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
from typing import List 

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        nums = [0] * n 
        df = self.Difference(nums)

        for booking in bookings:
            # 此处的i，j为索引，与题目中的first point和 last point不同
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2] 

            df.increment(i, j, val)

        return df.result()

    class Difference:
        def __init__(self, nums):
            assert len(nums) > 0 

            self.diff = [0] * len(nums)

            self.diff[0] = nums[0]

            for i in range(1, len(nums)):
                self.diff[i] = nums[i] - nums[i-1]

        def increment(self, i, j, val):
            self.diff[i] += val 
            if j + 1 < len(self.diff):
                self.diff[j+1] -= val 

        def result(self):
            res = [0] * len(self.diff)

            res[0] = self.diff[0] 

            for i in range(1, len(self.diff)):
                res[i] = res[i-1] + self.diff[i] 

            return res 
        

            
# @lc code=end



#
# @lcpr case=start
# [[1,2,10],[2,3,20],[2,5,25]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,10],[2,2,15]]\n2\n
# @lcpr case=end

#

