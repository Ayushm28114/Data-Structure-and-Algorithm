class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dict1={}
        a=len(nums)//2

        for num in nums:
            dict1[num] = dict1.get(num,0)+1
        
        for key, value in dict1.items():
            if value==a:
                return key