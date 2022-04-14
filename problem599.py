# <---coding: utf-8--->
# @Time:  2022/3/14/9:40
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = 2001
        res = []
        index1 = {list1[i]: i for i in range(len(list1))}
        for i in range(len(list2)):
            if list2[i] in index1.keys():
                temp = i + index1[list2[i]]
                if min_index == temp:
                    res.append(list2[i])
                if min_index > temp:
                    min_index = temp
                    res.clear()
                    res.append(list2[i])
        return res

s = Solution()
print(s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))