# <---coding: utf-8--->
# @Time:  2022/3/14/11:38
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        while 1:
            while num!=0:
                res += num % 10
                num //= 10
            if res > 9:
                num = res
                res = 0
            else:
                return res

s = Solution()
print(s.addDigits(38))