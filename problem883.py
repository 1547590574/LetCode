# <---coding: utf-8--->
# @Time:  2022/4/26/9:18
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area_xy, area_xz, area_yz = 0, 0, 0
        for i, j in enumerate(grid):
            if j != 0:
                area_xy += 1
            
        return []


s = Solution()
print()