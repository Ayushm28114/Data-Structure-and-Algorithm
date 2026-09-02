class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=sorted(set(nums),reverse=True)
        if len(n)<3: return max(n)
        return n[2]