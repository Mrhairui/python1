from typing import List
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        i = 0
        j = 1
        while j < n:
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            else:
                j += 1
        return i + 1


if __name__ ==  '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    p = solution.removeDuplicates(nums)
    print(p)

