class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        dict1={}
        dict2={}

        for num in nums:
            dict1[num]= dict1.get(num,0)+1
        
        for key, value in dict1.items():
            if value in dict2:
                return False
            dict2[value]=key
        return True