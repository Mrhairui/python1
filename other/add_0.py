from typing import List
class Solution:
    def threeeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        a = []
        if n <= 2:
            return a


        for i in range(n-2):
            for j in range(i+1, n-1):
                res = -(nums[i] + nums[j] )
                for t in range(j+1, n):
                    if nums[t] == res:
                        a.append([nums[i], nums[j], nums[t]])
        return a

if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    b =  solution.threeeSum(nums)
    print(b)




