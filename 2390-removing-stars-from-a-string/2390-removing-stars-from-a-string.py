class Solution:
    def removeStars(self, s: str) -> str:
        a=[]

        for ch in s:
            if ch!='*':
                a.append(ch)
            else:
                a.pop()
        
        return "".join(a)