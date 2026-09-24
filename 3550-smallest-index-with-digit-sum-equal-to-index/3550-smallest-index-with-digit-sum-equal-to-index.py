class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            s=0
            num=n
            while num>0:
                s+=num%10
                num//=10
            if i==s:
                return i
        return -1