class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = matrix
        tmp = [[0 for _ in m[0]] for _ in m]
        tmp[0] = map(int, m[0])
        for i in range(1, len(m)):
            for j in range(len(m[0])):
                if m[i][j] == '0':
                    tmp[i][j] = 0
                else:
                    tmp[i][j] = tmp[i-1][j] + 1
        res = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if tmp[i][j] != 0:
                    s = j
                    t = 0
                    mn = tmp[i][j]
                    while s >= 0 and tmp[i][s] != 0:
                        mn = min(mn, tmp[i][s])
                        t = max(t, mn * (j-s+1))
                        s -= 1
                    res = max(res, t)
        return res

m = ["10100","10111","11111","10010"]
print Solution().maximalRectangle(m)


