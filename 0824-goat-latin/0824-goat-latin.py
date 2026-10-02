class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        words = sentence.split()

        a=[]

        for i, word in enumerate(words):
            w = word
            if w[0] not in vowels:
                w = word[1::]+word[0]
            w+='ma'
            w+=(i+1)*'a'
            a.append(w)
        
        result = " ".join(a)
        return result