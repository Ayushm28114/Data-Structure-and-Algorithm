class Solution(object):
    def findMaxAverage(self, nums, k):
        s = sum(nums[:k])
        r = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s > r:
                r = s
        return r / float(k)