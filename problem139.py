# <---coding: utf-8--->
# @Time:  2022/5/4/22:14
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if not s:
                return True
            res = False
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)


# 这题的另一个解法，比较常规的动态规划。
# dp[i] 表示字符串的前i为能够被wordDoct表示, 只有前i-1位都能被表示并且i-j在worddict中，那么前i位也能被表示
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         dp = [True] + [False] * n
#         for i in range(n):
#             for j in range(i + 1, n + 1):
#                 if dp[i] and (s[i:j] in wordDict):
#                     dp[j] = True
#         return dp[-1]


s = Solution()
print(s.wordBreak("applepenapple", ["apple", "pen"]))
