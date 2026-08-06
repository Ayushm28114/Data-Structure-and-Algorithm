class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        m=len(nums)-1
        maxdiff= (nums[m] * nums[m-1]) - (nums[0] * nums[1]) 
        return maxdiff