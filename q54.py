class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        i, j = 0, 0
        d = 1
        num = len(matrix) * len(matrix[0])
        xm = len(matrix) - 1
        ym = len(matrix[0]) - 1
        xn = 0
        yn = 0
        while len(res) < num:
            res.append(matrix[i][j])
            if d == 1:
                if j+1 <= ym:
                    j += 1
                else:
                    xn += 1
                    i += 1
                    d = 2
            elif d == 2:
                if i+1 <= xm:
                    i += 1
                else:
                    ym -= 1
                    j -= 1
                    d = 3
            elif d == 3:
                if j-1 >= yn:
                    j -= 1
                else:
                    xm -= 1
                    i -= 1
                    d = 4
            else:
                if i-1 >= xn:
                    i -= 1
                else:
                    yn += 1
                    j += 1
                    d = 1
        return res

m = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
n = []
k = [[1,2], [3,4]]
print Solution().spiralOrder(n)
