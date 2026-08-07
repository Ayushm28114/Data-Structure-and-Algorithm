class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1={}
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1

        dict2={}
        for char in t:
            if char in dict2:
                dict2[char]+=1
            else:
                dict2[char]=1
        
        for char in t:
            if char not in dict1:
                return char
            if dict1[char]!=dict2[char]:
                return char