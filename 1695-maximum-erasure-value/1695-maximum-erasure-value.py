class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        s=set()
        max_sum, curr_sum = 0, 0
        l = 0

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                while num in s:
                    curr_sum-=nums[l]
                    s.remove(nums[l])
                    l+=1
                s.add(num)
            curr_sum+=num
            max_sum = max(curr_sum, max_sum)
        return max_sum