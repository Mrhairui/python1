class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                tmp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = tmp

        for i in range(n):
            matrix[i].reverse()

