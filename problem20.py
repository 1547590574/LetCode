class Solution:
    def isValid(self, s: str) -> bool:
        right = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                right.append(s[i])
            elif len(right)==0:
                return False
            elif s[i]==')' and right[-1]=='(':
                right.pop(-1)
            elif s[i]==']' and right[-1]=='[':
                right.pop(-1)
            elif s[i]=='}' and right[-1]=='{':
                right.pop(-1)
            else:
                return False
        if len(right)==0:
            return True
        return False



s = Solution()
print(s.isValid(']'))
