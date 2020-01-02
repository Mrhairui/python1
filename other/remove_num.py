from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int)-> int:
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] == val:
                nums.pop()

        return len(nums)


if __name__ ==  '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    p = solution.removeElement(nums, val)
    print(p)
