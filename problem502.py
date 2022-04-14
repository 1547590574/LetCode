# <---coding: utf-8--->
# @Time:  2021/12/31/0:14
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        ans = [1]
        a = int(math.sqrt(num))
        for i in range(2,a + 1):
            if num % i == 0:
                ans.append(i)
                ans.append(num // i)
        print(ans)
        if sum(ans) == num:
            return True
        return False

s = Solution()
print(s.checkPerfectNumber(28))