class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tmp = set()
        while n not in tmp:
            tmp.add(n)
            if n == 1:
                return True
            n = sum(map(lambda x: int(x) * int(x), str(n)))
        return False

print Solution().isHappy(0)