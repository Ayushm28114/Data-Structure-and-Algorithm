class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            mid = l + (r - l)//2
            if nums[mid]==target:
                return mid
            elif nums[l]==target:
                return l
            elif nums[r]==target:
                 return r
            elif target < nums[mid] and target > nums[l]:
                r=mid-1
            elif target > nums[mid] and target < nums[r]:
                l=mid+1
            else:
                l+=1
                r-=1
        return -1