from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def recoverTree(self, root: TreeNode) -> None:

        def find_Serach(root):
            a = 0
            if root.left:
                find_Serach(root.left)
            a = a+3
            if self.pre and self.pre.val > root.val:
                print(4)
            self.pre = root
            find_Serach(root.right)

        self.pre = None
        find_Serach(root)

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.right = TreeNode(4)
    solution.recoverTree(root)






