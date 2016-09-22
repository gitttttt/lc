class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return []
        if n == 1:
            return [0, 1]
        return map(lambda x: x + (1 << n-1), reversed(self.grayCode(n-1))) + self.grayCode(n-1)

print Solution().grayCode(0)
