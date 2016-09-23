class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        x = len(board)
        y = len(board[0])
        status = [[0 for _ in range(y)] for _ in range(x)]
        visited = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            if board[i][0] == 'O':
                self.search(x, y, i, 0, board, status, visited)
            if board[i][y-1] == 'O':
                self.search(x, y, i, y-1, board, status, visited)
        for i in range(y):
            if board[0][i] == 'O':
                self.search(x, y, 0, i, board, status, visited)
            if board[x-1][i] == 'O':
                self.search(x, y, x-1, i, board, status, visited)
        for i in range(x):
            for j in range(y):
                if status[i][j] == 0:
                    b = list(board[i])
                    b[j] = 'X'
                    board[i] = "".join(b)
        print status

    def search(self, xm, ym, x, y, board, status, visited):
        if 0 <= x < xm and 0 <= y < ym and not visited[x][y]:
            status[x][y] = 1
            print x, y
            visited[x][y] = 1
            if x+1 < xm and not visited[x+1][y]:
                self.search(xm, ym, x+1, y, board, status, visited)
            if x-1 >= 0 and not visited[x-1][y]:
                self.search(xm, ym, x-1, y, board, status, visited)
            if y+1 < ym and not visited[x][y]:
                self.search(xm, ym, x, y+1, board, status, visited)
            if y-1 >= 0 and not visited[x][y-1]:
                self.search(xm, ym, x, y-1, board, status, visited)

b = ["OOOOXX","OOOOOO","OXOXOO","OXOOXO","OXOXOO","OXOOOO"]
Solution().solve(b)
print b