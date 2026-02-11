#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30307
#
# [1] Two Sum
#
from typing import List
from operator import itemgetter
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums_with_index = sorted(enumerate(nums), key=lambda x: x[1])
        nums_with_index = sorted(enumerate(nums), key=itemgetter(1))

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

