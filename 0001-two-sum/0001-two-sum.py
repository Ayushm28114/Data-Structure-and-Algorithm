class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in dict1:
                return [dict1[rem],i]
            else:
                dict1[num]=i