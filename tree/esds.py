class Solution:
    def recoverTree(self, root):
        def find_Serach(root):
            if root != 0:
                find_Serach(root-1)
            self.a -= 1
            if self.a != 0:
                find_Serach(self.a -1)
            self.a -= 1

        self.a = 10
        find_Serach(root)

if __name__ == '__main__':
    solution = Solution()
    p=3
    solution.recoverTree(p)