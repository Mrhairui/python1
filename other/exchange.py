from typing import List
class Solution:
    def nextPermutation(self, nums:List[int]) -> None:
        firstIndex = -1
        n = len(nums)
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                firstIndex = i
                break
        if firstIndex == -1:
            reverse(nums, 0, n-1)
            return
        secondIndex = -1
        for i in range(n-1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                secondIndex = i
                break
        nums[firstIndex], nums[secondIndex] = nums[secondIndex], nums[firstIndex]
        reverse(nums,firstIndex + 1, n-1)


if __name__ == '__main__':
    nums = [1,3,2]
    solution = Solution()
    solution.nextPermutation(nums)


