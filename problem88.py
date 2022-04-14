from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 当一个数组被放完时，一定会有一个下标到达-1 ，因为0是可以被放的，放了会减一，为了避免这时候减一发生越界，所以设置单独的p 或 q等于-1时应该单独放一个数组剩下的元素，此时相当只有一个素组在放，因为要放完所以设置条件一定时大于等于0，当nums1和nums2元素相等时放在哪不重要。
        p = m - 1
        q = n - 1
        index = m + n - 1
        while p >= 0 or q >= 0:
            if p == -1:
                nums1[index] = nums2[q]
                q -= 1
            elif q == -1:
                nums1[index] = nums1[p]
                p -= 1
            elif nums1[p] > nums2[q]:
                nums1[index] = nums1[p]
                p -= 1
            elif nums1[p] <= nums2[q]:
                nums1[index] = nums2[q]
                q -= 1
            index -= 1
            print(index)


s = Solution()
s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
