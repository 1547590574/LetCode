# <---coding: utf-8--->
# @Time:  2022/1/4/23:52
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1)
            n //= 2
        return ans

s =Solution()
