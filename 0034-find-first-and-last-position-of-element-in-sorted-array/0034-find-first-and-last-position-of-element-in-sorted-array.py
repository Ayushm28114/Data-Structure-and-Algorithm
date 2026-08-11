class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)
        
        while(l<r):
            m=(l+r)//2
            if nums[m]>=target:
                r=m
            else:
                l=m+1
        first=l

        l=0
        r=len(nums)

        while(l<r):
            m=(l+r)//2
            if nums[m]>target:
                r=m
            else:
                l=m+1
        last=l-1

        if first==len(nums) or nums[first]!=target:
            return [-1, -1]
        else:
           
            return [first, last]