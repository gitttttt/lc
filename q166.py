import time

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not numerator % denominator:
            return str(numerator / denominator)
        sys = '-' if numerator > 0 ^ numerator > 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        z, y, yr = {}, {}, {}
        zs = numerator/denominator
        ys = numerator%denominator
        index = 0
        while ys:
            z[index], y[index] = ys/denominator, ys%denominator
            y[ys%denominator] = index
            if ys in yr:
                start = yr[ys]
                for i in range(start, index):
                    print i
            ys *= 10
            index += 1
            time.sleep(1)
            print z, y


print Solution().fractionToDecimal(-1, -33)