class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums.sort()
        tmp = [[nums[0]]]
        res = [[], [nums[0]]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                res += map(lambda x: x+[nums[i]], tmp)
                tmp = map(lambda x: x+[nums[i]], tmp)
            else:
                tmp = map(lambda x: x+[nums[i]], res)
                res += tmp
        return res

print Solution().subsetsWithDup([])