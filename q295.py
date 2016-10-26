import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []
        self.b = []
        self.n = 0


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.s) == len(self.b):
            heapq.heappush(self.b, -num)
            heapq.heappush(self.s, -heapq.heappop(self.b))
        else:
            heapq.heappush(self.s, num)
            heapq.heappush(self.b, heapq.heappop(self.s))
        self.n = 1

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.n == 0:
            return 0
        if self.n % 2:
            return float(self.s[0])
        else:
            return (self.s[0] + self.b[0]) / 2.0


        # Your MedianFinder object will be instantiated and called as such:
        # mf = MedianFinder()
        # mf.addNum(1)
        # mf.findMedian()
m = MedianFinder()
i = -5
while i <= 0:
    m.addNum(i)
    print m.findMedian()
    print m.b, m.s
    print
    i += 1