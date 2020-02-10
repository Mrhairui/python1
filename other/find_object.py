from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        t = n*m
        if t == 0:
            return False
        left = 0
        right = t - 1
        if matrix[right//m][right%m] == target:
            return True
        middle = (right+left) // 2
        while left <= right:
#            if matrix[left//m][left%m] == matrix[middle//m][middle%m]:
#                if matrix[middle//m][middle%m] == target:
#                    return True
#                else:
#                    return False
            if matrix[middle//m][middle%m] == target:
                return True
            elif matrix[middle//m][middle%m] > target:
                right = middle - 1
                middle = (right+left) // 2
            else:
                left = middle + 1
                middle = (right+left) // 2
        return False
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 3]]
    target = 3
    p = solution.searchMatrix(matrix, target)
    print(p)



