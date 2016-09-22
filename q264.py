class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        res, index, minum = [1], 1, 0
        a, b, c = 0, 0, 0
        while index < n:
            minum = min(res[a] * 2, res[b] * 3, res[c] * 5)
            res.append(minum)
            if res[a] * 2 == minum:
                a += 1
            if res[b] * 3 == minum:
                b += 1
            if res[c] * 5 == minum:
                c += 1
            index += 1
        return minum



for i in range(1, 12):
    print Solution().nthUglyNumber(i)