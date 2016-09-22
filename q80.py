class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end, res, index = 0, 1, 0, 0
        while start < len(nums) and end < len(nums):
            if nums[start] == nums[end]:
                res += 2
                while end < len(nums) and nums[end] == nums[start]:
                    end += 1
                nums[index], nums[index+1] = nums[start], nums[start]
                start, end, index = end, end + 1, index+2
            else:
                res += 1
                nums[index] = nums[start]
                start += 1
                end += 1
                index += 1
        if start == len(nums):
            nums[index-2] = nums[-1]
            nums[index-1] = nums[-1]
            print nums
            return res
        else:
            nums[index] = nums[-1]
            print nums
            return res+1


print Solution().removeDuplicates([1,1,1,2])