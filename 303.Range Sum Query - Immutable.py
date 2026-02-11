#
# @lc app=leetcode id=303 lang=python3
# @lcpr version=30307
#
# [303] Range Sum Query - Immutable
#
from typing import List 

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1)

        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]


    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right + 1] - self.preSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end



#
# @lcpr case=start
# ["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]\n
# @lcpr case=end

#

