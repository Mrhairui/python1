from typing import List
class Solution:
    def threeeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        p = []
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                elif sum == 0:
                    p.append([nums[i], nums[l],  nums[r]])
                    break

        return p

if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    b =  solution.threeeSum(nums)
    print(b)
