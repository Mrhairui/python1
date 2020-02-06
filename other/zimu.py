class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        num = 0
        for i in range(n-1, -1, -1):
            if s[i] != ' ':
                num += 1
            elif s[i] == ' ' and num != 0:
                break

        return num

if __name__ == '__main__':
    solution = Solution()
    s = 'a '
    p = solution.lengthOfLastWord(s)
    print(p)