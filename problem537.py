# <---coding: utf-8--->
# @Time:  2022/2/25/9:07
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        s1 = num1.split('+')
        a, b = int(s1[0]), int(s1[1].split('i')[0])
        s2 = num2.split('+')
        c, d = int(s2[0]), int(s2[1].split('i')[0])
        number = a * c - b * d
        complex = a * d + b * c
        return '{}+{}i'.format(number, complex)


s = Solution()
s.complexNumberMultiply('1+2i', '1+2i')
