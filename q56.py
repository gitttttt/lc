# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):

    # def merge(self, intervals):
    #     """
    #     :type intervals: List[Interval]
    #     :rtype: List[Interval]
    #     """
    #     if len(intervals) == 1:
    #         return intervals
    #     rest = self.merge(intervals[1:])
    #     start, end = 0, 0
    #     first = intervals[0]
    #     for i in range(len(rest)):
    #         if first.start < rest[i].start:
    #             start = len(rest) + i
    #         elif rest[i].start <= first.start <= rest[i].end:
    #             start = i
    #         if first.end > rest[i].end:
    #             end = len(rest) + i
    #         elif rest[i].start <= first.end <= rest[i].end:
    #             end = i
    #     if len(rest) >= start > end or end < start < len(rest):
    #         rest.insert(start, first)
    #         return rest
    #     if start >= len(rest) and end >= len(rest):
    #         return rest[:start-len(rest)] + Interval(first.start, first.end) + rest[end-len(rest)+1:]
    #     if start <= len(rest) <= end:
    #         return rest[:start-1] + Interval(rest[start].start, first.end) + rest[end-len(rest)+1:]
    #     if end <= len(rest) <= start:
    #         return rest[:start-len(rest)] + Interval(first.start, rest[end].end) + rest[end+1:]
    #     if start <= len(rest) and end <= len(rest):
    #         return rest[:start-1] + Interval(rest[start].start, rest[end].end) + rest[end+1:]

    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(cmp=lambda x, y: x.start < y.start)
        for i in intervals:
            print i.start, i.end, '000'
        res = []
        start = intervals[0].start
        end = intervals[0].end
        for i in range(len(intervals)):
            itv = intervals[i]
            if itv.start <= end:
                end = max(end, itv.end)
            else:
                res.append(Interval(start, end))
                start = itv.start
                end = itv.end
        res.append(Interval(start, end))
        return res

a = [Interval(1,4), Interval(0, 4)]
for i in Solution().merge(a):
    print i.start, i.end

