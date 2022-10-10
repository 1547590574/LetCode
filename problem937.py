# <---coding: utf-8--->
# @Time:  2022/5/3/0:05
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        str_list, digit_list = [], []
        for i, item in enumerate(logs):
            # 纯数字和纯字母 只取一个元素判断就行
            if item.split(' ',1)[1][0].isalpha():
                str_list.append(item)
            else:
                digit_list.append(item)
        # 第一个sorted为了保证相同字母日志按照标识符排序
        str_list = sorted(str_list, key=lambda x: x.split(' ',1)[::-1])
        return str_list + digit_list
s1 = "let1 art zero can"
s2 = "let3 art zero"
print(' '.join(s1.split(' ',1)[::-1]))
print(' '.join(s2.split(' ',1)[::-1]))
print(' '.join(s1.split(' ',1)[::-1]) > ' '.join(s2.split(' ',1)[::-1]))

s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]))
