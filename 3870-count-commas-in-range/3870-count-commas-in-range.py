class Solution:
    def countCommas(self, n: int) -> int:
        count=0
        for i in range(n+1):
            a=str(i)
            if len(a)>3:
                count+=(len(a)-1)//3
        return count