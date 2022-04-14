# <---coding: utf-8--->
# @Time:  2021/12/30/16:21
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

class Solution:
    def KMP(self,string: str, substring: str) -> int:
        pnext = self.get_next(substring)
        n, m, i, j =len(string), len(substring),0 ,0
        while i < n and j < m:
            if string[i] == substring[j]:
                i += 1
                j += 1
            elif j != 0:
                j = pnext[j - 1]
            else:
                i += 1
        if j == m:
            return i - j
        else:
            return -1
        return -1

    def get_next(self,substring: str) -> list[int]:
        index, n = 0, len(substring)
        pnext = [0] * n
        i = 1
        while i < n:
            if substring[i] == substring[index]:
                pnext[i] = index + 1
                i += 1
            elif index != 0:
                index = pnext[index - 1]
            else:
                pnext[i] == 0
                i += 1
        return pnext