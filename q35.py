class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) / 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        print left, right
        return left + 1 if nums[left] < target else left

print Solution().searchInsert([1,2,3,5], 4)