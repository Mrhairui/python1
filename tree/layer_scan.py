from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        def layer_Scan(node, layer):
            if len(levels) == layer:
                levels.append([])
            levels[layer].append(node.val)
            if node.left:
                layer_Scan(node.left, layer+1)
            if node.right:
                layer_Scan(node.right, layer+1)

        layer_Scan(root, 0)
        return levels

