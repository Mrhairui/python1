
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def find_D(root, depth):
            if not root:
                if depth > self.max_depth:
                    self.max_depth = depth
            else:
                depth += 1
                find_D(root.left, depth)
                find_D(root.right, depth)
        self.max_depth = 0
        find_D(root, 0)
        return self.max_depth


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    a = solution.maxDepth(root)
    print(a)

