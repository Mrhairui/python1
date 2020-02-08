class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n== 1:
            return 1
        a = [1 for _ in range(n)]
        a[1] = 2
        for i in range(2, n):
            a[i] = a[i-1] + a[i-2]

        return a[n-1]
