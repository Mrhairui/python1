from typing import List
class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            n = min(len(strs[i]),len(prefix))
            for j in range(n):
                if strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
                if j == n - 1 and len(strs[i]) < len(prefix):
                    prefix = strs[i]


        return prefix


if __name__ == '__main__':
    solution = Solution()
    a = ["flower", "flow", "flight"]
    b =  solution.longestCommonPrefix(a)
    print(b)






