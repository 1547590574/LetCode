# <---coding: utf-8--->
# @Time:  2021/12/31/14:09
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
from scipy.special import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex):
            ans.append(int(comb(rowIndex,i)))
        ans.append(1)
        return ans

s = Solution()
print(s.getRow(3))