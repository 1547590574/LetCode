# <---coding: utf-8--->
# @Time:  2022/5/8/1:17
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        return [key for key in count if count[key] == 2]


s = Solution()
print(s.findDuplicates([4,3,2,7,8,2,3,1]))