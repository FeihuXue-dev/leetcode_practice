"""
找到升序数组中的指定数字所有的索引
解法：
    二分查找，注意左右的闭区间
"""

from importlib.resources import Resource
from typing import List, Optional

class Solution:
    def searchRange(self, nums:List[int], target:int) -> Optional[List]:
        left, right = 0, len(nums) - 1

        res = [-1, -1]

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                l_bound = mid
                r_bound = mid

                while l_bound > 0 and nums[l_bound - 1] == target:
                    l_bound -= 1

                while r_bound < len(nums) - 1 and nums[r_bound + 1] == target:
                    r_bound += 1

                res = [l_bound, r_bound]
                break # 找到了所有的目标数字的索引，则停止循环

            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        return res


input1 = [5,7,7,8,8,10]
target = 6
Sol = Solution()

result = Sol.searchRange(input1, target)

print(result)
