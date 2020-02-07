class Solution:
    def uniquePaths(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j-1]
        return dp[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    n = 7
    k = 3
    a = solution.uniquePaths(n, k)
    print(a)