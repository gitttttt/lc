import sys
sys.maxint

class Solution(object):

    a = 1

    @staticmethod
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = False
        tmp = [i for i in range(1, n+1)]
        while len(tmp) > 1:
            if flag:
                tmp = [v for i, v in enumerate(tmp) if not i % 2]
            else:
                tmp = [v for i, v in enumerate(tmp) if i % 2]
            flag = not flag
            print tmp
        return tmp[0]

print type(Solution.a)
def a(aa, aaa = 1):
    pass

a()