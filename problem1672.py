# <---coding: utf-8--->
# @Time:  2022/4/14/11:16
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        weathly = -1
        for people in accounts:
            weathly = sum(people) if sum(people) > weathly else weathly
        return  weathly

s = Solution()
print(s.maximumWealth([[1,2,3],[3,2,1]]))