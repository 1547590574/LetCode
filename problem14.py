from typing import List


class Solution:
    #暴力解法，时间上不占优
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxcount = 200
        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                count = self.commonPrefix(strs[i], strs[j])
                if count < maxcount:
                    maxcount = count
        return strs[0][0:maxcount]

    def commonPrefix(self, str1, str2) -> int:
        count = 0
        minstr=len(str1)
        if len(str1)>len(str2):
            minstr=len(str2)
        for i in range(minstr):
            if str1[i] != str2[i]:
                break
            count += 1
        return count


s = Solution()
print(s.longestCommonPrefix(["baab", "bacb", "b", "cbc"]))
