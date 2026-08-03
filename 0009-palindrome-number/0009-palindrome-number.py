class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        n=x
        m=0
        while x>0:
            m=(m*10)+(x%10)
            x//=10
        return n==m