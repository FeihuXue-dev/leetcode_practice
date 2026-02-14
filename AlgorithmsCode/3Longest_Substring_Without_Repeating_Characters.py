"""
无重复字符串的最长字串
解法：
    滑动窗口
"""

class Solution:
    def FindAnagram(self, s:str) -> int:
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

            res = max(res, right - left)

        return res


s = "abcabcbb"

Sol = Solution()
result = Sol.FindAnagram(s)
print(result)
