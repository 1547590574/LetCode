from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            # 在n位置存储前n-1项最大和。有负值会被0弄掉的
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
