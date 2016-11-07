class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nw = len(str(n))
        kw = len(str(k))
        if nw == 1:
            pass