# <---coding: utf-8--->
# @Time:  2022/3/18/21:48
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        map = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        group = [map[int(_)] for _ in digits]
        print()
        print(*group)
        return [''.join(com)  for com in itertools.product(item for item in group)]


s = Solution()
print(s.letterCombinations('23'))