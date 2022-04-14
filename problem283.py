# <---coding: utf-8--->
# @Time:  2022/3/14/12:51
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i, j = 0, 0
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

s = Solution()
s.moveZeroes([0,1,0,3,12])