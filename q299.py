class Solution(object):
    def getHint(self, secret, guess):
        eq = 0
        nq = 0
        tmp1, tmp2 = [], []
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                eq += 1
            else:
                tmp1.append(secret[i])
                tmp2.append(guess[i])
        i1, i2 = 0, 0
        tmp1.sort()
        tmp2.sort()
        while i1 < len(tmp1) and i2 < len(tmp2):
            if tmp1[i1] == tmp2[i2]:
                nq += 1
                i1 += 1
                i2 += 1
            elif tmp1[i1] < tmp2[i2]:
                i1 += 1
            else:
                i2 += 1
        return str(eq) + 'A' + str(nq) + 'B'

print Solution().getHint('1123', '0111')