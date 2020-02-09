from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        x = 0
        for i in range(n):
            if matrix[i][-1] > target:
                x = i
                break
        for j in range(m):
            
