from typing import List


class Solution:
    # 0还是要判断一下的，这样快速结束，不然时间代价太大。 一前一后指针，前面遇到要扔掉的就等着让后面的动，后面遇到要除掉的就跳过，直到两个相碰
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] == val:
                # 这里会换两次，第一次换过来，发现i上面还是要去掉的元素，但是j已经过了那个val，会把新的再和这个交换一下。
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i


s = Solution()
a = s.removeElement([3, 2, 2, 3], 3)
print(a)
