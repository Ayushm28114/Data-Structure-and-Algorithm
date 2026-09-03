class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
            
        a=[]    
        for b in s:
            if b=='(' or b=='{' or b=='[':
                a.append(b)
            else:
                if a:
                    m=a.pop()
                else:
                    return False
                    
                if m=='(' and b==')':
                    continue
                elif m=='[' and b==']':
                    continue
                elif m=='{' and b=='}':
                    continue
                else:
                    return False
        if a:
            return False
        return True