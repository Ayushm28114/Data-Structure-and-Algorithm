class Solution:
    def reverseStr(self, s: str, k: int) -> str:     

        a=list(s)

        def reverse(st,e):
            e=min(e-1, len(s)-1)

            while st<e:
                a[st], a[e] = a[e], a[st]
                st+=1
                e-=1
            
        i=0
        while i<len(s):
            reverse(i, i+k)
            i+=2*k
        
        return "".join(a)