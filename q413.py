class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        diff = [0 for _ in range(len(A)-1)]
        for i in range(len(A)-1):
            diff[i] = A[i+1] - A[i]
        print diff
        i = 1
        now = diff[0]
        count = 1
        res = 0
        while i < len(diff):
            if diff[i] == now:
                count += 1
            else:
                if count >= 2:
                    res += (count-1) * count / 2
                    print '1', (count-1) * count / 2
                now = diff[i]
                count = 1
            i += 1
        print count
        if count >= 2:
            res += (count-1) * count / 2
            print '2', (count-1) * count / 2
        return res

a =  [1, 2, 3, 8,9,10]
print Solution().numberOfArithmeticSlices(a)
