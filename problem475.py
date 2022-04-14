from bisect import *
from typing import List


class Solution:
    # def findRadius(self, houses: List[int], heaters: List[int]) -> int:
    #     m = len(heaters)
    #     houses.sort()
    #     n = len(houses)
    #     heaters.sort()
    #     minValue = abs(houses[0] - heaters[0])
    #     i, j = 1, 0
    #     while i < n:
    #         minV = abs(houses[i] - heaters[j])
    #         while j+1 < m:
    #             value = abs(houses[i] - heaters[j])
    #             minV=min(minV,value)
    #             j += 1
    #         j-=1
    #         minValue = max(minValue, minV)
    #         i += 1
    #     return minValue
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        raduis = 0
        heaters.sort()
        n = len(heaters)
        for i in houses:
            # 这是在网上找的一个方法，左插右插是一样的，只是遇到相同值的不同表现，这里left和right遇到相同值只是表现在right_distance为0还是left_distance为0，另外考虑出界的情况，插到边上有一边距离为无穷大，此时取min会自动忽略掉该值。
            # 相比于以上方法，该方法的复杂度小了，不用全遍历，n^2会超时
            index = bisect_left(heaters, i)
            right_distance = heaters[index] - i if index < n else float('inf')
            left_distance = i - heaters[index - 1] if index - 1 >= 0 else float('inf')
            raduis = max(raduis, min(right_distance, left_distance))
        return raduis


s = Solution()
print(s.findRadius([1, 5], [10]))
