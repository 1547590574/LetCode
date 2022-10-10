# <---coding: utf-8--->
# @Time:  2022/3/14/17:17
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        heapq.heapify(nums)
        print(nums)
        return heapq.nlargest(3,nums)[2]


s = Solution()
print(s.thirdMax([2, 2, 3, 1]))