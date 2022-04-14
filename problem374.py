# <---coding: utf-8--->
# @Time:  2022/3/18/23:03
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            mid = (start + end) // 2
            if guess(mid) == -1:
                end = mid - 1
            elif guess(mid) == 1:
                start = mid + 1
            elif guess(mid) == 0:
                return mid 

