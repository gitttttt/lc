class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = map(lambda x: map(lambda x: int(x), list(x)), matrix)
        res = [[[0,0] for x in range(len(matrix[0]))] for x in range(len(matrix))]
        result = 0
        for i, v in enumerate(matrix[0]):
            if v == 1:
                res[0][i] = [1,1]
                result = 1
        for i, v in enumerate(matrix):
            if v[0] == 1:
                res[i][0] = [1,1]
                result = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 1:
                    result = max(result, res[i][j][0] * res[i][j][1])
        print res
        return result

print Solution().maximalRectangle(["10100","10111","11111","10010"])
