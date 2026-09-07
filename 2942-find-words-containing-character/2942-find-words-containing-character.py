class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        
        for i, word in enumerate(words):
            if x in word:
                a.append(i)
        return a