class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        tmp = [[0 for _ in range(s+1)] for _ in nums]
        for i in range(nums[0], s):
            tmp[0][i] = nums[0]
        for i in range(1, len(nums)):
            for j in range(nums[i], s+1):
                tmp[i][j] = max(tmp[i-1][j], tmp[i-1][j-nums[i]] + nums[i])
        return tmp[-1][s] == s