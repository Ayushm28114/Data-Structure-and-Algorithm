class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        i=0
        j=len(height)-1
        while i<j:
            ans=0
            if height[i] < height[j]:
                ans=(j-i)*height[i]
                i+=1
            else:
                ans= (j-i)*height[j]
                j-=1
            if ans>res:
                res=ans
        return res     
