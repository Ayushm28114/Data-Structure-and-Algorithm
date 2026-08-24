class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0]*n for i in range(n)]

        top, bottom = 0, len(m)-1
        left, right = 0, len(m[0])-1

        count=1

        while top<=bottom and left<=right:

            for a in range(left, right+1):
                m[top][a]=count
                count+=1            
            top+=1

            for b in range(top, bottom+1):
                m[b][right]=count
                count+=1
            right-=1

            if top<=bottom:
                for c in range(right, left-1, -1):
                    m[bottom][c]=count
                    count+=1
                bottom-=1
            
            if left<=right:
                for d in range(bottom, top-1, -1):
                    m[d][left]=count
                    count+=1
                left+=1
        
        return m