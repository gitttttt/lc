class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        tmp = [0 for _ in range(8)]
        tmp = [1, 10, 100, 1000, 10000, 100000]
        tmp[0] = 9
        for i in range(1, 8):
            tmp[i] = tmp[i-1] * 10
        for i in range(1, 8):
            tmp[i] = tmp[i-1] + tmp[i] * (i+1)
        while n > 0:
            index = 7
            while n < tmp[index]:
                index -= 1
            n -= tmp[index]
        print tmp


Solution().findNthDigit(10)
print 2**31