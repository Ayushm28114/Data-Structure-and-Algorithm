class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=low%2
        b=high%2

        if a==0 and  b==0:
            return (high-low)//2
        else:
            m=((high-low)//2)+1
            return m