class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        xl = map(lambda x: reduce(lambda ky, z: ky*z, x), matrix)
        def y(i):
            return reduce(lambda x, y: x*y, map(lambda z: z[i], matrix))
        yl = map(lambda x: y(x), range(len(matrix[0])))
        print 'x', xl, 'y', yl
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not xl[i] * yl[j]:
                    matrix[i][j] = 0

m = [[0,1]]
print Solution().setZeroes(m)
print m