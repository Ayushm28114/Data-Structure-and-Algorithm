class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        a=""

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                a+=t[j]
                i+=1
            j+=1
        
        m="".join(a)
        return m==s
