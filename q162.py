class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        i = 1
        res = []
        while i<len(nums)-1:
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            else:
                i += 1
        return None

print Solution().findPeakElement([1,2,3,2,4,2,1])
