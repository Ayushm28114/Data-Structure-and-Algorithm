class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]        
        count=0
        i=0

        while i<len(s):
            if s[i]=="(":
                stack.append(s[i])
                i+=1
            else:
                while i<len(s) and s[i]==")":
                    if stack:
                        stack.pop()
                    else:
                        count+=1
                    i+=1
        result = count + len(stack)
        return result