# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mid_scan(p1, p2):
            if p1 == p2 == None:
                return True
            elif not p1 or not p2:
                return False
            else:
                if p1.val == p2.val:
                    return mid_scan(p1.left, p2.right) and mid_scan(p1.right, p2.left)
                else:
                    return False
        if root == None:
            return True
        else:
            return mid_scan(root.left, root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(2)