class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        start, exp = 0, ""
        res = []
        for i in range(len(nums)):
            if exp == "":
                exp = nums[i] + 1
                start = i
            else:
                if nums[i] == exp:
                    exp += 1
                else:
                    if i-1 == start:
                        res.append(str(nums[start]))
                    else:
                        res.append(str(nums[start]) + '->' + str(nums[i-1]))
                    start = i
                    exp = nums[i] + 1
        if len(nums)-1 == start:
            res.append(str(nums[start]))
        else:
            res.append(str(nums[start]) + '->' + str(nums[-1]))
        return res

print Solution().summaryRanges([-2,-1,1,2,2147483646,2147483647])
