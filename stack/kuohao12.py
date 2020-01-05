class Solution:
    def longestValidParentheses(self, s:str) -> int:
        n = len(s)
        stack = []
        num = 0
        num_num = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
                    num = num + 2
                    if not stack:
                        num_num = num

        return num


if __name__ ==  '__main__':
    s = ")()())"
    solution = Solution()
    p = solution.longestValidParentheses(s)
    print(p)
