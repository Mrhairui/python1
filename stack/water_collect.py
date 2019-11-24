from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height : return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] -1)
            stack.append(i)
        return res


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result = solution.trap(height)
    print(result)

