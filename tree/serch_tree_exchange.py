from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.pre = None
        p = TreeNode(-1)
        def find_Serach(root):
            if not root.left:
                find_Serach(root.left)

            if self.pre and self.pre > root:
                p1 = self.pre
            if self.pre and self.pre
            self.pre = root



