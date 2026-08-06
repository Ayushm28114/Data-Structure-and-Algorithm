class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        dict1={}
        for num in nums:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1

        for k,v in dict1.items():
            if k%2==0 and v==1:
                return k

        return -1 