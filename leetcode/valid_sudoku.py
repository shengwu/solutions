from collections import Counter

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        oneToNine = Counter(str(n) for n in range(10))
        def isValidRange(a):
            for k in a:
                if a[k] > oneToNine[k]: return False
            return True

        def transf(coll):
            return Counter(filter(lambda elem: elem != '.', coll))

        for row in board:
            if not isValidRange(transf(row)): return False
        transp = zip(*board)
        for i in range(9):
            if not isValidRange(transf(transp[i])): return False
        for i in range(3):
            for j in range(3):
                coll = board[i*3][j*3:j*3+3] + board[i*3+1][j*3:j*3+3] + board[i*3+2][j*3:j*3+3]
                if not isValidRange(transf(coll)): return False
        return True

        
s = Solution()
assert s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
assert not s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])
