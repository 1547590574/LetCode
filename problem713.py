# <---coding: utf-8--->
# @Time:  2022/5/5/20:26
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 参考全站27的写法， 设计一个滑动窗口
        left, res, count = 0, 1, 0
        for right, item in enumerate(nums):
            res *= item
            # 窗口开始滑动，只有当前乘积大于k时才滑动，窗口的左边界右移，乘积变小
            while left <= right and res >= k:
                res /= nums[left]
                left += 1
            # 这里只要这个长度满足，那么它的子串都满足，长度等于1的子串，因为大于1的在后面会被重新统计
            count += right - left + 1
        return count

s = Solution()
print(s.numSubarrayProductLessThanK([10,5,2,6],100))