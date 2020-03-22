from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])

        pre_left, pre_right, in_left, in_right = [], [], [], []
        for i in range(0, n):
            if inorder[i] == preorder[0]:
                pre_left = preorder[1:i+1]
                pre_right = preorder[i+1:n]
                in_left = inorder[0:i]
                in_right = inorder[i+1:n]
                break
        n1 = len(pre_left)
        n2 = len(pre_right)
        if n1 != 0:
            root.left = self.buildTree(pre_left, in_left)
        if n2 != 0:
            root.right = self.buildTree(pre_right, in_right)
        return root



if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    a = solution.buildTree(preorder, inorder)
    print(a)