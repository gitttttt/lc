def isValidSudoku(board):
    def func(p):
        if p == '.':
            return -1
        else:
            return int(p)
    board = [list(map(func, x)) for x in board]
    print(board)
    for y in board:
        sets = set()
        for x in y:
            if not x == -1:
                if sets.__contains__(x):
                    return False
                else:
                    sets.add(x)
    for (x, y) in [(x, y) for x in range(3) for y in range(3)]:
            sets = set()
            for (m, n) in [(m, n) for m in range(3) for n in range(3)]:
                k = board[3*x+m][3*y+n]
                if not k == -1:
                    if sets.__contains__(k):
                        return False
                    else:
                        sets.add(k)
    for y in range(9):
        sets = set()
        for z in board:
            x = z[y]
            if not x == -1:
                if sets.__contains__(x):
                    return False
                else:
                    sets.add(x)
    return True




a = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
isValidSudoku(a)