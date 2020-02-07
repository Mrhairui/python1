class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        di = [0]
        aa = [1]
        tmp = 1
        if n== 1:
            return '1'
        for i in range(1, n):
            tmp *= i
            aa.append(i+1)
            di.append(tmp)
        di.append(0)

        output = ''
        pp = 0


        for i in range(n-1, 1, -1):
            if k % di[i]!= 0:
                pp = k // di[i]
            else:
                pp = k // di[i] - 1
            output += str(aa[pp])
            aa.remove(aa[pp])
            k -= pp * di[i]
        if k == 1 or k== 2:
            if k == 1:
                output += str(aa[0])
                output += str(aa[1])
            else:
                output += str(aa[1])
                output += str(aa[0])
        else:
            k -= 2
            if k == 1:
                output += str(aa[0])
                output += str(aa[1])
            else:
                output += str(aa[1])
                output += str(aa[0])

        return output

if __name__ == '__main__':
    solution = Solution()
    n = 3
    k = 5
    a = solution.getPermutation(n, k)
    print(a)

