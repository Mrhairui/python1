from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, t=0, tmp=[], tt = [], mark = False):
            if board[i][j] == word[t]:
                tmp.append(board[i][j])
                tt.append([i, j])
                t += 1
                if t >= n_word:
                    mark = True
                    return True
                if [i+1, j] not in tt and i < n-1 and not mark:
                    mark1 = backtrack(i + 1, j, t, tmp, tt)
                    if mark1:
                        return True
                if [i-1, j] not in tt and i > 0 and not mark:
                    mark1 = backtrack(i -1, j, t, tmp, tt)
                    if mark1:
                        return True
                if [i, j+1] not in tt and j < m-1 and not mark:
                    mark1 = backtrack(i, j+1, t, tmp, tt)
                    if mark1:
                        return True
                if [i, j-1] not in tt and j > 0 and not mark:
                    mark1 = backtrack(i, j-1, t, tmp, tt)
                    if mark1:
                        return True
                tmp.pop()
                tt.pop()
                return False
            else:
                return



        n_word = len(word)
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    h = backtrack(i, j, t=0, tmp=[], tt = [], mark=False)
                    if h:
                        return True
        return False

if __name__ == '__main__':
    solution = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    a = solution.exist(board, word)
    print(a)