#
# @lc app=leetcode id=567 lang=python3
# @lcpr version=30307
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = {}, {} 

        for a in s1:
            need[a] = need.get(a, 0) + 1

        left = 0 
        right = 0 
        valid = 0

        while right < len(s2):
            r = s2[right]
            right += 1 
            if r in need:
                window[r] = window.get(r, 0) + 1 
                if window[r] == need[r]:
                    valid += 1 

            while right - left >= len(s1):
                if valid == len(need):
                    return True 
                
                l = s2[left]
                left += 1 

                if l in need:
                    if window[l] == need[l]:
                        valid -= 1 

                    window[l] -= 1

        return False

# @lc code=end



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

