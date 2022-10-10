# <---coding: utf-8--->
# @Time:  2022/10/9/23:46
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        i, j = 0, len(s) - 1
        a = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
        while 0 <= i < j < len(s):
            if s[i] not in a:
                i += 1
            elif s[j] not in a:
                j -= 1
            else:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return ''.join(res)


s1 = Solution()
print(s1.reverseVowels('hello'))
