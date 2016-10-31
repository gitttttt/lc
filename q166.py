import time

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n, d = numerator, denominator
        l = n/d
        n -= l*d
        tmp = {n: 0}
        c = 0
        while n not in tmp:
            while n < d and n:
                c += 1
                n *= 10
            n -= n/d * d
            if n == 0:
                pass
            tmp[n] = c




print Solution().fractionToDecimal(-1, -33)