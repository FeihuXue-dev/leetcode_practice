#
# @lc app=leetcode id=3 lang=python3
# @lcpr version=30307
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        left = 0 
        right = 0 

        res = 0 

        while right < len(s):
            c = s[right]
            right += 1 

            window[c] = window.get(c, 0) + 1 

            while window[c] > 1:
                d = s[left]
                left += 1 
                window[d] = window.get(d, 0) - 1 

            res = max(res, right-left)

        return res 

                



        
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

