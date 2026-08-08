class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        time=0

        while l<=r:
            mid=l+(r-l)//2
            if self.time(mid,piles)<=h:
                time = mid
                r=mid-1
            elif self.time(mid,piles)>h:
                l=mid+1
            else:
                r=mid-1
        
        return time

    def time(self,n,nums):
        ans=0
        for num in nums:
            ans+= (num+n-1)//n
        return ans