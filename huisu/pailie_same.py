from typing import List
class Solution:
    def permuteUnique(self, nums:List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                if i != first and nums[i] == nums[first]:
                    continue
                elif i != first and nums[i] != nums[first]:

                    nums[first], nums[i] = nums[i], nums[first]
                    if nums[:] in output:
                        continue
                backtrack(first + 1)
                if i != first and nums[i] != nums[first]:
                    nums[first], nums[i] = nums[i], nums[first]






        output = []
        n = len(nums)
        backtrack()
        return output


if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,1,1]
    p = solution.permuteUnique(nums)
    print(p)