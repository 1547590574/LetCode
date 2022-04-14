# <---coding: utf-8--->
# @Time:  2022/3/14/16:38
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = 1
        while a <= num / a:
            if a == num / a:
                return True
            else:
                a += 1
        return False


s = Solution()
print(s.isPerfectSquare(16))