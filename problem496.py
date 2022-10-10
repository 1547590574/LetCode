# <---coding: utf-8--->
# @Time:  2022/5/5/22:32
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        for i, item in enumerate(nums2):
            for j, jtem in enumerate(nums1):
