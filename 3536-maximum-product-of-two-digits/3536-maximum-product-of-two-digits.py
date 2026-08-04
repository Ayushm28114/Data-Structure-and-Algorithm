class Solution:
    def maxProduct(self, n: int) -> int:
        bigger=0
        big=0

        m=n

        while m>0:
            rem=m%10       

            if rem>bigger:
                big=max(bigger,big)
                bigger=rem

            elif rem>big:
                big=rem
            m//=10
            
        return big * bigger