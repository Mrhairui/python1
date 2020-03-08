from typing import List
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def scan_1(tree, i):
    p_tree = tree
    while True:
        if i < p_tree.val:
            if p_tree.left.val == i:
                p_tree.left = None
                break
            else:
                p_tree = p_tree.left
        else:
            if p_tree.right.val == i:
                p_tree.right = None
                break
            else:
                p_tree = p_tree.right
    return tree

tree = TreeNode(2)
tree.right = TreeNode(3)
tree.left = TreeNode(1)
pp = scan_1(tree, 1)