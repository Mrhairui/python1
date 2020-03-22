# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def if_same(p1,p2):
            if p1 == p2 == None:
                return True
            elif not p1 or not p2:
                return False
            else:
                if p1.val == p2.val:
                    return if_same(p1.left,p2.left) and if_same(p1.right, p2.right)
                else:
                    return False

        return if_same(p, q)
