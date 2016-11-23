class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        res = 0
        for arr in [A, B, C, D]:
            arr.sort()
        i, j = 0, 0
        tmpA = 0
        tmpB = 0
        while i < len(A):
            if i > 0 and A[i] == A[i-1]:
                res += tmpA
            else:
                j = 0
                tmpA = 0
                while j < len(B):
                    m = 0
                    n = len(D) - 1
                    while m < len(C) and n > -1:
                        if A[i] + B[j] + C[m] + D[n] == 0:
                            mm = m
                            nn = n
                            n1, n2 = 0, 0
                            while mm < len(C) and C[mm] == C[m]:
                                n1 += 1
                                mm += 1
                            while nn > -1 and D[nn] == D[n]:
                                n2 += 1
                                nn -= 1
                            m = mm
                            n = nn
                            tmpA += n1 * n2
                        elif A[i] + B[j] + C[m] + D[n] < 0:
                            m += 1
                        else:
                            n -= 1
                    j += 1
                res += tmpA
            i += 1
        return res

a, b, c, d = [0,1,-1],[-1,1,0],[0,0,1],[-1,1,1]
print Solution().fourSumCount(a,b,c,d)

