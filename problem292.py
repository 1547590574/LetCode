# <---coding: utf-8--->
# @Time:  2022/2/25/10:36
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    # 其实叫巴什博弈更正确，因为这是石子堆数等于1的特殊情况
    def canWinNim(self, n: int) -> bool:
        return n % 4 == 0