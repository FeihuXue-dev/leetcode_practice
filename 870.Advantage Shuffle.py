#
# @lc app=leetcode id=870 lang=python3
# @lcpr version=30400
#
# [870] Advantage Shuffle
#

# @lc code=start
from typing import List 
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)

        nums1.sort() 

        indices = sorted(range(n), key=lambda i: nums2[i], reverse=True) # 将num2数组按照从大到小进行排序

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
    


# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n[1,10,4,11]\n
# @lcpr case=end

# @lcpr case=start
# [12,24,8,32]\n[13,25,32,11]\n
# @lcpr case=end

#

