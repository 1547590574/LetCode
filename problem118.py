# <---coding: utf-8--->
# @Time:  2021/12/31/13:49
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(len(ans[i - 1]) - 1):
                temp.append(ans[i - 1][j] + ans[i - 1][j + 1])
            temp.append(1)
            ans.append(temp)
        return ans


s = Solution()
print(s.generate(4))
