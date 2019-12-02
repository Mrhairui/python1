class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        res = 0
        ores = x
        while res < ores:
            a = ores % 10
            ores = ores // 10
            res = res * 10 + a

        if res//10 == ores or res == ores:
            return True
        else:
            return False

if __name__ == '__main__':
    solution =Solution()
    x = 11
    a = solution.isPalindrome(x)
    print(a)




