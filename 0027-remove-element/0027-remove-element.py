class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l]==val:
                nums[l],nums[r] = nums[r],nums[l]
                r-=1
                count+=1
            else:
                l+=1
                
        return len(nums)-count