# <---coding: utf-8--->
# @Time:  2022/3/27/21:14
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        a = mean * (n + len(rolls)) - sum(rolls)
        if not n <= a <= 6 * n:
            return []
        quotient, remainder = divmod(a, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)

