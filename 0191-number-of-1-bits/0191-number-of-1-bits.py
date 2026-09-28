class Solution:
    def hammingWeight(self, n: int) -> int:
        sb=0
        w=n
        while w:
            a=w&1
            if a==1:
                sb+=1
            w>>=1
        return sb