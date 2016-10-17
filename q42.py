class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        m = max(height)
        mi = height.index(m)
        mm = 0
        l = 0
        r = len(height)-1
        res = 0
        print mi, 'yy'
        while l < mi:
            if height[l] > mm:
                mm = height[l]
            else:
                res += mm - height[l]
            l += 1
        mm = 0
        print res
        while r >= mi:
            if height[r] > mm:
                mm = height[r]
            else:
                res += mm - height[r]
            r -= 1
            print r
        return res

print Solution().trap([2,0,2])
