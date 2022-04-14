# <---coding: utf-8--->
# @Time:  2022/3/26/23:33
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n and n % 3 == 0:
            n //= 3
        return n == 1

