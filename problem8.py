# <---coding: utf-8--->
# @Time:  2022/4/25/15:27
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def myAtoi(self, s: str) -> int:
        low, high = -2**31, 2**31 -1
        s = s.strip()
        if not s:
            return 0
        i, flag = 0, 1
        res = 0
        if s[0] in '-+':
            flag = 1 if s[0] == '+' else -1
            i += 1
        while i < len(s):
            if s[i] <'0' or s[i] > '9':
                break
            res = 10*res+int(s[i])
            i += 1
            if res*flag < low:
                return low
            elif res*flag > high:
                return high
        return res*flag


s = Solution()
print(s.myAtoi('42'))

