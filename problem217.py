# <---coding: utf-8--->
# @Time:  2022/2/25/9:31
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for i in nums:
            if i in set1:
                return True
            else:
                set1.add(i)
        return False