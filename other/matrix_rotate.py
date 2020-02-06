class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        judge = 1
        i, j = 0, -1
        while m > 0 and n > 0:
            for x in range(n):
                j += judge * 1
                ans.append(matrix[i][j])

            for y in range(m-1):
                i += judge * 1
                ans.append(matrix[i][j])
                m, n = m -1, n - 1
                judge *= -1
        return ans


