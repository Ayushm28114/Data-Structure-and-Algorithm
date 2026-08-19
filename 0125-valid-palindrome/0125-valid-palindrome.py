class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        st=0
        e=len(s)-1
        while st<=e:
            if not s[st].isalnum():
                st+=1
            elif not s[e].isalnum():
                e-=1
            else:
                if s[st]==s[e]:
                    st+=1
                    e-=1
                else:
                    return False
        return True