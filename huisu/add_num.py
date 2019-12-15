from typing import List
class Solution:
    ### fdf ###
    def foursum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        stack = []
        def traceback(nums, target):
            n = len(nums)
            if target == 0:
                output.append(stack[:])
            for i in range(n):

                if target - nums[i] < 0:
                    break
                stack.append(nums[i])
                traceback(nums[i+1:], target - nums[i])
                stack.pop()

        traceback(nums, target)
        return output


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2,3 ,4]
    target = 0
    tt = solution.foursum(nums, target)
    print(tt)
