# <---coding: utf-8--->
# @Time:  2022/1/4/17:57
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[right] + numbers[left] == target:
                return [left + 1, right + 1]
            elif numbers[right] + numbers[left] < target:
                left += 1
            else:
                right -= 1
        return []


s = Solution()
print(s.twoSum([2,3,4],6))
