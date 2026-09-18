class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        s = sum(arr[:k])
        if s//k >= threshold:
            count+=1
        
        for i in range(k,len(arr)):
            s += arr[i] - arr[i-k]
            if s//k >= threshold:
                count+=1
        
        return count