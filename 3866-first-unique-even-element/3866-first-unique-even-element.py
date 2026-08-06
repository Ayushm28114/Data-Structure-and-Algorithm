class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1

        for num in nums:
            if num%2==0:
                if dict1[num]==1:
                    return num

        return -1 