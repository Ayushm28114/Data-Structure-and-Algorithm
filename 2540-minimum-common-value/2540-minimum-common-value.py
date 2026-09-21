class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        a=list(set(nums1).intersection(set(nums2)))
        return min(a) if a else -1