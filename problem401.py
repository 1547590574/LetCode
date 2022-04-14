# <---coding: utf-8--->
# @Time:  2022/3/14/14:51
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
import itertools as it


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    res.append(f"{i}:{j:02d}")

        return res


s = Solution()
print(s.readBinaryWatch(3))