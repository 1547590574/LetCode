# <---coding: utf-8--->
# @Time:  2022/3/14/17:17
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        map = {id:x for id, x in enumerate(nums)}
        pass


s = Solution()
s.thirdMax([2, 2, 3, 1])