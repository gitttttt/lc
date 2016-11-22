class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 1
        points.sort()
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1])
            else:
                res += 1
                end = points[i][1]
        return res



    def in_arr(self, n, arr):
        return arr[0] <= n <= arr[1]

print Solution().findMinArrowShots([[10,16], [2,8], [7,6], [7,12]])

