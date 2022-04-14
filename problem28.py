class Solution:
    # 第一遍，当两个匹配的串太长时会timeout，所以第二遍打算用已学过的KMP算法
    # def strStr(self, haystack: str, needle: str) -> int:
    #     n = len(haystack)
    #     m=len(needle)
    #     if n < m:
    #         return -1
    #     if m == 0:
    #         return 0
    #     if n == 0:
    #         return 0
    #     i = 0
    #     while i <= n-m:
    #         if haystack[i] == needle[0]:
    #             count = 1
    #             for j in range(1,m):
    #                 if haystack[i+j] != needle[j]:
    #                     break
    #                 else:
    #                     count += 1
    #             if count == m:
    #                 return i
    #         i += 1
    #     return -1

    def strStr(self, haystack: str, needle: str) -> int:

        return 0

    def same_start_end(self,s):
        #最长前后缀相同的字符位数
        n=len(s)
        i=0
        j=1
        result=[0] * n
        while i < n:
            breakpoint()

s=Solution()
print(s.strStr("aaaaaaaaaaaab","a"))