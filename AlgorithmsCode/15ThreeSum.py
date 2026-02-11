"""
找到数组中三个数之和等于0的组合，并返回所有可能的情况
解法：
    排序+双指针

注意外部循环的基准去重和内部循环的双指针去重
"""

from typing import List

def ThreeSum(nums:List[int]) -> List[List[int]]:
    n = len(nums)
    nums = sorted(nums)

    res = []

    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]: left += 1
                while left < right and  nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return res


nums = [-1,0,1,2,-1,-4]

results = ThreeSum(nums)
print(results)
