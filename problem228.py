# <---coding: utf-8--->
# @Time:  2022/4/24/18:12
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 1:
            return ['' + nums[0]]
        else:
            i, j = 0, 1
            while j < len(nums):
                if nums[j] == nums[i] + 1:
                    j += 1
                    