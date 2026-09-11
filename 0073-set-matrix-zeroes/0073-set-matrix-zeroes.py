class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        col=set()
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)

        for num in row:
            for j in range(n):
                matrix[num][j]=0
        
        for num in col:
            for i in range(m):
                matrix[i][num]=0