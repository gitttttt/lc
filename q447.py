class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def f(i):
            if i == 2:
                return
        m = {}
        for i in range(len(points)-1):
            for j in range(i, len(points)):
                d = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if d not in m:
                    m[d] = 0
                m[d] += 1
