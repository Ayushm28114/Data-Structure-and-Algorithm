class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x=min(nums)
        if x<0:
            x=1            
        
        s=set()
        for num in nums:
            s.add(num)
        
        for i in range(1,x+len(nums)+1):
            if i not in s:
                return i