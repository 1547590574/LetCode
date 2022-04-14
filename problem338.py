# <---coding: utf-8--->
# @Time:  2022/3/26/23:24
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res


s = Solution()
print(s.countBits(2))