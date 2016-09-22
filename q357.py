class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp, res = 9, 10
        for i in range(1, n):
            tmp *= (10 - i)
            res += tmp
        return res

print Solution().countNumbersWithUniqueDigits(111)