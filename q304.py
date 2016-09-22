class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.tmp1 = [[0 for _ in matrix[0]] for _ in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 0:
                    print 'h'
                    self.tmp1[i][0] = matrix[i][0]
                else:
                    self.tmp1[i][j] = self.tmp1[i][j-1] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                res += self.tmp1[i][col2]
            else:
                res += (self.tmp1[i][col2] - self.tmp1[i][col1-1])
        return res


        # Your NumMatrix object will be instantiated and called as such:
        # numMatrix = NumMatrix(matrix)
        # numMatrix.sumRegion(0, 1, 2, 3)
        # numMatrix.sumRegion(1, 2, 3, 4)

m = NumMatrix([[-1]])
print m.tmp1
print m.sumRegion(0,0,0,0)