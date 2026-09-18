class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        for i, word in enumerate(words):
            m=self.rev(word)
            words[i]=m
        return " ".join(words)


    def rev(self,w):
        s=list(w)
        i, j = 0, len(s)-1

        while i<=j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        return "".join(s)