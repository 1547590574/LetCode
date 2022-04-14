class Soultion:
    def expandString(self, start, end, s):
        while start > 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            start1, end1 = self.expandString(i, i, s)
            start2, end2 = self.expandString(i, i + 1, s)
            if end2 - start2 > end - start:
                start, end = start2, end2
            if end1-start1>end-start:
                start, end = start1, end1
        return s[start:end + 1]


s = Soultion()
print(s.longestPalindrome('babad'))
