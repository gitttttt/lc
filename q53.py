class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        tmp = nums[0]
        for i in nums[1:]:
            if tmp < 0:
                tmp = 0
            tmp = tmp + i
            res = max(tmp, res)
        return res

print Solution().maxSubArray([1])