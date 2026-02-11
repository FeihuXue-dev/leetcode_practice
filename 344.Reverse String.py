#
# @lc app=leetcode id=344 lang=python3
# @lcpr version=30307
#
# [344] Reverse String
#

# @lc code=start
from typing import List 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1 

        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp 

            left += 1 
            right -= 1
            

        
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

