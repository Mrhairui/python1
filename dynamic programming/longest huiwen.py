class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return  ''
        n = len(s)
        dp = [[0]*n  for _ in range(n)]
        max_len = float('-inf')
        res = ''
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                if dp[j][i] and max_len < i + 1 - j:
                    res = s[j : i + 1]
                    max_len = i + 1 - j
        return res
