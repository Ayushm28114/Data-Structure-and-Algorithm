        # gain = lambda map(gain[x]: gain[x]+gain[x-1]) for x in range(1,len(gain))
        # return max(gain)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        for i in range(1, len(gain)):
            gain[i]+=gain[i-1]
        
        return max(max(gain),0)