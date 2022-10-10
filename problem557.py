# <---coding: utf-8--->
# @Time:  2022/5/7/20:28
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ''
        for item in s.split(' '):
            i = list(item)
            res += ''.join(i[::-1]) + ' '
        return res[:-1]
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))