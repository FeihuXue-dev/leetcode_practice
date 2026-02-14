#
# @lc app=leetcode id=1094 lang=python3
# @lcpr version=30307
#
# [1094] Car Pooling
#

# @lc code=start
from typing import List 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        nums = [0] * 1001 

        df = self.Difference(nums)

        for trip in trips:
            val = trip[0] 
            i = trip[1]
            j = trip[2] - 1

            df.increment(i, j, val)

        res = df.result()


        for i in range(len(res)):
            if capacity < res[i]:
                return False 
            
        return True 
        
    class Difference:
        def __init__(self, nums:List[int]):

            self.diff = [nums[0]] + [nums[i] - nums[i-1] for i in range(1, len(nums))]

        def increment(self, i:int, j:int, val:int) -> None:
            self.diff[i] += val 

            if j + 1 < len(self.diff):
                self.diff[j+1] -= val 

        def result(self) -> List[int]:
            res = [self.diff[0]]

            for i in range(1, len(self.diff)):
                res.append(res[i-1] + self.diff[i])

            return res 



# @lc code=end



#
# @lcpr case=start
# [[2,1,5],[3,3,7]]\n4\n
# @lcpr case=end

# @lcpr case=start
# [[2,1,5],[3,3,7]]\n5\n
# @lcpr case=end

#

