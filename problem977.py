# <---coding: utf-8--->
# @Time:  2022/5/5/14:43
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i, item in enumerate(nums):
            res.append(item**2)
        res.sort()
        return res