class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) / 2
            num = len(filter(lambda x: x <= mid, nums))
            if mid < num:
                right = mid - 1
            else:
                left = mid + 1
        return left

print Solution().findDuplicate([2,1,1])


