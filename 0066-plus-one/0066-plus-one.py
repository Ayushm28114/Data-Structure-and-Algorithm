class Solution:
    def plusOne(self, nums: List[int]) -> List[int]:
        if nums[len(nums)-1]!=9:
            nums[len(nums)-1]+=1
            return nums
        digit =0
        for i in nums:
            digit = (digit*10)+i
        digit+=1
        m=digit
        arr=[]

        while m>0:
            n=m%10
            arr.append(n)
            m//=10
        
        l=0
        r=len(arr)-1
        while l<r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        return arr