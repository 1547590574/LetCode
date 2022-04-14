# <---coding: utf-8--->
# @Time:  2022/4/13/0:19
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line, res = 0, 1
        for index, item in enumerate(s):
            if line <= 100:
                line += widths[ord(item) - ord('a')]
            if line > 100:
                res += 1
                line = widths[ord(item) - ord('a')]
        return [res, line]


s = Solution()
A = s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa")
print(A)