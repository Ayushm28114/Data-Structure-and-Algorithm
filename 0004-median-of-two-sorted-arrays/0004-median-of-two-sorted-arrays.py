class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums.sort()
        half=(len(nums)-1)//2

        if len(nums)%2==1:
            return nums[half]
        else:
            return (nums[half]+nums[half+1])/2