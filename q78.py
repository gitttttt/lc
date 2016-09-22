class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            res = res[::] + map(lambda x: x + [i], res[::])
            print res
        return res

print Solution().subsets([1, 2])
