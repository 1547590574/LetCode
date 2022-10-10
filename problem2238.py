# <---coding: utf-8--->
# @Time:  2022/10/10/12:08
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        length = len(energy)
        n, hours = 0, 0
        while n < length:
            if initialExperience <= experience[n]:
                temp = experience[n]-initialExperience + 1
                initialExperience += temp
                hours += temp
            if initialEnergy <= energy[n]:
                temp = energy[n] - initialEnergy + 1
                initialEnergy += temp
                hours += temp
            if initialExperience > experience[n] and initialEnergy > energy[n]:
                initialExperience += experience[n]
                initialEnergy -= energy[n]
            n += 1
        return hours


s = Solution()
print(s.minNumberOfHours(5,3,[1,4,3,2],[2,6,3,1]))