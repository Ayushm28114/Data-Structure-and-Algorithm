class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        
        l, r = 0, 0

        while r<len(nums):
            if nums[r]==0:
                r+=1
            else:
                nums[r], nums[l] = nums[l], nums[r]
                r+=1
                l+=1
        return nums