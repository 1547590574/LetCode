from typing import List
import heapq


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # 介绍一种优先队列的数据结构，为了每次吃到最不新鲜的苹果，同样不用考虑两个同样新鲜度的苹果的排放顺序
        # 因为不知道怎么改队中数据的优先级，所以这里用绝对优先级，就是直接放入苹果能保存到的天数，而不是距离今天还有几天过期
        h = []
        ans = 0
        i = 0
        n = len(apples)
        while i < n:
            while h and h[0][0] <= i:
                heapq.heappop(h)
            if apples[i]:
                heapq.heappush(h, [i + days[i], apples[i]])
            if h:
                h[0][1] -= 1
                if h[0][1] == 0:
                    heapq.heappop(h)
                ans += 1
            i += 1
        print(h, ans)
        while h:
            while h and h[0][0] <= i:
                heapq.heappop(h)
            if len(h) == 0:
                return ans
        # 这里可以一天一天的模拟，也可以直接求和
            if h:
                h[0][1] -= 1
                if h[0][1] == 0:
                    heapq.heappop(h)
                ans += 1
            i += 1
        return ans

s=Solution()
print(s.eatenApples([1,2,3,5,2],[3,2,1,4,2]))