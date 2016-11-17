class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        while len(points) > 1:
            nums = reduce(lambda x, y: x+y, points)
            p = None
            nb = 0
            for n in nums:
                tmp = filter(lambda p: self.in_arr(n, p), points)
                if len(tmp) > nb:
                    nb = len(tmp)
                    p = tmp
            res += 1
        return res + 1


    def in_arr(self, n, arr):
        return arr[0] <= n <= arr[1]

print Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]])

