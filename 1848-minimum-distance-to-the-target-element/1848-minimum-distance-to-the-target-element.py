class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        
        minimum=1001

        for i,num in enumerate(nums):
            if num==target:
                minimum = min(minimum, abs(i-start))
        
        return minimum