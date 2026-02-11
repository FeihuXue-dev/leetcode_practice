#
# @lc app=leetcode id=76 lang=python3
# @lcpr version=30307
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {} 

        for c in t:
            need[c] = need.get(c, 0) + 1 

        left = 0 
        right = 0 
        valid = 0 
        start = 0 
        length = float('inf')

        while right < len(s):
            c = s[right]
            right += 1 

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left 
                    length = right - left 

                d = s[left]

                left += 1 

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1

                    window[d] -= 1 

        return "" if length == float('inf') else s[start: start + length]

# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

