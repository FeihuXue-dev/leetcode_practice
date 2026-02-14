"""
寻找字符串中所有字母的异位词
解法：
    滑动窗口
"""
from typing import List

class Solution:
    def FindAnagrams(self, s:str, p:str) -> List[int]:
        need = {}
        window = {}

        for c in p:
            need[c] = need.get(c, 0) + 1

        left = 0
        right = 0

        valid = 0

        res = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1

                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1

                    window[d] -= 1

        return res

strings = "cbaebabacd"

p = "abc"
Sol = Solution()
result = Sol.FindAnagrams(strings, p)
print(result)
