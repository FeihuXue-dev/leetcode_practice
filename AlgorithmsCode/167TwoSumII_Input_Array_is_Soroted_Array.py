"""
返回非严格排序数组中两个数字之和等于目标数字的索引
解法:
    二分法
"""
from typing import List

def twoSum(self, numbers:List[int], target:int) -> List[int]:
    left, right = 0, len(numbers) - 1
    sum = numbers[left] + numbers[right]

    if sum == target:
        return [left+1, right+1]
    elif sum < target:
        left += 1

    elif sum > target:
        right -= 1

    return [left+1, right+1]
