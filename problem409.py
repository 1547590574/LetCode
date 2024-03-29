# <---coding: utf-8--->
# @Time:  2022/5/5/23:36
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans



s = Solution()
print(s.longestPalindrome("abccccdd"))