"""
标准的二分搜索
"""
from typing import Optional, List
class Solution:
    def binary_search(self, nums:List[int], target:int) -> Optional[int]:

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return -1

    def left_round(self, nums:List[int], target:int) -> Optional[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right -  left) // 2

            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left =  mid + 1

        if left < 0 or left >= len(nums):
            return -1

        return left if nums[left] == target else -1

    def right_round(self, nums:List[int], target:int) -> Optional[int]:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                left = mid + 1

            elif nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

        if right < 0 or right >= len(nums):
            return -1

        return right if nums[right] == target else -1
