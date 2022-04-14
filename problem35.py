from typing import List


class Solution:
    # 二分查找的变式
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # if target <= nums[0]:
        #     return left
        # if target >= nums[-1]:
        #     return right+1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return right + 1
    # 据评论区说，返回right + 1 和 left 是一样的， 试了一下真可以


s = Solution()
print(s.searchInsert([1, 3], 2))
