# <---coding: utf-8--->
# @Time:  2022/2/25/9:34
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        else:
            while n / 2 != 1:
                n /= 2
                if n == 0:
                    return False
        return True

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         return n > 0 and n & (n - 1) == 0

