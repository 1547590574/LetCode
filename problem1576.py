# <---coding: utf-8--->
# @Time:  2022/1/6/0:13
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import random


class Solution:
    def modifyString(self, s: str) -> str:
        res = list(s)
        n = len(res)
        for i in range(n):
            if res[i] == '?':
                for b in "abc":
                    if not (i > 0 and res[i - 1] == b or i < n - 1 and res[i + 1] == b):
                        res[i] = b
                        break
        return ''.join(res)
