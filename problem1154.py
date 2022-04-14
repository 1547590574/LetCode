class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        framgent = date.split('-')
        if int(framgent[0]) % 4 == 0 and int(framgent[0]) % 100 != 0 or int(framgent[0]) % 400 == 0:
            days[1] = 29
        else:
            days[1] = 28
        ans = 0
        for i in range(int(framgent[1])-1):
            ans += days[i]
        return ans + int(framgent[2])

s = Solution()
print(s.dayOfYear('2003-03-01'))
