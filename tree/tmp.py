from typing import List
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def scan(tree, i):
    p_tree = tree
    while True:
        if i < p_tree.val:
            if p_tree.left == None:
                p_tree.left = TreeNode(i)
                break
            else:
                p_tree = p_tree.left
        else:
            if p_tree.right == None:
                p_tree.right = TreeNode(i)
                break
            else:
                p_tree = p_tree.right
    return tree

tree = TreeNode(1)
tree.right = TreeNode(3)
pp = scan(tree, 2)