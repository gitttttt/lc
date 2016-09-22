class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n % 2:
            return self.integerReplacement(n/2) + 1
        else:
            return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1

print Solution().integerReplacement(61)
