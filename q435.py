# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def cmp(x, y):
            if x.start == y.start:
                return x.end - y.end
            return x.start - y.start
        intervals.sort(cmp=cmp)
        end = 0
        res = 0
        for i in intervals:
            if i.start >= end:
                end = i.end
                res += 1
            else:
                end = min(end, i.end)
        return res