#
# @lc app=leetcode id=9 lang=python3
# @lcpr version=30307
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False 
        
        s = str(x)
        left, right = 0, len(s) - 1 

        while left < right:
            if s[left] != s[right]:
                return False 
            left += 1 
            right -= 1 

        return True 
        
# @lc code=end



#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

