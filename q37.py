def solveSudoku(board):
    def check(x, y, k):
        pass
    for x in range(9):
        for y in range(9):
            if board[x][y] == '.':
                for k in range(9):
                    if check(x, y, k):
                        pass