from sys import maxint
import math, time

class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [maxint] * (n+1)
        res[0] = 0
        for i in range(0, n+1):
            for j in range(1, int(math.sqrt(n-i)) + 1):
                if j * j == i:
                    res[i] = 1
                res[i + j * j] = min(res[i + j * j], res[i] + 1)
        return res[-1]

start = time.time()
print Solution().numSquares(7334)
print time.time() - start

