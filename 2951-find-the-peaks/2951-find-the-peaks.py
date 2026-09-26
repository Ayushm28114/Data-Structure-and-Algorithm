class Solution:
    def findPeaks(self, nums: List[int]) -> List[int]:
        a=[]
        for i, num in enumerate(nums):
            if i==0:
                continue
            if i==len(nums)-1:
                break
            
            if nums[i-1] < num > nums[i+1]:
                a.append(i)
        return a