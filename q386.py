import time

class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        now = 1
        res = []
        for i in range(n):
            res.append(now)
            if now * 10 <= n:
                now *= 10
            elif now + 1 <= n and now % 10 != 9:
                now += 1
            else:
                while (now / 10) % 10 == 9:
                    now /= 10
                now /= 10
                now += 1

        return res

nn = 1111

print Solution().lexicalOrder(nn)

print map(lambda x: int(x), sorted(map(lambda x: str(x), range(1, nn+1))))

time.sleep(10000)
