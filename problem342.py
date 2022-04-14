# <---coding: utf-8--->
# @Time:  2022/3/14/14:42
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        res = 0
        while 4**res <= n:
            if 4**res == n:
                return True
            res += 1
        return False


s = Solution()
print(s.isPowerOfFour(1))