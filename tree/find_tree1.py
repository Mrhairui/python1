from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        n = len(inorder)
        if n == 0:
            return None
        root = TreeNode(postorder[-1])

        in_left, in_right, post_left, post_right = [], [], [], []
        for i in range(0, n):
            if inorder[i] == postorder[-1]:
                post_left = postorder[0:i]
                post_right = postorder[i:n-1]
                in_left = inorder[0:i]
                in_right = inorder[i + 1:n]
                break
        n1 = len(post_left)
        n2 = len(post_right)
        if n1 != 0:
            root.left = self.buildTree(in_left, post_left)
        if n2 != 0:
            root.right = self.buildTree(in_right, post_right)
        return root