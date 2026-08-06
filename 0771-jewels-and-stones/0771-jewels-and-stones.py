class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone={}
        total_jewel=0

        for char in stones:
            if char in stone:
                stone[char]+=1
            else:
                stone[char]=1
        
        for jewel in jewels:
            if jewel in stone:
                total_jewel+=stone[jewel]
            
        return total_jewel