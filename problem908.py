# <---coding: utf-8--->
# @Time:  2022/4/30/0:17
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import random
from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        res = max(nums) - min(nums) -2*k
        return max(0, res)