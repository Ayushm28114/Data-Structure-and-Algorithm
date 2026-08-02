class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        l=0
        while nums[l]!=0 and l<len(nums):
            l+=1
            if l==len(nums):
                return nums

        r=l+1        

        while r<len(nums) and l<len(nums):
            if nums[r]==0:
                r+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r+=1
        return nums