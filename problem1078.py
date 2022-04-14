# <---coding: utf-8--->
# @Time:  2021/12/26/0:11
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List

# so easy的每日任务，明白了在if中用==和is的区别，以前的误区以为判断字符串相等要用is，其实只是比较对象引用是否相等的，要是想比较字符串的值是否相等还是用 ==。
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        first_word = text.split(' ')
        for i in range(len(first_word) - 2):
            if first_word[i] == first and first_word[i + 1] == second:
                result.append(first_word[i + 2])
        return result


s = Solution()
print(s.findOcurrences("alice is a good girl she is a good student", "a", "good"))
