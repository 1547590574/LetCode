# <---coding: utf-8--->
# @Time:  2022/10/10/13:43
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        s_length, struct_size = len(s), 2 * numRows - 2
        cols = (s_length // struct_size + 1) * (numRows - 1)
        m = [['']*cols for _ in range(numRows)]
        for i in range(s_length):
            temp1, temp2 = i // struct_size , i % struct_size
            if temp2 < numRows:
                m[temp2][temp1*numRows - temp1] = s[i]
            else:
                m[struct_size - temp2 ][temp1*numRows - temp1 + 1 + temp2 - numRows] = s[i]
        res = []
        for i in range(numRows):
            res.append(''.join(m[i]))
        return ''.join(res)

s = Solution()
s.convert("ABCDE",2)