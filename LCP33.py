# <---coding: utf-8--->
# @Time:  2022/10/10/12:42
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List
import math

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        if max(vat) == 0:
            return 0
        length = len(vat)
        res = 10e4
        for i in range(1,max(vat)+1):
            cur = i
            for j in range(length):
                bucket_size = (vat[j] + i - 1)//i
                times = 0 if bucket_size -bucket[j] < 0 else bucket_size -bucket[j]
                cur += times
            res = res if res < cur else cur
        return res
