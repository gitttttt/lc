class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        if x[2] > x[0] and x[3] > x[1]:
            flag = True
        elif x[3] < x[1]:
            flag = False
        else:
            return False
