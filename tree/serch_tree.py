from typing import List
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n:int) -> List[TreeNode]:
        ans = []
        tmp = []
        for i in range(1, n+1):
            tmp.append(i)

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
        def tree_gen(tmp, tree):
            if not tmp:
                return tree.right
            nn = len(tmp)
            for i in range(nn):
                tree = scan(tree, tmp[i])
                pp = tmp[i]
                tmp.remove(tmp[i])
                ppt = tree_gen(tmp, tree)
                ans.append(ppt)
                tmp.insert(0, pp)
                tree = scan_1(tree, pp)

        tree_gen(tmp, TreeNode(0))
        return ans

if __name__ == '__main__':
    solution = Solution()
    solution.generateTrees(3)

