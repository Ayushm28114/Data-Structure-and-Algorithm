class Solution:
    def mirrorDistance(self, n: int) -> int:
        a=str(n)[::-1]
        
        return abs(n-int(a))