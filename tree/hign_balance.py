from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        if n == 0:
            return None
        root = TreeNode(nums[n//2])
        if n > 1:
            root.left = self.sortedArrayToBST(nums[0:n//2])
            root.right = self.sortedArrayToBST(nums[n//2 + 1: n])
        return root


if __name__ == '__main__':
    nums = [-10,3,0,5,9]
    solution = Solution()
    a = solution.sortedArrayToBST(nums)
    print(a)

