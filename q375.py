import sys

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for l in range(1, n)[::-1]:
            for r in range(l+1, n+1):
                tmp = sys.maxint
                for m in range(l, r):
                    tmp = min(tmp, m + max(res[l][m-1], res[m+1][r]))
                res[l][r] = tmp
        return res[1][n]

print Solution().getMoneyAmount(1)