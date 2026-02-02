#
# @lc app=leetcode id=13 lang=python3
# @lcpr version=30307
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s:str) -> int:
        roman_number_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        total = 0
        present_value = 0
        for char in s[::-1]:
            value = roman_number_dict[char]
            if value < present_value:
                total = total - value
            else:
                total = total + value

            present_value = value

        return total
        
# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

