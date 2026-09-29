class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s={}
        for i, num in enumerate(nums):
            if num in s and abs(i-s[num])<=k:
                return True
            s[num]=i
        return False