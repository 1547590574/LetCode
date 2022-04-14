# <---coding: utf-8--->
# @Time:  2022/2/25/10:01
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i, num in enumerate(nums):
            if num in map and i - map[num] <= k:
                return True
            map[num] = i
        return False

# 类似与倒排索引，将数值放在key位，索引放在value，因为是map所以速度很快，另外 if条件中的后一部分判断很精妙，直接覆盖原本可能超过k位的空间，不用一直去清空。此外学会enumerate的用法，比单纯的range要好一点。
