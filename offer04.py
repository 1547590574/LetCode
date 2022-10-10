# <---coding: utf-8--->
# @Time:  2022/10/10/22:22
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        i, j = 0, n-1
        while i < m and j >=0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            if matrix[i][j] < target:
                i += 1
        return False

s = Solution()
print(s.findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],20))