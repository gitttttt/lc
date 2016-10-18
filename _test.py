class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = [0 for _ in nums]
        n = [0 for _ in nums]
        if nums[0] > 0:
            p[0] = nums[0]
        elif nums[0] < 0:
            n[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                p[i] = p[i-1] * nums[i] #max(p[i-1] * nums[i], nums[i])
                n[i] = n[i-1] * nums[i]
            elif nums[i] < 0:
                p[i] = n[i-1] * nums[i]
                n[i] = p[i-1] * nums[i] #min(p[i-1] * nums[i], nums[i])
        print p, n
        return max(p)

print Solution().maxProduct([-4,-3,-2])