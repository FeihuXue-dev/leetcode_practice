"""移除非严格排序数组中的重复数字
解法：
    采用链表中使用的快慢指针的方式移除原有数组中的重复数字
    slow 负责记录那些是非重复的，fast负责判断那些是与slow中重复的，并移除
    只需要返回slow指针下记录的非重复数字的长度
"""

from typing import List, Optional

def removeDuplicates(self, nums:List[int]) -> Optional[int]:
    if len(nums) == 0:
        return 0

    slow = 0
    fast = 0
