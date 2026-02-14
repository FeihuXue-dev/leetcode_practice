"""判断车辆是否能够刚好将所有乘客送到目的地
解法：
    差分数组：适用于频繁对某个区间进行增加减少的操作
"""

from typing import List
class Solution:
    def CarPooling(self, trips:List[List[int]], capacity:int) -> bool:

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

trips = [[2,1,5],[3,3,7]]

capacity = 5
Sol = Solution()
result = Sol.CarPooling(trips, capacity)

print(result)
