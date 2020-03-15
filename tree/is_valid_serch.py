class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            return isBST(root.right)

        return isBST(root)



