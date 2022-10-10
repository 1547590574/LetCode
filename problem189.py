# <---coding: utf-8--->
# @Time:  2022/5/5/15:05
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from collections import deque

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #  原地赋值需要[:]这样哦,而且要考虑到k比n大的情况，先取余
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)
a = [1,2,3,4,5,6,7]
print(a[:])