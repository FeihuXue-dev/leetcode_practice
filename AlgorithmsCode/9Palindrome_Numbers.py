"""判断某个数字是否是回文数
解法：
    双指针
"""

def PalindromeNumber(x:int) -> bool:
    if x < 0:
        return False

    s = str(x)
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

x = 121

result = PalindromeNumber(x)
print(result)
