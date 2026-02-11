#
# @lc app=leetcode id=5 lang=python3
# @lcpr version=30307
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            s1 = self.Palindrome(s, i, i)
            s2  = self.Palindrome(s, i, i+1)

            res = res if len(res) > len(s1) else s1 
            res = res if len(res) > len(s2) else s2 
            
        return res 

    def Palindrome(self, s:str, l:int, r:int) -> str:
        
        while l >= 0  and r < len(s) and s[l] == s[r]:
             l -= 1
             r += 1 

        return s[l+1: r]
    
        
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

