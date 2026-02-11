"""
返回无序数组中两者之和为目标值的索引
解法：
    哈希表
    双指针
"""

"""解法一：双指针"""
from typing import List

class Solution:
    def TwoSum(self, nums:List[int], target:int) -> List[int]:

        nums_with_index = sorted(enumerate(nums), key=lambda x: x[1])

        left, right = 0, len(nums) - 1

        while left < right:
            sum_nums = nums_with_index[left][1] + nums_with_index[right][1]

            if sum_nums < target:
                left += 1
            elif sum_nums > target:
                right -= 1

            else:
                return [nums_with_index[left][0], nums_with_index[right][0]]

        return []

nums = [3, 2, 4]
target = 6

Sol = Solution()

result = Sol.TwoSum(nums, target)

print(result)

"""解法二：哈希表"""
