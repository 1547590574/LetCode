class Solution:
    # 26进制没有26，所以每次开头减一，这样每次循环时候就将0去掉，也就是上一个位置上的26去掉
    # 本题相当于转化为26进制，用0表示A，25表示Z，正好26个
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        while columnNumber:
            columnNumber -= 1
            result += chr(columnNumber % 26 + ord('A'))
            columnNumber //= 26
        return result[::-1]


s = Solution()
print(s.convertToTitle(2147483647))
