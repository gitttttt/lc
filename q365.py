class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        x, y = max(x, y), min(x, y)
        if x == y:
            return x == z or z == 0
        if x == 0 or y == 0:
            return x+y == z or z == 0
        i = 0
        while i * y <= x:
            i += 1
        j = i * y - x
        res = [k * y for k in range(i)] + \
              [x - k * y for k in range(i)] + \
              [j + k * y for k in range(i)] + \
              [x+y, x+j, 2*x-(i-1)*y]
        print res
        return z in res

print Solution().canMeasureWater(11,13,13)
