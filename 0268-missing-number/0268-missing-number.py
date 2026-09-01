class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict1=Counter(nums)

        for i in range(0,len(nums)+1):
            if i not in dict1:
                return i
        