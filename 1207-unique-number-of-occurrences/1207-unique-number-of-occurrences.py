class Solution:
    def uniqueOccurrences(self, nums: List[int]) -> bool:
        dict1={}
        dict2={}

        for num in nums:
            dict1[num]= dict1.get(num,0)+1
        
        return len(dict1.values())== len(set(dict1.values()))