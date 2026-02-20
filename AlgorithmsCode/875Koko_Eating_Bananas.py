"""
Koko吃香蕉的问题。香蕉分为i堆，每堆有piles[i]个香蕉。Koko每小时可以吃k个香蕉。首先Koko先吃某一堆的k个香蕉，若此堆香蕉数量小于k，则吃完且该小时内不再吃香蕉。Koko希望慢点在规定的时间（h小时）内把香蕉吃完，请问k取多少？
解法：
    问题为在一个明确的范围内找到一个最值
    二分查找
"""

from typing import List, Optional

class Solution:
    def minEatingSpeed(self, piels:List[int], h:int) -> Optional[int]:
        pass
