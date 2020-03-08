from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root:TreeNode) -> List[int]:

        def find(tree):
            if not tree: # 刚开始没有想到的，在最开始判断是不是空，进而后面代码可以简单
                return
            find(tree.left)
            ans.append(tree.val)
            find(tree.right)
        ans = []

        find(root)
        return ans

