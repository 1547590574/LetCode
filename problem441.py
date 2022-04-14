# <---coding: utf-8--->
# @Time:  2022/3/18/22:49
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2 * n + 0.25) ** 0.5 - 0.5)


s = Solution()
print(s.arrangeCoins(5))
