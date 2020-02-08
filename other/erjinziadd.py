class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = min(len(a), len(b))
        m = max(len(a), len(b))
        tmp = 0
        c = ''
        def reverse1(c):
            return c[::-1]
        a = reverse1(a)
        b = reverse1(b)
        for i in range(n):
            if tmp == 0:
                if int(a[i]) and int(b[i]):
                    tmp = 1
                    c += '0'
                elif int(a[i]) or int(b[i]):
                    tmp = 0
                    c += '1'
                else:
                    tmp = 0
                    c += '0'
            else:
                if int(a[i]) and int(b[i]):
                    tmp = 1
                    c += '1'
                elif int(a[i]) or int(b[i]):
                    tmp = 1
                    c += '0'
                else:
                    tmp = 0
                    c += '1'
        if tmp == 1 and m == n:
            c += '1'
        if len(a) > len(b):
            for i in range(n, m):
                if tmp:
                    if int(a[i]):
                        c += '0'
                        tmp = 1
                    else:
                        c += '1'
                        tmp = 0
                else:
                    c += a[i:m]
                    break
            if tmp == 1:
                c += '1'
        elif len(a) < len(b):
            for i in range(n, m):
                if tmp:
                    if int(b[i]):
                        c += '0'
                        tmp = 1
                    else:
                        c += '1'
                        tmp = 0
                else:
                    c += b[i:m]
                    break
            if tmp == 1:
                c += '1'


        c = reverse1(c)
        return c

if __name__ == '__main__':
    solution = Solution()
    a = '100'
    b = '110010'
    c = solution.addBinary(a, b)
    print(c)
