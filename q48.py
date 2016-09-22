class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)/2):
            for j in range(i, len(matrix)-1-i):
                matrix[i][j], matrix[j][len(matrix)-1-i], \
                matrix[len(matrix)-1-i][len(matrix)-1-j], matrix[len(matrix)-1-j][i] =\
                matrix[len(matrix)-1-j][i], matrix[i][j],\
                matrix[j][len(matrix)-1-i], matrix[len(matrix)-1-i][len(matrix)-1-j]


m = [[1,2,3], [4,5,6], [7,8,9]]
Solution().rotate(m)
print m