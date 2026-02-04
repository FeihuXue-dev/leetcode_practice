"""反转数组
解法：
    双指针，左右分别一个指针
"""
from typing import List
def reverseString(s:List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp

        left += 1
        right -= 1
