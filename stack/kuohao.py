class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        dic = {'(':')','{':'}','[':']'}
        stack = []
        for i in range(n):
            if s[i] in dic.values():
                if dic[stack[-1]] != s[i]:
                    return False
                stack.pop()
            else:
                stack.append(s[i])

        if not stack:
            return True

if __name__ == '__main__':
    solution = Solution()
    s = "{[]}"
    p = solution.isValid(s)
    print(p)



