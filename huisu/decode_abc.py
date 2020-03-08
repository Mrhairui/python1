class Solution:
    def numDecodings(self, s:str) -> int:
        n = len(s)
        t = []
        def decode(idx, n):
            if idx == n-1:
                t.append(1)
                return t
            if idx == n-2 and int(s[idx:idx+2]) <= 26 and (int(s[idx]) != 0 and int(s[idx+1]) != 0):
                t.append(1)
            if int(s[idx]) != 0 and idx < n-1:
                decode(idx+1, n)
                if int(s[idx:idx+2]) <= 26 and  idx < n-2:
                    decode(idx + 2, n)
            else:
                if idx < n-1:
                    decode(idx + 1, n)
            return t


        pt = True
        for i in range(n):
            if s[i] != '0':
                pt = False
                break
        if pt == True:
            return 0
        else:
            pp = decode(0, n)
            return len(pp)





if __name__ == '__main__':
    solution = Solution()
    s = '010'
    p = solution.numDecodings(s)
    print(p)



