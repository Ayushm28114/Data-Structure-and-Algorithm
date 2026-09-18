class Solution:
    def checkIfExist(self, nums: list[int]) -> bool:
        freq={}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num in nums:
            if num==0 and freq[num]==1:
                continue
            if num*2 in freq:
                return True
        return False