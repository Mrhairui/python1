from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
         n = len(nums)
         p = 0
         for i in range(n-1):
             if nums[i] > nums[i+1]:
                 p = i + 1
                 break
         nums_1 = []
         if p == 0:
             nums_1 = nums
         else:
             nums_1 .extend(nums[p:n])
             nums_1.extend(nums[0:p])
         left = 0
         right = n-1
         while left <= right:
             middle = (right + left) // 2
             if nums_1[middle] == target:
                 return True
             elif nums_1[middle] > target:
                 right = middle - 1
             else:
                 left = middle + 1
         return False

if __name__ == '__main__':
    solution = Solution()
    nums = [1]
    target = 1
    p = solution.search(nums, target)
    print(p)



