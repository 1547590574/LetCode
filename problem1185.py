# <---coding: utf-8--->
# @Time:  2022/1/3/9:50
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
# 蔡勒公式 记住年份也要跟着减一 然后算c的时候先算，不然会被2被扩大余数，导致+1。
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        if month < 3:
            month += 12
            year -= 1
        c = year // 100
        y = year % 100
        w = (c // 4 - 2 * c + y + y // 4 + 13 * (month + 1) // 5 + day - 1 + 210) % 7
        return week[w]

s = Solution()
print(s.dayOfTheWeek(31, 8, 2019))
