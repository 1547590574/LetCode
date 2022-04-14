# <---coding: utf-8--->
# @Time:  2022/1/4/19:06
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for x in columnTitle:
            ans *= 26
            ans += ord(x) - ord('A') + 1
        return ans