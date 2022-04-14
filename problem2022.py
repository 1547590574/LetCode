# <---coding: utf-8--->
# @Time:  2022/1/1/0:16
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        length = len(original)
        ans = []
        if length != m * n:
            return ans
        for i in range(m):
            ans.append(original[i * n:i * n + n])
        return ans

s = Solution()
print(s.construct2DArray([1, 1, 1, 1], 4, 1))
