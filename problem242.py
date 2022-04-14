# <---coding: utf-8--->
# @Time:  2022/2/25/10:56
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = len(s), len(t)
        if a != b:
            return False
        res = 0
        for i in range(a):
            print(s[i])
            res ^= (ord(s[i]) ^ ord(t[i]))
        return res == 0


s = Solution()
s.isAnagram("anagram", "nagaram")