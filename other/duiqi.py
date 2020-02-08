from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int)->List[str]:
        n = len(words)
        l = maxWidth + 1
        output = []
        tmp = []
        for i in range(n):
            if l > len(words[i]):
                l = l - 1
                tmp.append(words[i])
                l -= len(words[i])
            else:
                nn = len(tmp)
                if nn == 1:
                    tmpp = tmp[0] + l * ' '
                else:
                    pp = l // (nn-1)
                    pt = l % (nn - 1)
                    tmpp = tmp[0]
                    for j in range(1, nn):
                        tmpp += (pp + 1) * ' '
                        if pt > 0:
                            tmpp += ' '
                        tmpp += tmp[j]
                        pt = pt -1
                output.append(tmpp)
                l = maxWidth
                tmp = []
                pt = 0
                tmp.append(words[i])
                l = l - len(words[i])
        nn = len(tmp)
        if nn == 1:
            tmpp = tmp[0] + l * ' '
        else:
            pp = l // (nn - 1)
            pt = l % (nn - 1)
            tmpp = tmp[0]
            for j in range(1, nn):
                tmpp += ' '
                tmpp += tmp[j]
            tmpp += l*' '
        output.append(tmpp)

        return output

if __name__ == '__main__':
    solution = Solution()
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    b = solution.fullJustify(words, maxWidth)
    print(b)

