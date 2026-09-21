class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        a = sorted(nums)
        avg=set()

        l, r = 0, len(a)-1

        while l<r:
            av= (a[l]+a[r])/2
            avg.add(av)
            l+=1
            r-=1
        return len(avg)