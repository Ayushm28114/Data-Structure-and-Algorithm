class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reverse = ""
        n = len(s)
        
        for i in range(0, n, 2 * k):
            first_part = s[i : i + k]
            reverse += first_part[::-1]
            reverse += s[i + k : i + 2 * k]
            
        return reverse
        