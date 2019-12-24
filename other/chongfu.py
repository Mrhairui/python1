from typing import List
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n-1:
            if nums[i + 1] == nums[i]:
                n = n - 1
                j = i + 1
                while j < n :
                    nums[j] = nums[j + 1]
                    j = j + 1
            else:
                i = i + 1

        return n

if __name__ ==  '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    p = solution.removeDuplicates(nums)
    print(p)
