# <---coding: utf-8--->
# @Time:  2022/4/19/15:41
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        map = {}
        for i, j in enumerate(s):
            map[j] = map[j] + 1 if j in map.keys() else 1
        for
        return 0