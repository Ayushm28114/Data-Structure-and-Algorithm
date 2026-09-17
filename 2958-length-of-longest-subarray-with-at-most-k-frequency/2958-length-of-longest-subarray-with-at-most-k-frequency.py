class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq={}
        l, r = 0, 0
        max_freq, curr_freq = 0, 0

        while r<len(nums):
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            
            if freq[nums[r]]<=k:
                curr_freq+=1

            else:
                while freq[nums[r]]>k:
                    freq[nums[l]]-=1
                    l+=1
                    curr_freq-=1
                curr_freq+=1
            max_freq = max(max_freq, curr_freq)
            r+=1
        
        return max_freq