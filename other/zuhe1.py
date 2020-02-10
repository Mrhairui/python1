from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, tmp = []):
            for i in range(first, n+1):
                tmp.append(i)
                if len(tmp) == k:
                    output.append(tmp[:])
                    tmp.pop()
                    continue
                backtrack(i + 1, tmp)
                tmp.pop()
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    solution = Solution()
    s = 4
    t = 3
    solution.combine(s, t)



