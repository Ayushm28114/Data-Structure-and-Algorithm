class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l, r = 0, 0
        max_freq, curr_freq = 0, 0

        while r<len(s):
            if s[r] not in freq or freq[s[r]]==0:
                # curr_freq += 1
                freq[s[r]] = 1
                r+=1

            else:
                max_freq = max(max_freq, curr_freq)
                curr_freq = r-l
                while freq[s[r]]>0:
                    # curr_freq -= 1
                    freq[s[l]] -= 1
                    l+=1
            curr_freq = r-l
            max_freq = max(max_freq, curr_freq)
        return max_freq