from typing import List
class Solution:
    def merge(self, nums1:List[int], m:int, nums2:List[int], n:int) -> None:
        t = 0
        nn = m - 1
        for i in range(n):
            while t <= nn:
                if nums2[i] < nums1[t]:
                    pp = nn
                    while pp >= t:
                        nums1[pp+1] = nums1[pp]
                        pp = pp - 1
                    nums1[t] = nums2[i]
                    nn += 1
                    t += 1
                    break
                else:
                    t += 1
            if t > nn:
                nums1[nn + 1] = nums2[i]
                nn += 1
            i += 1



if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)



