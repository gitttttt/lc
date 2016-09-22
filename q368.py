class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = [1 for _ in nums]
        for i in range(1, len(nums)):
            tmp = 1
            for j in range(0, i):
                if not nums[i] % nums[j]:
                    tmp = max(tmp, res[j] + 1)
            res[i] = tmp
        print res
        result = []
        m = max(res)
        maxindex = res.index(max(res))
        maxnum = nums[maxindex]
        for i in range(0, len(nums))[::-1]:
            if not maxnum % nums[i] and res[i] == m:
                m -= 1
                result.append(nums[i])
        return result

print Solution().largestDivisibleSubset([1,2,4,9,81,729])