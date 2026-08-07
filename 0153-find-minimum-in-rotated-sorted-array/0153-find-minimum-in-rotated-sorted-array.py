class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        # minimum=nums[0]

        while l<r:
            mid=l+(r-l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            
            elif nums[mid]<nums[r]:
                r=mid

            elif nums[mid]<nums[l]:
                r=mid-1

            else:
                l=mid

        return nums[l]            