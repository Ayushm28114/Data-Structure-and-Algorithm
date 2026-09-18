class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        l, r = 0, k-1
        sum=0

        for i in range(k):
            sum+=nums[i]
        
        max_avg=sum/float(k)

        while r<len(nums)-1:
            r+=1
            sum+=nums[r]
            sum-=nums[l]
            l+=1
            max_avg= max(max_avg, sum/float(k))
        return max_avg