class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)

        s=set()
        for num in nums:
            s.add(num)
        a=[]

        for i in range(small, large):
            if i not in s:
                a.append(i)
        
        return a