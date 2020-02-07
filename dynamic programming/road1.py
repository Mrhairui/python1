class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
        else:
            obstacleGrid[0][0] = 0
        for i in range(1, m):
            if obstacleGrid[0][i] != 1:
                obstacleGrid[0][i] = obstacleGrid[0][i-1]
            else:
                obstacleGrid[0][i] = 0
        for i in range(1, n):
            if obstacleGrid[i][0] != 1:
                obstacleGrid[i][0] = obstacleGrid[i-1][0]
            else:
                obstacleGrid[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[n-1][m-1]

if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [[0,0],[1,1],[0,0]]
    a = solution.uniquePathsWithObstacles(obstacleGrid)
    print(a)