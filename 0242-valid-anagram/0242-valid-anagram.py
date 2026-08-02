class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            dict1={}
            dict2={}

            for i,char in enumerate(s):
                if char in dict1:
                    dict1[char]+=1
                else:
                    dict1[char]=1
            
            for i,char in enumerate(t):
                if char in dict2:
                    dict2[char]+=1
                else:
                    dict2[char]=1
            return dict1==dict2