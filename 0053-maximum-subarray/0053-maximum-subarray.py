class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1 : return nums[0]
        max_sum=nums[0]
        curr_sum=nums[0]
        i=1


        while i<len(nums):
            curr_sum= max(nums[i], curr_sum + nums[i])
            max_sum= max(curr_sum, max_sum)
            i+=1

        return max_sum