class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        for i, item in enumerate(words):
            words[i] = words[i] + 'ma' + 'a' * (i+1) if item[0] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ] else item[1::] + item[0] + 'ma' +'a' * (i+1)
        return ' '.join(words)

s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))