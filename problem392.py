# <---coding: utf-8--->
# @Time:  2022/5/5/21:44
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len, t_len = len(s), len(t)
        i, j = 0, 0
        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == s_len

s = Solution()
print(s.isSubsequence('ace','abcde'))