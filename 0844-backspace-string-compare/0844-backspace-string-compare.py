class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        p=self.strike(s)
        q=self.strike(t)
        return p==q        
    

    def strike(self,st):
        a=[]
        for ch in st:
            if not a and ch=='#':
                continue
            elif ch=='#':
                a.pop()
            else:
                a.append(ch)
            
        b=""
        for ch in a:
            b+=ch
        return b