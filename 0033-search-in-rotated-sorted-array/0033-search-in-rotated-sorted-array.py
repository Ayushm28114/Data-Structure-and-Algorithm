class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Target lies in sorted left half
                else:
                    l = mid + 1  # Target lies in right half
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Target lies in sorted right half
                else:
                    r = mid - 1  # Target lies in left half

        return -1