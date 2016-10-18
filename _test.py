class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        n = 0
        for i in nums:
            if n < 0:
                n = 0
            n += i
            m = max(m, n)
        return m

print Solution().maxSubArray([-2])