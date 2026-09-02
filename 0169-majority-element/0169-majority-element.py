class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1=Counter(nums)

        for key, value in dict1.items():
            if value>len(nums)/2:
                return key