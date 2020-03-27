class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        def dp(root):
            if not root:
                return 0, True
            l, a = dp(root.left)
            r, b = dp(root.right)
            if not a or not b:
                return -10000, False
            if abs(l - r) > 1:
                return -10000, False
            if l >= r:
                return l+1, True
            else:
                return r+1, True

        if not root:
            return True
        l, a = dp(root.left)
        if not a:
            return False
        r, b = dp(root.right)
        if not b:
            return False
        if abs(l - r) > 1:
            return False
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
#    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
#    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)
#    root.right.right.right = TreeNode(3)
    solution = Solution()
    solution.isBalanced(root)