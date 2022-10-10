# <---coding: utf-8--->
# @Time:  2022/5/9/23:19
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = [ord(x) - ord('a') for x in s1]
        b = [ord(x) - ord('a') for x in s2]
        for i, item in enumerate(b):
            if item in a:

        print(a)
        return True

s = Solution()
s.checkInclusion('eidbaooo','eidbaooo')


