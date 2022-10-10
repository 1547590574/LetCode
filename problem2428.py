# <---coding: utf-8--->
# @Time:  2022/10/10/17:01
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        s=[[0]*(n+1) for j in range(m+1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = grid[i - 1][j - 1] + s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1]
        ans = -1
        for i in range(3,m+1):
            for j in range(3,n+1):
                ans = max(ans,s[i][j]-s[i-3][j]-s[i][j-3]+s[i-3][j-3]-grid[i-2][j-1]-grid[i-2][j-3])
        return ans

s = Solution()
ans = s.maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]])
print(ans)