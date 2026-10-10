class Solution:
    def findPrefixScore(self, nums: list[int]) -> list[int]:
        max_till_i = nums[0]

        nums[0]+=nums[0]

        for i in range(1, len(nums)):
            if nums[i] > max_till_i:
                max_till_i = nums[i]
            nums[i] += max_till_i + nums[i-1]
        
        return nums