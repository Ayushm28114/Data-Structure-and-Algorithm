class Solution:
    def findMaxK(self, nums):
        s = set(nums)
        
        ans = -1
        
        for x in nums:
            if x > 0 and -x in s:
                ans = max(ans, x)
        
        return ans