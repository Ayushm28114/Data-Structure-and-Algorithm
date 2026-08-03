class Solution:
    def isPalindrome(self, x: int) -> bool:
        m=str(x)
        l=0
        r=len(m)-1

        while l<r:
            if m[l]==m[r]:
                l+=1
                r-=1
            else:
                return False
        return True