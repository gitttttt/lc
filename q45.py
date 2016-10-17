import sys

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = [sys.maxint for _ in nums]
        step[0] = 0
        for i in range(1, len(nums)):
            m = sys.maxint
            for j in range(0, i):
                if nums[j] + j >= i:
                    m = min(step[j], m)
            step[i] = m + 1
        print step
        return step[-1]

print Solution().jump([1,2])