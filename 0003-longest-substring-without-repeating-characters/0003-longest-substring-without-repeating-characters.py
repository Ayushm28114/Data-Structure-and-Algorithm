class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t=set()
        l=0
        max_l=0

        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l+=1
            max_l = max(max_l, r-l+1)
            t.add(s[r])
        return max_l