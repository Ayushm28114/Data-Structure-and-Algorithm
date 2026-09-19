class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow='aeiou'
        count = 0
        for i in range(k):
            if s[i] in vow:
                count+=1
        curr = count
        
        for i in range(k,len(s)):
            if s[i] in vow:
                curr+=1
            if s[i-k] in vow:
                curr-=1
            count=max(count,curr)
        return count
            
    