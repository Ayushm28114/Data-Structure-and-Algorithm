class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid=l+(r-l)//2

            if nums[l]==nums[r]==nums[mid]:
                l+=1
                r-=1

            elif nums[mid]>nums[r]:
                l=mid+1
            
            elif nums[mid]<=nums[r]:
                r=mid

            elif nums[mid]<nums[l]:
                l=mid

            else:
                r=mid-1


        return nums[l]            