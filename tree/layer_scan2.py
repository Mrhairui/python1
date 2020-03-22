from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def layer_scan(root, layer):
            if not root:
                return
            if len(layers) == layer:
                layers.append([])
            layers[layer].append(root.val)
            layer_scan(root.left, layer+1)
            layer_scan(root.right, layer + 1)

        layers = []
        layer_scan(root, 0)
        return layers[::-1]


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    solution = Solution()
    a = solution.levelOrderBottom(root)

