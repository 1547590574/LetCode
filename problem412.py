# <---coding: utf-8--->
# @Time:  2022/3/14/16:30
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0 and not i % 5 == 0:
                res.append('Fizz')
            elif not i % 3 == 0 and i % 5 == 0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


s = Solution()
print(s.fizzBuzz(5))