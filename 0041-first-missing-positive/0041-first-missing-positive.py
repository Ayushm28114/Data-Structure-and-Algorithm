class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=min(nums)
        if x<0:
            x=1            
        
        dict1=Counter(nums)
        
        for i in range(1,x+len(nums)+1):
            if i not in dict1:
                return i