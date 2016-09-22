class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        toright = [1 for _ in nums]
        toleft = [1 for _ in nums]
        for i in range(1, len(nums)):
            toright[i] = toright[i-1] * nums[i-1]
            toleft[len(nums)-i-1] = toleft[len(nums)-i] * nums[len(nums)-i]
        return map(lambda x: x[0]*x[1], zip(toright, toleft))

print Solution().productExceptSelf([1,2])
