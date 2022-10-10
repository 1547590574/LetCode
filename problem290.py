# <---coding: utf-8--->
# @Time:  2022/5/5/21:20
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ch2word, word2ch ={}, {}
        word = s.split(' ')
        if len(word) != len(pattern):
            return False
        for ch, word in zip(pattern,word):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word
        return True