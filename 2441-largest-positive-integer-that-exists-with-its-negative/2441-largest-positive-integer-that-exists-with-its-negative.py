class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ht = {}
        largest = 0

        for num in nums:
            ht[num] = ht.get(num, 0) + 1
            
            if num*-1 in ht:
                largest = max(abs(num), largest)

        return largest if largest>0 else -1