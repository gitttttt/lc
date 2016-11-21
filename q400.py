class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n
        arr = map(lambda x: (x+1) * 9 * 10**x, [i for i in range(9)])
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        index = 0
        for i in range(len(arr)):
            if arr[i] > n:
                index = i-1
                break
        rest = n - arr[index]
        a, b = rest/(index+2), rest%(index+2)
        print arr, 'i', index, 'r', rest, 'a', a, 'b', b, 'n'
        if not b:
            return str(10 ** (index+1) + a-1)[-1]
        now = 10 ** (index+1) + a

        return str(now)[b-1]




print Solution().findNthDigit(11)