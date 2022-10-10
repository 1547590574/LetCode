# <---coding: utf-8--->
# @Time:  2022/5/5/22:06
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        border, land = 0, 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    land += 1
                    if j < col - 1 and grid[i][j + 1]:
                        border += 1
                    if i < row - 1 and grid[i + 1][j]:
                        border += 1

        return 4 * land - 2 * border

s = Solution()
print(s.islandPerimeter([[1,0]]))
