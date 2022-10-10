# <---coding: utf-8--->
# @Time:  2022/5/5/20:57
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        def getNums(n: str) -> int:
            res = 0
            for i in n:
                res += int(i)**2
            return res
        x = []
        while n not in x:
            print(x)
            x.append(n)
            n = getNums(str(n))
            if n == 1:
                return True
        return False

s = Solution()
print(s.isHappy(19))