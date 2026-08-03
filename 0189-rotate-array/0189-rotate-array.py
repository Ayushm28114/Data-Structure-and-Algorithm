class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotating_index=k%len(nums)

        self.rev(0, len(nums)-1, nums)

        self.rev(0, rotating_index-1, nums)

        self.rev(rotating_index, len(nums)-1, nums)

    def rev(self, l, r, nums):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        return nums