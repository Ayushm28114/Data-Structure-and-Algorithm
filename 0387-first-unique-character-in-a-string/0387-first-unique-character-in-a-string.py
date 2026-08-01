class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1
        
        for i in range(len(s)):
            if dict1[s[i]]==1:
                return i
        return -1