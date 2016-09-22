class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        matrix = map(lambda x: map(lambda x: int(x), list(x)), matrix)
        res = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
        result = 0
        for i1, v1 in enumerate(matrix):
            for i2, v2 in enumerate(v1):
                if v2 == 1:
                    res[i1][i2] = 1
                    result = max(result, 1)
                if i1 != 0 and i2 != 0:
                    num = res[i1-1][i2-1]
                    if v2 == 1 and i1-num >=0 and i2-num >= 0 and num!= 0:
                        if reduce(lambda a,b: a*b, v1[i2-num:i2:]) == 1 and reduce(lambda a,b: a*b, map(lambda a: a[i2], matrix[i1-num:i1:])) == 1:
                            res[i1][i2] = num + 1
                            result = max(result, num+1)
            print res
            print result

        print res

Solution().maximalSquare(["0001","1101","1111","0111","0111"])
