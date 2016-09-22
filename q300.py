class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [1]
        for i in range(1, len(nums)):
            tmp = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, res[j]+1)
            res.append(tmp)
            print res
        return max(res)

print Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])