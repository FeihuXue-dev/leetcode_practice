"""航班预订统计，根据输入的航班预订统计信息，计算各个站点之间的作为的预订结果
解法:
    差分数组
"""

from typing import List

class Solution:
    def CoporateFlightBookings(self, bookings:List[List[int]], n:int) -> List[int]:
        nums = [0] * n

        df = self.Difference(nums)

        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1

            val = booking[2]

            df.increment(i, j, val)

        return df.result()

    class Difference:
        def __init__(self, nums):
            assert len(nums) > 0

            self. diff = [0] * len(nums)

            self.diff[0] = nums[0]

            for i in range(1, len(self.diff)):
                self.diff [i] = nums[i] - nums[i-1]

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


bookings = [[1,2,10],[2,3,20],[2,5,25]]

n = 5

Sol = Solution()
results = Sol.CoporateFlightBookings(bookings, n)

print(results)
