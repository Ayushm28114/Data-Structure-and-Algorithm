class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1=Counter(s)
        for i,char in enumerate(s):
            if dict1[char]==1:
                return i
        return -1