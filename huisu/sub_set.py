class Solution:
    def subsets(self, nums):
        def backtrack(first = 0, tmp = []):
            for i in range(first, n):
                tmp.append(nums[i])
                output.append(tmp[:])
                if i < n-1:
                    backtrack(i + 1,tmp)
                tmp.pop()
        n = len(nums)
        output = []
        backtrack()
        output.append([])
        return output

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    soltion.subsets(nums)