# <---coding: utf-8--->
# @Time:  2021/12/27/16:01
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        num = 0
        for i in range(len(ages)):
            for j in range(0, len(ages)):
                if j == i :
                    continue
                if not (ages[j] <= 0.5 * ages[i] + 7 or ages[j] > ages[i] or (ages[j] > 100 and ages[i] < 100)):
                    num += 1
        return num


s = Solution()
print(s.numFriendRequests([16, 17,18]))
