class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1

        check=False

        def present(idx: int):
            for i in range(len(needle)):
                if haystack[idx]!=needle[i]:
                    return False
                idx+=1
            return True
                
                
        for i, ch in enumerate(haystack):
            if ch==needle[0]:
                check=present(i)
                if check==True:
                    return i