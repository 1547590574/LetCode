# <---coding: utf-8--->
# @Time:  2022/1/2/23:34
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        number = None
        for i in range(0, len(nums)):
            if count == 0:
                number = nums[i]
            count += (1 if nums[i] == number else -1)
        return number


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1]))
