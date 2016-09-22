class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = int("".join(map(lambda x: str(x), b)))
        chu = b
        num, tmp = 0, 1
        while tmp < 1337:
            num += 1
            tmp *= a
        print num
        while tmp >= 1337:
            chu, yu = chu / num, chu % num
            print chu, yu
            tmp = ((tmp - 1337) ** chu) * (a ** yu)
        print tmp

Solution().superPow(3, [1,0])