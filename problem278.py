# <---coding: utf-8--->
# @Time:  2022/5/4/21:43
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def isBadVersion(version) -> bool:
        return True

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left