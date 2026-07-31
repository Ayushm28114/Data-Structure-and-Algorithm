class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        b=a[::-1]
        c=""
        for i in b:
            c+=i+" "
        return c.strip()