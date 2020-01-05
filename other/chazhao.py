from typing import List
class Solution:
    def search(self, nums:List[int], target:int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        middle = n//2
        while left < right-2:
            if nums[middle] > nums[left]:
                left = middle
                middle = left + (right - left + 1) // 2
            else:
                right = middle
                middle = left + (right - left + 1) // 2

        t = middle
        left = 0
        right = n-1
        while left < right:
            middle = (left + right) // 2  # 求中点
            real_middle = (t + middle) % n  # 循环队列
            if nums[real_middle] == target:
                return real_middle
            elif nums[real_middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1


if __name__ ==  '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    solution = Solution()
    p = solution.search(nums, target)
    print(p)




