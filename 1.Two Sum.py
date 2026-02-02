#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30307
#
# [1] Two Sum
#
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = []
        for i, j in enumerate(nums):
            for k, h in enumerate(nums[1:]):
                if j + h == target:
                    return i, k 
                else:
                    return None 
                
        num_map.append(i)
        num_map.append(k)


# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

