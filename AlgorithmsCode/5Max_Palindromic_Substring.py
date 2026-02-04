"""
寻找字符串中的最大子字符串
解法：
    双指针 + 分类讨论（子字符串为偶数或奇数）
"""

class Solution:
    def longestPalindrome(self, s:str) -> str:
        res = ""

        for i in range(len(s)):
            s1 = self.Palindrome(s, i, i)
            s2 = self.Palindrome(s, i, i+1)

            res = res if len(res) > len(s1) else s1

            res = res if len(res) > len(s2) else s2

        return res

    def Palindrome(self, s:str, l:int, r:int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l+1:r]

s = "babad"
Sol = Solution()
result = Sol.longestPalindrome(s)
print(result)
