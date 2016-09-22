class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        zd = [0 for _ in nums]
        fx = [0 for _ in nums]
        if nums[0] > 0:
            zd[0] = nums[0]
        elif nums[0] < 0:
            fx[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                zd[i] = max(zd[i-1] * nums[i], nums[i])
                fx[i] = fx[i-1] * nums[i]
            elif nums[i] < 0:
                zd[i] = fx[i-1] * nums[i]
                fx[i] = min(zd[i-1] * nums[i], nums[i])
        print zd
        print fx
        return max(zd)

print Solution().maxProduct([-2, 0, 2, -3, 5])
