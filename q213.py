class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        yes = [0 for _ in nums[1:]]
        yes[0], yes[1] = nums[0], nums[0]
        no = [0 for _ in nums[1:]]
        no[1] = nums[1]
        for i in range(2, len(nums)-1):
            yes[i] = max(yes[i-1], yes[i-2] + nums[i])
            no[i] = max(no[i-1], no[i-2] + nums[i])
        print yes
        print no
        return max(yes[-1], no[-1]+nums[-1])

Solution().rob([1,1,1])
