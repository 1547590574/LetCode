from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        nums = []
        for i in digits:
            ans = ans * 10 +i
        ans += 1
        for i in str(ans):
            nums.append(int(i))
        return nums

s=Solution()
print(s.plusOne([4,3,2,1]))