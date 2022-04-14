# <---coding: utf-8--->
# @Time:  2022/3/18/22:39
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[-1])
        for i in range(len(s)):
            res^=(ord(s[i])^ord(t[i]))
        return chr(res)

s = Solution()
print(s.findTheDifference('abc','adcb'))