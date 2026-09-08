class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s)!=len(words):
            return False
        
        i=0
        
        for word in words:
            a=word
            if s[i]!=a[0]:
                return False
            i+=1
        
        return True