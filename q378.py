import heapq

class Solution(object):

    # def kthSmallest(self, matrix, k):
    #     """
    #     :type matrix: List[List[int]]
    #     :type k: int
    #     :rtype: int
    #     """
    #     res = []
    #     for i in matrix:
    #         for j in i:
    #             res.append(j)
    #     res.sort()
    #     return res[k-1]

    def kthSmallest(self, matrix, k):
        print list(heapq.merge(*matrix))


matrix = [
             [ 1,  5,  9],
             [8, 11, 13],
             [12, 13, 15]
         ]
k = 8

print Solution().kthSmallest(matrix, 8)