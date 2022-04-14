# <---coding: utf-8--->
# @Time:  2021/12/30/15:34
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        oc = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i !=0:
                oc.remove(s[i - 1])
            while rk + 1 < n and s[rk +1] not in oc:
                oc.add(s[rk + 1])
                rk += 1
            ans =max(ans, rk - i + 1)
        return ans
