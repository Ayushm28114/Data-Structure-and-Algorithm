class Solution:
    def removeStars(self, s: str) -> str:
        a=[]

        for ch in s:
            if ch=='*' and not a:
                continue
            if ch!='*':
                a.append(ch)
            else:
                a.pop()
        
        return "".join(a)