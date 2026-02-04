"""寻找最小覆盖字串
解法：
    滑动窗口
"""
def minimumWindowSubstring(s:str, t:str) -> str:
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

            #窗口左边进行滑动
            d = s[left]
            left += 1

            if d in need:
                if window[d] == need[d]:
                    valid -= 1

                window[d] -= 1

    return "" if length == float('inf') else s[start:start+length]

s = "ADOBECODEBANC"
t = "ABC"

result = minimumWindowSubstring(s, t)
print(result)
