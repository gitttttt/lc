import sys
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        print bin(n)
        while n > m:
            n &= (n-1)
            print bin(n)
        return n


print Solution().rangeBitwiseAnd(1024,1088)
