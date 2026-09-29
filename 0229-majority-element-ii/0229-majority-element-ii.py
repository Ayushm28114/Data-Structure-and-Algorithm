class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        fr={}
        for num in nums:
            fr[num] = fr.get(num, 0) + 1
        l=len(nums)

        a=[]

        for key, value in fr.items():
            if value>l//3:
                a.append(key)

        return a