# <---coding: utf-8--->
# @Time:  2022/1/2/0:40
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def lastRemaining(self, n: int) -> int:
        remain = n
        flag = True
        res = 1
        step = 1
        while remain > 1:
            # 当左到右 或者剩余个数为奇数
            if flag or remain % 2 == 1:
                res += step
            flag = not flag
            step *= 2
            remain //= 2
        return res