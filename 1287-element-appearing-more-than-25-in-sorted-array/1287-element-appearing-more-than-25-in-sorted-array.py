class Solution:
    def findSpecialInteger(self, nums: List[int]) -> int:
        dict1=Counter(nums)
        a=len(nums)/4
        for num in nums:
            if dict1[num]>a:
                return num