# <---coding: utf-8--->
# @Time:  2022/1/1/0:49
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import re

#这里用个正则表达式就行，顺便了解一下python自带的一些算法

class Solution:
    def isPalindrome(self, s: str) -> bool:
        reslut = ''.join(re.findall(r'[A-Za-z0-9]',s)).lower()
        n = len(reslut)
        for i in range(n):
            if reslut[i] != reslut[n - 1 - i]:
                return False
        return True
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))