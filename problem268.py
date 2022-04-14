# <---coding: utf-8--->
# @Time:  2022/3/14/11:54
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ak = [-1] * (n+1)
        for item in nums:
            ak[item] = item
        print(ak)
        for i in range(n+1):
            if ak[i] == -1:
                return i


s =Solution()
print(s.missingNumber([0,1]))