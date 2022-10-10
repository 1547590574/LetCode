# <---coding: utf-8--->
# @Time:  2022/4/24/18:12
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        res = []
        for i in nums:
            if len(res) == 0 or i == res[-1] + 1:
                res.append(i)
            else:
                if len(res) == 1:
                    r.append(f"{res[-1]}")
                else:
                    r.append(f"{res[0]}->{res[-1]}")
                res.clear()
                res.append(i)
        if len(res) == 1:
            r.append(f"{res[-1]}")
        if len(res) > 1:
            r.append(f"{res[0]}->{res[-1]}")
        return r

s = Solution()
r = s.summaryRanges([0,1,2,4,5,7])
print(r)