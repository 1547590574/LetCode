# <---coding: utf-8--->
# @Time:  2021/12/30/18:37
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize !=0:
            return False
        hand.sort()
        # Counter方法用于统计数组中每个元素出现的次数，返回值是一个字典(只是可以通过字典形式索引),类似于逆文档频率，在collection中自带的方法。
        cnt = Counter(hand)
        print(type(cnt))
        for x in hand:
            if cnt[x] == 0:
                continue
            for num in range(x, x + groupSize):       # 这里用for循环完成公差为1的等差数列验证
                if cnt[num] == 0:
                    return False
                cnt[num] -= 1
        return True

s = Solution()
print(s.isNStraightHand([8,10,12],3))