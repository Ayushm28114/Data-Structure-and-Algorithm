class Solution:
    def maxArea(self, h: List[int]) -> int:
        result=0
        max_water=0
        curr_water=0

        l, r = 0, len(h)-1

        while l<r:
            a=min(h[l], h[r])
            curr_water=max(curr_water, a*(r-l))
            max_water=max(curr_water, max_water)

            if h[l]<h[r]:
                l+=1
            else:
                r-=1

        return max_water