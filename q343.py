class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [-1 for _ in range(n+1)]
        res[1] = 1
        for i in range(2, n+1):
            tmp = 1
            for j in range(1, int(i/2)+1):
                tmp = max(tmp, max(res[i-j], i-j) * max(res[j], j))
                print i, j, res[i-j], res[j]
            res[i] = tmp
        print res
        return res[-1]

Solution().integerBreak(58)

