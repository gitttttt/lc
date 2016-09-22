class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        res = 0
        while n >= 5**i:
            print n / (5**i) * i
            res += n / (5**i)
            i += 1
        return res

print Solution().trailingZeroes(15)