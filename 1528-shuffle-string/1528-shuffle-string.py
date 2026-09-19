class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        a=list(s)

        for i, idx in enumerate(indices):
            a[idx]=s[i]
        return "".join(a)