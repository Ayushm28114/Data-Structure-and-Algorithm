class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # for num in nums:
        #     if nums.count(num) > 1:
        #         return True
        # return False
        return len(set(nums)) != len(nums)