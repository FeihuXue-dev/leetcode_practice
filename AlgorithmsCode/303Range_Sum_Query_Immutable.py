"""计算数组区间内的元素和
解法：
    前缀和技巧
"""
# 使用前缀技巧计算逐项的和，而后需要某个区间的数值和只需要做减法即可

from typing import List
class NumArray:
    def __init__(self, nums:List[int]):
        self.preSum = [0] * (len(nums) + 1)

        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i-1] + nums[i-1]

    def SumRange(self, left: int, right:int) -> int:
        return self.preSum[right + 1] - self.preSum[left]
