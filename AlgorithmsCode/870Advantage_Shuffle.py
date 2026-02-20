"""
“田忌赛马”问题。给定两个数组，重新排序数组一，使得数组比数组二相比时，获得最大的优势。最大优势指数组一中的数字大于数组二的数字的次数最多
解法：
    贪心算法 + 双指针 + 排序
"""

from typing import List, Optional

class Solution:
    def advantageCount(self, nums1:List[int], nums2:List[int]) -> Optional[List[int]]:
        n = len(nums1)

        nums1.sort()

        indices = sorted(range(n), key=lambda i:nums2[i], reverse=True)

        res = [0] * n
        left, right = 0, n - 1

        for i in indices:
            if nums1[right] > nums2[i]:
                res[i] = nums1[right]
                right -= 1

            else:
                res[i] = nums1[left]
                left += 1

        return res
