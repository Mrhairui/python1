from typing import List
class Solution:
    def grayCode(self, n:int) -> List[int]:
        if n == 0:
            return [0]
        li = []
        li.append([0])
        li.append([0, 1])
        for i in range(2, n+1):
            tmp = li[i-1]
            p_tmp = list(reversed(tmp))
            pt = 2**(i-1)
            tt = tmp + [i+pt  for i in p_tmp]
            li.append(tt)

        return li[n]


if __name__ == '__main__':
    solution = Solution()
    n= 3
    pm = solution.grayCode(n)
    print(pm)

