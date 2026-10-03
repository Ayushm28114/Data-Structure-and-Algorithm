class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        result=0
        odd=0

        for key, value in freq.items():
            if value%2==0:
                result+=value
            else:
                result+=value-1
                odd=1
        
        answer = result + odd
        
        return answer