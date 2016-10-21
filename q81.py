class Solution(object):
    def search(self, nums, target):
        """
        http://blog.csdn.net/linhuanmars/article/details/20588511
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) / 2
            if target == nums[m]:
                return True
            elif nums[r] < nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return False