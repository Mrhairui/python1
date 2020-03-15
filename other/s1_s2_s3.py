class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ni = len(s1)
        nj = len(s2)
        nt = len(s3)
        if ni + nj != nt:
            return False
        i = j = t =0
        while t < nt:
            while i < ni:
                if s1[i] == s3[t]:
                    i += 1
                    t += 1
                else:
                    if nj == 0 or j == nj:
                        return False
                    else:
                        break
            while j < nj:
                if s2[j] == s3[t]:
                    j += 1
                    t += 1
                else:
                    if ni == 0 or i == ni:
                        return False
                    else:
                        break
            if i < ni and j < nj:
                if s1[i] != s3[t] and s2[j] != s3[t]:
                    return False

        return True



if __name__ == '__main__':
    s1 = 'aa'
    s2 = 'ab'
    s3 = "aaba"
    solution = Solution()
    pp = solution.isInterleave(s1, s2, s3)
    print(pp)
