class Solution:
    def reverse(self, x: int) -> int:
        a=1
        if x<0:
            x*=-1
            a*=-1

        b=0
        
        while x>0:
            rem=x%10
            b=(b*10)+rem
            x//=10
        
        b*=a

        if b< -2**31 or b>2**31 -1:
            return 0
        return b
        
