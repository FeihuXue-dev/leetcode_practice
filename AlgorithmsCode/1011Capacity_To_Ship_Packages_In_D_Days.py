"""
在规定的时间内，将传送带上带有权重的快递运送到船上。已有的快递为weights数组，含有i个数字，每个数字代表第i个快递的权重。寻找到合适的每船的权重确保刚好在规定的时间内将所有货物传送到船上。
解法：
    二分法
"""

from typing import List, Optional


class Solution:
    def shipWithDays(self, weights: List[int], days: int) -> Optional[int]:
        left = max(weights)
        right = sum(weights)

        res = right

        while left <= right:
            mid = left + (right - left) // 2

            current_weights = 0
            total_days = 1

            for w in weights:

                if current_weights + w > mid:
                    total_days += 1
                    current_weights = 0

                current_weights = current_weights + w

            if total_days <= days:
                res = mid
                right = mid - 1

            else:
                left = mid + 1

        return res

weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

Sol = Solution()
results = Sol.shipWithDays(weights, days)
print(results)
