class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        print i, j
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]

a = [5,1,1]
Solution().nextPermutation(a)
print a
