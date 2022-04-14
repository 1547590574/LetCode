# <---coding: utf-8--->
# @Time:  2022/1/1/21:28
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1,len(nums)-1):
            ans ^= nums[i]
        return ans

s = Solution()
print(s.singleNumber([4,1,2,1,2]))