from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = 0
        while left < right:
            if height[left] > height[right]:
                area = (right - left) * height[right]
                right -= 1
            else:
                area = (right - left) * height[left]
                left += 1
            if area >= max_area:
                max_area = area
        return max_area

if __name__ == '__main__':
    solution = Solution()
    aa = [1,8,6,2,5,4,8,3,7]
    bb = solution.maxArea(aa)
    print(bb)




