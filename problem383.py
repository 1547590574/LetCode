# <---coding: utf-8--->
# @Time:  2022/4/14/11:33
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a, b = len(ransomNote), len(magazine)
        if a > b:
            return False
        if a <= b :
            map = {}
            for i, j in enumerate(magazine):
                map[j] = map[j] + 1 if j in map.keys() else 1
            for i, item in enumerate(ransomNote):
                if item not in map:
                    return False
                else:
                    if map[item] >= 1:
                        map[item] -= 1
                    else:
                        return False
            return True

s = Solution()
print(s.canConstruct('aa','aab'))