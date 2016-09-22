class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = max(lambda x: x[0]-x[1], zip(gas, cost))
        start = 0
        cur = 0
        max_ = 0
        for i in range(len(diff)):
            if cur <= 0:
                start = i
                cur = 0
            cur += diff[i]
            if cur > max_:
                max_ = cur
        return start



