class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        idx, count = 0, 0
        
        for num in nums:
            if num<target:
                idx+=1
            elif num==target:
                count+=1
        
        result = []
        
        for i in range(count):
            result.append(idx)
            idx+=1

        return result