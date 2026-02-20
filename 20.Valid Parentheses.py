#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=30307
#
# [20] Valid Parentheses
#

# @lc code=start
"""栈是一种先进后出的数据结构。在此问题中，最后出现的左括号必须被最先被匹配，符号栈的后进先出的特性"""
class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {")":"(", "}":"{", "]":"["}

        stack = [] 

        for char in s:
            if char in mappings:
                top_element = stack.pop()  if stack else '#'

                if mappings[char] != top_element:
                    return False 
                
            else:
                stack.append(char)

        return not stack 
        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

