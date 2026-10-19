class Solution:
    def minInsertions(self, s: str) -> int:
        zero_one = 0
        st = []
        count = 0

        for br in s:
            if br=='(':
                if zero_one == 1:
                    zero_one = 0
                    if st:
                        count+=1
                        st.pop()
                    else:
                        count+=2

                st.append(br)
            else:
                if not st:
                    if zero_one==0:
                        zero_one=1
                    else:
                        zero_one=0
                        count+=1
                else:
                    if zero_one==0:
                        zero_one=1
                    else:
                        zero_one=0
                        st.pop()
        
        if zero_one==1:
            if st:
                st.pop()
                count+=1
            else:
                count+=2


        m=len(st)*2
        answer = count + m
        return answer