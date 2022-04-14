# <---coding: utf-8--->
# @Time:  2022/3/14/16:41
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import re
class Solution:
    def countSegments(self, s):
        segment_count = 0

        for i in range(len(s)):
            if (i == 0 or s[i - 1] == ' ') and s[i] != ' ':
                segment_count += 1

        return segment_count
