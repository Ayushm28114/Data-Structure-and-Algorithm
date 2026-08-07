class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        st=0
        e=2

        if len(s)<3:
            return 0
        count=0

        while e<len(s):
            a=s[st]
            b=s[st+1]
            c=s[e]

            st+=1
            e+=1

            if a!=b and b!=c and c!=a:
                count+=1
        return count
            