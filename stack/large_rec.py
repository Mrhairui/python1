from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        n = len(heights)
        stack = []
        stack.append(-1)
        max_area = 0
        i = 0
        for i in range(n):
            while heights[i] < heights[stack[-1]] and stack[-1] != -1:
                tmp = stack.pop()
                max_area = max(max_area, heights[tmp] * (i - 1 - stack[-1]))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (n - stack[-1]-1 ))
        return max_area


if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    solution = Solution()
    result = solution.largestRectangleArea(heights)
    print(result)





