class Solution:
    def romanToInt(self, s: str) -> int:
        """

        用字典记录每个罗马字母对应的数字，将每个数设置优先级，优先级大的数值大，并且认为优先级小的出现在优先级大的左边时，就是大的减去小的；
        遇到优先级大的可以直接加到整体上，遇到小的直接减下去。
        """
        value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and value[s[i]] < value[s[i + 1]]:
                ans -= value[s[i]]
            else:
                ans += value[s[i]]

        return ans


s = Solution()
print(s.romanToInt('MCMXCIV'))
