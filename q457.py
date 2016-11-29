class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [(i+v) % len(nums) for i, v in enumerate(nums)]
        print nums

Solution().circularArrayLoop([-1,2])