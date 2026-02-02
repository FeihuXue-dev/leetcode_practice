"""移除数组中的重复元素，并返回移除后的数组长度
解法：
    使用快慢指针判断
"""

from typing import List, Optional

def removeElements(self, nums:List[int], val:Optional[int]) -> Optional[int]:
    if len(nums) == 0:
        return 0

    slow, fast = 0, 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1

        fast += 1

    return slow
