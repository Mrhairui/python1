from typing import List
class Solution:
    def permute(self, nums:List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                for i in range(first, n):


        n = len(nums)
        output = []
        backtrack()
        return output
