# <---coding: utf-8--->
# @Time:  2022/4/25/10:33
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
import random
from collections import defaultdict
class Solution:
    def __init__(self, nums: List[int]):
        self.map = defaultdict(list)
        for key, value in enumerate(nums):
            self.map[value].append(key)

    def pick(self, target: int) -> int:
        return random.choice(self.map[target])


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,3,3]
obj = Solution(nums)
param_1 = obj.pick(3)