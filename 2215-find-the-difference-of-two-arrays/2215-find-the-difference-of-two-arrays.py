class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]

        a=[]
        for num in nums1:
            if num not in nums2:
                a.append(num)
        
        b=[]
        for num in nums2:
            if num not in nums1:
                b.append(num)
        
        m=set(a)
        n=set(b)
        
        result.append(list(m))
        result.append(list(n))
        return result