# <---coding: utf-8--->
# @Time:  2022/2/25/9:56
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n % 5 == 0:
            n /= 5
        while n % 3 == 0:
            n /= 3
        while n % 2 == 0:
            n /= 2
        return n == 1


s = Solution()
s.isUgly(0)