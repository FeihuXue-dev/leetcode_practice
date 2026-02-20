#
# @lc app=leetcode id=528 lang=python3
# @lcpr version=30400
#
# [528] Random Pick with Weight
#

# @lc code=start

from typing import List
import random 
class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = [] 
        current_sums = 0 

        for weight in w:
            current_sums += weight 
            self.prefix_sums.append(current_sums)

        self.total_sums = current_sums

    def pickIndex(self) -> int:
        
        target = random.randint(1, self.total_sums)

        left = 0 
        right = len(self.prefix_sums)

        ans = -1 

        while left <= right:
            mid = left + (right - left) // 2 

            if self.prefix_sums[mid] >= target:
                ans = mid 
                right = mid - 1 

            else:
                left = mid + 1 

        return ans 
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end



#
# @lcpr case=start
# ["Solution","pickIndex"]\n[[[1]],[]]\n["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]\n[[[1,3]],[],[],[],[],[]]\n
# @lcpr case=end

#

