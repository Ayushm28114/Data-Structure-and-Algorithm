class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        one, zero, curr_zero, curr_one, curr = 0, 0, 0, 0, True

        i=0
        while i<len(s):
            if s[i]=='0':
                if curr==False:                    
                    curr_zero+=1
                else:
                    curr=False
                    curr_zero=1
                zero = max(curr_zero, zero)

            else:
                if curr==True:
                    curr_one+=1
                else:
                    curr=True
                    curr_one=1
                one = max(curr_one, one)
            i+=1
            
        return one>zero