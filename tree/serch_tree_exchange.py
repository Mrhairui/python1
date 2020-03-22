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
            if self.pre:
                if self.a == None and self.pre.val > root.val:
                    self.a = self.pre
                if self.a and self.pre.val > root.val:
                    self.b = root

            self.pre = root
            if root.right:
                find_Serach(root.right)

        self.pre = None
        self.a = None
        self.b = None
        find_Serach(root)
        self.a.val, self.b.val = self.b.val, self.a.val

if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    solution.recoverTree(root)






