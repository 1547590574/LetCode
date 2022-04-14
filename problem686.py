import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 图解更方便，设置跳出条件（不然溢出），b的开头以a的尾巴结束，b的尾巴以a的头。所以blank长度为2 * n + m
        blank = ''
        n, m = len(a), len(b)
        i = 1
        while len(blank) < 2 * n + m:
            blank += a
            if blank.find(b) != -1:
                return i
            i += 1
        return -1


s = Solution()
print(s.repeatedStringMatch("abcd", "cdabcdab"))
