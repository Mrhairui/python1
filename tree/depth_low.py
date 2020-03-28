class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l == 0 and r == 0:
            return 1
        if l >0 and  r == 0:
            return l + 1
        if l == 0 and r > 0:
            return r + 1
        if l <= r:
            return l + 1
        else:
            return r + 1


if __name__ == '_main__':
    solution = Solution( )
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(23)
    a = solution.minDepth(root)
    print(a)