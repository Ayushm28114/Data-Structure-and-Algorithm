class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        a=''.join(word1)
        b=''.join(word2)
        return a==b