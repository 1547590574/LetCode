# <---coding: utf-8--->
# @Time:  2022/3/26/21:56
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for num, item in enumerate(ops):
            if item == 'C':
                res.pop()
            elif item == 'D':
                res.append(res[-1] * 2)
            elif item == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(item))
        return sum(res)


s = Solution()
print(s.calPoints(["5","2","C","D","+"]))