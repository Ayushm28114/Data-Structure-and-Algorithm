class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        for i in range(k):
            if self.check(s[i]):
                count+=1
        curr = count
        
        for i in range(k,len(s)):
            if self.check(s[i]):
                curr+=1
            if self.check(s[i-k]):
                curr-=1
            count=max(count,curr)
        return count
            
    def check(self, ch):
        s=['a','e','i','o','u']
        if ch in s:
            return True
        return False