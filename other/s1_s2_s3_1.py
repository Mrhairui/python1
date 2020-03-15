class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        import functools
        @functools.lru_cache(None)

        def isCopy1(s1,s3):
            n = len(s1)
            i = 0
            while i < n:
                if s1[i] != s3[i]:
                    return False
                i += 1
            return True

        def isCopy(s1,s2,s3):
            if s1[0] == s3[0] and s2[0] == s3[0]:
                if len(s1) > 1 and len(s2) > 1:
                    return isCopy(s1[1:], s2, s3[1:]) or isCopy(s1, s2[1:], s3[1:])
                elif len(s1) > 1 and len(s2) == 1:
                    return isCopy1(s1,s3[1:]) or isCopy(s1[1:], s2, s3[1:])
                elif len(s2) > 1 and len(s1) == 1:
                    return isCopy1(s2, s3[1:]) or isCopy(s1, s2[1:], s3[1:])
                else:
                    return isCopy1(s2, s3[1:]) or isCopy1(s1, s3[1:])
            elif s1[0] == s3[0] and s2[0] != s3[0]:
                if len(s1) > 1:
                    return isCopy(s1[1:], s2, s3[1:])
                else:
                    return isCopy1(s2, s3[1:])
            elif s1[0] != s3[0] and s2[0] == s3[0]:
                if len(s2) > 1:
                    return isCopy(s1, s2[1:], s3[1:])
                else:
                    return isCopy1(s1, s3[1:])
            else:
                return False




        ni = len(s1)
        nj = len(s2)
        nt = len(s3)
        if ni + nj != nt:
            return False
        if ni == nj == nt == 0:
            return True
        if ni == 0:
            return isCopy1(s2,s3)
        elif nj == 0:
            return isCopy1(s1, s3)
        else:
            return isCopy(s1,s2,s3)


if __name__ == '__main__':
    s1 = "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
    s2 = "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
    s3 = "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    solution = Solution()
    pp = solution.isInterleave(s1, s2, s3)
    print(pp)


