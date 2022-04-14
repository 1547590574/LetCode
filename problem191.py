# <---coding: utf-8--->
# @Time:  2022/2/23/10:32
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = sum(1 for i in range(32) if n&(1<<i))
        return res



s = Solution()
