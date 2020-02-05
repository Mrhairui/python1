from typing import List
class Solution:
    def permuteUnique(self, nums: List[int])-> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]




        n = len(nums)
        output = []
        backtrack()
        return output
