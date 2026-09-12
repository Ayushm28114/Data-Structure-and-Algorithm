class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        m,n=len(word1), len(word2)
        a=''
            
        while i<m and j<n:
            a+=word1[i]
            a+=word2[j]
            i+=1
            j+=1

        while i<m:
            a+=word1[i]
            i+=1
        
        while j<n:
            a+=word2[j]
            j+=1
        
        return a