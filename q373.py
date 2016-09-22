import heapq

class Value:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def __le__(self, other):
        return self.c - other.c

    def __str__(self):
        return str(self.a)


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        heap, num, res = [], 0, []
        for i in nums1:
            for j in nums2:
                if num < k:
                    heapq.heappush(heap, Value(i, j, i+j))
                    num += 1
                    print heap
                else:
                    if heap[0] > i+j:
                        res.append([heapq.heappop(heap).a, heapq.heappop(heap).b])
                        heapq.heappush(heap, Value(i, j, i+j))
        print res

Solution().kSmallestPairs([1,7,11], [2,4,6], 3)
