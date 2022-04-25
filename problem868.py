# <---coding: utf-8--->
# @Time:  2022/4/24/10:05
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# and str(int(str1[0:i + 1], 2) ^ (2 ** (i+1) - 1)).count('1') != 0
class Solution:
    def binaryGap(self, n: int) -> int:
        str1= bin(n)[2::]
        pos = len(str1) - 1
        while str1[pos] != '1':
            pos -= 1
        if pos == 0:
            return 0
        str1 = str1[:pos+1]
        num = str1.count('0')
        res = 0
        for i in range(1, num + 1):
            if str1.count(i * '0') == 0:
                break
            else:
                res = i
        return res+1

s = Solution()
print(s.binaryGap(22))
