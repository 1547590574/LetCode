from typing import List


class Solution:
    # 上面的方法是自己写的，用了逆向索引表，耗费的时间代价和空间代价都比较大，时间上用了pop方法（消耗比较大），空间上用了一个repeat方法记录重复元素。下面的方法直接快慢双指针，没有空间代价，而且直接赋值元素，所以没有移动元素的代价
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        repeat = []
        count = 0
        while count < len(nums):
            if nums[count] not in repeat:
                repeat.append(nums[count])
            else:
                nums.pop(count)
                count -= 1
            count += 1
        print(nums)
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        fast = slow = 1
        while fast < n:
            print(nums)
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        print(nums)
        return slow


s = Solution()
a = [1, 1, 2, 2, 3, 3]
print(s.removeDuplicates(a))
