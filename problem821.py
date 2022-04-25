# <---coding: utf-8--->
# @Time:  2022/4/19/14:16
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        position = [i for i in range(len(s)) if s[i] == c]
        print(position)
        res = []
        for i in range(len(s)):
            max_index = len(s) + 1
            for j in range(len(position)):
                min_index = min(max_index,abs(i-position[j]))
                max_index = min_index
            res.append(min_index)
        return res

s = Solution()
print(s.shortestToChar("loveleetcode","e"))