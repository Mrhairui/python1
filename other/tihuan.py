class Solution:
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        tmpi = []
        tmpj = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    tmpi.append(i)
                    tmpj.append(j)
        tmpi = list(set(tmpi))
        tmpj = list(set(tmpj))
        ni = len(tmpi)
        nj = len(tmpj)
        for i in range(ni):
            matrix[tmpi[i]] = [0] * m
        for j in range(nj):
            for t in range(n):
                matrix[t][tmpj[j]] = 0


if __name__ == '__main__':
    solution = Solution()
    matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
    solution.setZeroes(matrix)






