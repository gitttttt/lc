class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        i = 0
        while i < len(nums):
            if nums[i] != i+1:
                if nums[i] > len(nums) or nums[i]-1<0 or nums[i]-1 >= len(nums)or nums[i] == nums[nums[i]-1]:
                    break
                else:
                    nums[nums[i]-1] = nums[i]
                    nums[i] = i+1
            else:
                i += 1
            print nums
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return max(nums) + 1

print Solution().firstMissingPositive([0, 1, 2])