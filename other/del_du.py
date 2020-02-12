from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        len_n = n
        if n < 3:
            return n
        t = 1
        p = []
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                t += 1
                if t > 2:
                    len_n -= 1
                    p.append(i)
            else:
                t = 1
        if p == []:
            return len_n
        else:
            m = 0
            p = [_ + 1  for _ in p[:]]
            while m < len(p):
                p = [_ - 1 for _ in p[:]]
                del nums[p[m]]
                m += 1

        return len_n

if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0, 0, 0, 0]
    p = solution.removeDuplicates(nums)
    print(p)


