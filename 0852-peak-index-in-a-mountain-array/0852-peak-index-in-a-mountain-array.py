class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        maxm=0
        index=0
        for i,num in enumerate(arr):
            if num>maxm:
                maxm=num
                index=i
        return index