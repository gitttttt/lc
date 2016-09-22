class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = sum(A)
        tmp = map(lambda x: s-x, A)[::-1]
        print tmp
        res = sum(map(lambda x: x[0] * x[1], zip(A, [i for i in range(len(A))])))
        cur = res
        for i in range(0, len(A)):

            cur = cur + tmp[i] - A[-i-1]*(len(A)-1)
            res = max(cur, res)
        return res

a = [i for i in range(10000)]
print Solution().maxRotateFunction(a)