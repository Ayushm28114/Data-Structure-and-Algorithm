class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        a = [[0]*len(matrix) for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                matrix[row][col], a[col][row] = a[col][row], matrix[row][col]
        return a