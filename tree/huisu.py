class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.s = 10000000
        def back_track(root, sum):
            if not root:
                return
            sum -= root.val
            if sum == 0:
                if root.left ==None and root.right == None:
                    self.s = 0
                    return
                else:
                    back_track(root.left, sum)
                    back_track(root.right, sum)

            back_track(root.left, sum)
            back_track(root.right, sum)

        if not root:
            if self.s == 0:
                return False
            else:
                return False
        back_track(root, sum)
        if self.s == 0:
            return True
        else:
            return False


if __name__ == '_main__':
    solution = Solution( )
    sum = -1
    root = TreeNode(1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(-2)
    a = solution.hasPathSum(root, sum)
    print(a)