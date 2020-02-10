from typing import List
class Solution:
    def sortColors(self, nums:List[int]) -> None:
        n = len(nums)
        for i in range(0, n-1):
            j = 0
            while j < n - i - 1:
                if nums[j] > nums[j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
                j += 1


if __name__ == '__main__':
    solution = Solution()
    matrix = [2,0,2,1,1,0]
    solution.sortColors(matrix)



