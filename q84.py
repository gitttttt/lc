class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = [0 for _ in heights]
        r = [0 for _ in heights]
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                l[i] = 0
            elif heights[i] == heights[i-1]:
                l[i] = l[i-1] + 1
            else:
                li = i
                while li >= 0 and heights[li] >= heights[i]:
                    li -= 1
                l[i] = i-li-1
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > heights[i+1]:
                r[i] = 0
            elif heights[i] == heights[i-1]:
                r[i] = r[i-1] + 1
            else:
                ri = i
                while ri < len(heights) and heights[ri] >= heights[i]:
                    ri += 1
                r[i] = ri-i-1
        print l, r
        res = 0
        for i in range(len(heights)):
            res = max(res, (l[i] + r[i] + 1) * heights[i])
        return res


print Solution().largestRectangleArea([3,21,2])
