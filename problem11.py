# <---coding: utf-8--->
# @Time:  2022/5/5/21:32
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max((right - left) * min(height[left], height[right]),area)
            print(area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area

s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])